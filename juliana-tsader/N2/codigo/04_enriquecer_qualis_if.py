"""
04_enriquecer_qualis_if.py
==========================

Enriquece os artigos extraidos com dois atributos externos:

  - Estrato Qualis: lido de um CSV publico baixado da CAPES
    (https://sucupira.capes.gov.br/ -- planilha por area de avaliacao).
    O arquivo deve estar em ./referencias/qualis_engenharias.csv com
    pelo menos as colunas: issn, titulo, estrato.

  - Fator de Impacto (IF): lido de um CSV elaborado pela autora a
    partir de relatorios do JCR/Scopus (./referencias/if_periodicos.csv,
    colunas: issn, fator_impacto, ano_referencia).

O script atualiza a colecao 'artigos' do MongoDB acrescentando os
campos 'estrato_qualis' e 'fator_impacto' a cada documento. Em
seguida, calcula e salva indicadores agregados:

  - I6: distribuicao por estrato Qualis (numero e percentual)
  - I7: fator de impacto medio ponderado por pesquisador

Em execucao offline (sem MongoDB), o script faz a mesma juncao em
pandas a partir dos JSONs anonimizados.

Uso:
    python 04_enriquecer_qualis_if.py \\
        --entrada ../dados_anonimizados \\
        --qualis ../referencias/qualis_engenharias.csv \\
        --if-csv ../referencias/if_periodicos.csv \\
        --saida-tabelas ../tabelas \\
        --saida-figuras ../figuras
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Optional

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


COR_PRIMARIA = "#2b3a55"
COR_DESTAQUE = "#d97b00"

# Ordem oficial dos estratos Qualis (2017 em diante)
ESTRATOS = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C", "Nao Classificado"]


# ---------------------------------------------------------------------------
# Carga das tabelas de referencia
# ---------------------------------------------------------------------------

def carrega_qualis(caminho: Path) -> dict[str, str]:
    """Le o CSV de Qualis e devolve um dicionario {issn_normalizado: estrato}.

    Espera colunas 'issn' e 'estrato' (case-insensitive).
    Aceita ISSNs com ou sem hifen.
    """
    df = pd.read_csv(caminho, dtype=str).fillna("")
    cols = {c.lower(): c for c in df.columns}
    if "issn" not in cols or "estrato" not in cols:
        raise SystemExit(
            f"CSV de Qualis em {caminho} precisa ter colunas 'issn' e 'estrato'"
        )
    mapa = {}
    for _, row in df.iterrows():
        issn = _normaliza_issn(row[cols["issn"]])
        estrato = row[cols["estrato"]].upper().strip()
        if issn and estrato:
            mapa[issn] = estrato
    return mapa


def carrega_if(caminho: Path) -> dict[str, float]:
    """Le o CSV de fator de impacto e devolve {issn_normalizado: if_float}."""
    df = pd.read_csv(caminho, dtype=str).fillna("")
    cols = {c.lower(): c for c in df.columns}
    if "issn" not in cols or "fator_impacto" not in cols:
        raise SystemExit(
            f"CSV de IF em {caminho} precisa ter colunas 'issn' e 'fator_impacto'"
        )
    mapa = {}
    for _, row in df.iterrows():
        issn = _normaliza_issn(row[cols["issn"]])
        try:
            valor = float(str(row[cols["fator_impacto"]]).replace(",", "."))
        except ValueError:
            continue
        if issn:
            mapa[issn] = valor
    return mapa


def _normaliza_issn(valor: str) -> str:
    """Remove caracteres nao alfanumericos e converte para maiusculas."""
    if not valor:
        return ""
    limpo = "".join(c for c in valor.upper() if c.isalnum())
    return limpo


# ---------------------------------------------------------------------------
# Enriquecimento sobre os JSONs anonimizados (modo offline)
# ---------------------------------------------------------------------------

def enriquece_artigos(jsons: Path,
                      qualis: dict[str, str],
                      ifs: dict[str, float]) -> pd.DataFrame:
    linhas = []
    for caminho in sorted(jsons.glob("Pesquisador_*.json")):
        with caminho.open(encoding="utf-8") as f:
            doc = json.load(f)
        pseudo = doc.get("informacoes_pessoais", {}).get("nome_completo", "")
        for art in doc.get("producao_bibliografica", {}).get(
                "artigos_periodicos", []):
            issn = _normaliza_issn(art.get("issn") or "")
            linhas.append({
                "pesquisador": pseudo,
                "titulo": art.get("titulo"),
                "ano": art.get("ano"),
                "revista": art.get("revista"),
                "issn": issn,
                "estrato_qualis": qualis.get(issn, "Nao Classificado"),
                "fator_impacto": ifs.get(issn, None),
            })
    return pd.DataFrame(linhas)


# ---------------------------------------------------------------------------
# I6 -- Distribuicao por estrato Qualis
# ---------------------------------------------------------------------------

def i6_distribuicao_qualis(df: pd.DataFrame) -> pd.DataFrame:
    contagem = df["estrato_qualis"].value_counts().reindex(ESTRATOS).fillna(0)
    total = contagem.sum()
    out = pd.DataFrame({
        "estrato": contagem.index,
        "n_artigos": contagem.astype(int).values,
        "percentual": (contagem / total * 100).round(2).values,
    })
    return out


def plota_i6(df: pd.DataFrame, destino: Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 4.5))
    cores = ["#1b5e20" if e.startswith("A") else
             "#558b2f" if e.startswith("B") else
             "#9e9d24" if e == "C" else "#777"
             for e in df["estrato"]]
    barras = ax.bar(df["estrato"], df["n_artigos"], color=cores)
    for b, v, p in zip(barras, df["n_artigos"], df["percentual"]):
        ax.text(b.get_x() + b.get_width() / 2, v + max(df["n_artigos"]) * 0.01,
                f"{int(v)}\n({p:.1f}%)", ha="center", va="bottom", fontsize=9)
    ax.set_ylabel("Numero de artigos")
    ax.set_title("I6 -- Distribuicao da producao por estrato Qualis")
    fig.tight_layout()
    fig.savefig(destino, dpi=160, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# I7 -- Fator de impacto ponderado por pesquisador
# ---------------------------------------------------------------------------

def i7_if_por_pesquisador(df: pd.DataFrame) -> pd.DataFrame:
    com_if = df.dropna(subset=["fator_impacto"]).copy()
    agg = (com_if.groupby("pesquisador")
                  .agg(n_artigos_com_if=("fator_impacto", "count"),
                       if_medio=("fator_impacto", "mean"),
                       if_acumulado=("fator_impacto", "sum"))
                  .round(3)
                  .sort_values("if_acumulado", ascending=False)
                  .reset_index())
    return agg


def plota_i7(df: pd.DataFrame, destino: Path, top_n: int = 10) -> None:
    head = df.head(top_n)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.barh(head["pesquisador"][::-1], head["if_acumulado"][::-1],
            color=COR_DESTAQUE)
    for i, (n, v) in enumerate(zip(head["pesquisador"][::-1],
                                    head["if_acumulado"][::-1])):
        ax.text(v + 0.2, i, f"{v:.1f}", va="center", fontsize=9)
    ax.set_xlabel("Fator de impacto acumulado (soma dos IFs)")
    ax.set_title(f"I7 -- Top {top_n} pesquisadores por IF acumulado")
    fig.tight_layout()
    fig.savefig(destino, dpi=160, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Pipeline principal
# ---------------------------------------------------------------------------

def executa(entrada: Path, qualis_csv: Path, if_csv: Path,
            saida_tabelas: Path, saida_figuras: Path) -> None:
    saida_tabelas.mkdir(parents=True, exist_ok=True)
    saida_figuras.mkdir(parents=True, exist_ok=True)

    print(f"[+] Carregando referencia Qualis de {qualis_csv}")
    qualis = carrega_qualis(qualis_csv)
    print(f"    {len(qualis)} periodicos com Qualis carregados")

    print(f"[+] Carregando referencia IF de {if_csv}")
    ifs = carrega_if(if_csv)
    print(f"    {len(ifs)} periodicos com IF carregados")

    print(f"[+] Enriquecendo artigos a partir de {entrada}")
    df = enriquece_artigos(entrada, qualis, ifs)
    df.to_csv(saida_tabelas / "artigos_enriquecidos.csv", index=False)
    print(f"    {len(df)} artigos processados")

    i6 = i6_distribuicao_qualis(df)
    i6.to_csv(saida_tabelas / "I6_distribuicao_qualis.csv", index=False)
    plota_i6(i6, saida_figuras / "fig06_qualis.png")

    i7 = i7_if_por_pesquisador(df)
    i7.to_csv(saida_tabelas / "I7_if_por_pesquisador.csv", index=False)
    plota_i7(i7, saida_figuras / "fig07_if.png")

    print(f"[+] Tabelas e figuras geradas em {saida_tabelas} e {saida_figuras}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--entrada", type=Path, required=True,
                   help="Pasta com JSONs anonimizados")
    p.add_argument("--qualis", type=Path, required=True,
                   help="CSV com a referencia Qualis (issn, estrato)")
    p.add_argument("--if-csv", dest="if_csv", type=Path, required=True,
                   help="CSV com fatores de impacto (issn, fator_impacto)")
    p.add_argument("--saida-tabelas", type=Path, default=Path("./tabelas"))
    p.add_argument("--saida-figuras", type=Path, default=Path("./figuras"))
    args = p.parse_args()
    executa(args.entrada, args.qualis, args.if_csv,
            args.saida_tabelas, args.saida_figuras)


if __name__ == "__main__":
    main()
