"""
03_analisar.py
==============

Executa as analises e gera os indicadores que compoem a Secao 5 do
artigo (Resultados):
  - I1: contagem de pesquisadores por nivel de formacao maxima
  - I2: producao de artigos em periodicos por pesquisador (top 10)
  - I3: artigos publicados por ano (serie temporal)
  - I4: orientacoes em andamento por nivel
  - I5: rede de coautoria interna do PPGEP

As consultas sao escritas em duas variantes:
  (a) usando pipelines de agregacao do MongoDB (via pymongo)
  (b) usando pandas, para o leitor que nao tenha o servidor disponivel

Saidas:
  - indicadores.csv     tabelas por indicador
  - figuras/*.png       graficos correspondentes
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

try:
    from pymongo import MongoClient
    PYMONGO_OK = True
except ImportError:
    PYMONGO_OK = False


# ---------------------------------------------------------------------------
# Carga dos JSONs (modo offline, sem MongoDB)
# ---------------------------------------------------------------------------

def carrega_jsons(pasta: Path) -> list[dict[str, Any]]:
    pesquisadores = []
    for caminho in sorted(pasta.glob("Pesquisador_*.json")):
        with caminho.open(encoding="utf-8") as f:
            pesquisadores.append(json.load(f))
    return pesquisadores


# ---------------------------------------------------------------------------
# I1 -- Distribuicao por nivel maximo de formacao
# ---------------------------------------------------------------------------

def i1_formacao_maxima(pesquisadores: list[dict]) -> pd.DataFrame:
    ordem = {"Pos-Doutorado": 5, "Doutorado": 4, "Mestrado": 3,
             "Especializacao": 2, "Graduacao": 1}
    contagem = Counter()
    for doc in pesquisadores:
        formacoes = doc.get("formacao_academica", [])
        nivel_atual = 0
        nome_atual = "Desconhecido"
        for f in formacoes:
            tipo = (f.get("tipo") or "").split(" em ")[0]
            chave = tipo.replace("Pos-Doutorado", "Pos-Doutorado")
            valor = ordem.get(chave, 0)
            if valor > nivel_atual:
                nivel_atual = valor
                nome_atual = chave
        contagem[nome_atual] += 1
    df = (pd.DataFrame(contagem.items(), columns=["nivel", "n_pesquisadores"])
            .sort_values("n_pesquisadores", ascending=False))
    return df


# ---------------------------------------------------------------------------
# I2 -- Producao de artigos em periodicos por pesquisador (top 10)
# ---------------------------------------------------------------------------

def i2_artigos_por_pesquisador(pesquisadores: list[dict]) -> pd.DataFrame:
    linhas = []
    for doc in pesquisadores:
        nome = doc.get("informacoes_pessoais", {}).get("nome_completo", "")
        artigos = doc.get("producao_bibliografica", {}).get("artigos_periodicos", [])
        linhas.append({"pesquisador": nome, "n_artigos": len(artigos)})
    df = pd.DataFrame(linhas).sort_values("n_artigos", ascending=False)
    return df


# ---------------------------------------------------------------------------
# I3 -- Artigos por ano (serie temporal agregada do PPGEP)
# ---------------------------------------------------------------------------

def i3_artigos_por_ano(pesquisadores: list[dict]) -> pd.DataFrame:
    contagem: Counter = Counter()
    for doc in pesquisadores:
        artigos = doc.get("producao_bibliografica", {}).get("artigos_periodicos", [])
        for a in artigos:
            ano = a.get("ano")
            try:
                ano = int(ano)
            except (ValueError, TypeError):
                continue
            if 1990 <= ano <= 2026:
                contagem[ano] += 1
    df = (pd.DataFrame(contagem.items(), columns=["ano", "n_artigos"])
            .sort_values("ano"))
    return df


# ---------------------------------------------------------------------------
# I4 -- Orientacoes em andamento por nivel
# ---------------------------------------------------------------------------

def i4_orientacoes_em_andamento(pesquisadores: list[dict]) -> pd.DataFrame:
    contagem: Counter = Counter()
    for doc in pesquisadores:
        emand = doc.get("orientacoes", {}).get("em_andamento", {})
        for nivel, itens in emand.items():
            if isinstance(itens, list):
                contagem[nivel] += len(itens)
    df = (pd.DataFrame(contagem.items(), columns=["nivel", "n_orientacoes"])
            .sort_values("n_orientacoes", ascending=False))
    return df


# ---------------------------------------------------------------------------
# I5 -- Rede de coautoria interna ao PPGEP
# ---------------------------------------------------------------------------

def i5_rede_coautoria(pesquisadores: list[dict]) -> pd.DataFrame:
    """Conta quantos artigos sao co-assinados por pares de pesquisadores
    do PPGEP, identificando-os pelo pseudonimo presente na string de
    autores.
    """
    pseudonimos = {doc.get("informacoes_pessoais", {}).get("nome_completo")
                   for doc in pesquisadores}
    pseudonimos.discard(None)

    pares: Counter = Counter()
    for doc in pesquisadores:
        autor = doc.get("informacoes_pessoais", {}).get("nome_completo")
        for art in doc.get("producao_bibliografica", {}).get("artigos_periodicos", []):
            autores_texto = art.get("autores") or ""
            coautores = {p for p in pseudonimos if p in autores_texto and p != autor}
            for c in coautores:
                par = tuple(sorted([autor, c]))
                pares[par] += 1
    df = (pd.DataFrame([(a, b, n) for (a, b), n in pares.items()],
                       columns=["pesquisador_a", "pesquisador_b", "n_artigos"])
            .sort_values("n_artigos", ascending=False))
    # Cada par aparece duas vezes (um por pesquisador); deduplicamos
    return df.drop_duplicates()


# ---------------------------------------------------------------------------
# Geracao dos graficos
# ---------------------------------------------------------------------------

def salva_barra(df: pd.DataFrame, x: str, y: str, titulo: str,
                destino: Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(df[x].astype(str), df[y], color="#2b3a55")
    ax.set_title(titulo)
    ax.set_ylabel(y)
    ax.set_xlabel(x)
    plt.xticks(rotation=45, ha="right")
    fig.tight_layout()
    fig.savefig(destino, dpi=150)
    plt.close(fig)


def salva_linha(df: pd.DataFrame, x: str, y: str, titulo: str,
                destino: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df[x], df[y], marker="o", color="#d97b00")
    ax.fill_between(df[x], df[y], alpha=0.2, color="#d97b00")
    ax.set_title(titulo)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(destino, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Pipelines de agregacao MongoDB (versao para o artigo)
# ---------------------------------------------------------------------------

PIPELINE_I3_MONGODB = [
    {"$unwind": "$producao_bibliografica.artigos_periodicos"},
    {"$group": {
        "_id": "$producao_bibliografica.artigos_periodicos.ano",
        "n_artigos": {"$sum": 1}
    }},
    {"$match": {"_id": {"$gte": 1990, "$lte": 2026}}},
    {"$sort": {"_id": 1}},
]

PIPELINE_I2_MONGODB = [
    {"$project": {
        "pesquisador": "$informacoes_pessoais.nome_completo",
        "n_artigos": {"$size": {
            "$ifNull": ["$producao_bibliografica.artigos_periodicos", []]
        }}
    }},
    {"$sort": {"n_artigos": -1}},
    {"$limit": 10},
]


# ---------------------------------------------------------------------------
# Pipeline principal
# ---------------------------------------------------------------------------

def executa(entrada: Path, saida_tabelas: Path, saida_figuras: Path) -> None:
    saida_tabelas.mkdir(parents=True, exist_ok=True)
    saida_figuras.mkdir(parents=True, exist_ok=True)

    pesquisadores = carrega_jsons(entrada)
    print(f"[+] {len(pesquisadores)} pesquisadores carregados")

    # I1
    i1 = i1_formacao_maxima(pesquisadores)
    i1.to_csv(saida_tabelas / "I1_formacao_maxima.csv", index=False)
    salva_barra(i1, "nivel", "n_pesquisadores",
                "I1 -- Distribuicao por formacao maxima",
                saida_figuras / "I1_formacao_maxima.png")

    # I2 -- top 10
    i2 = i2_artigos_por_pesquisador(pesquisadores).head(10)
    i2.to_csv(saida_tabelas / "I2_top10_artigos.csv", index=False)
    salva_barra(i2, "pesquisador", "n_artigos",
                "I2 -- Top 10: artigos em periodicos por pesquisador",
                saida_figuras / "I2_top10_artigos.png")

    # I3
    i3 = i3_artigos_por_ano(pesquisadores)
    i3.to_csv(saida_tabelas / "I3_artigos_por_ano.csv", index=False)
    salva_linha(i3, "ano", "n_artigos",
                "I3 -- Producao anual de artigos do PPGEP",
                saida_figuras / "I3_artigos_por_ano.png")

    # I4
    i4 = i4_orientacoes_em_andamento(pesquisadores)
    i4.to_csv(saida_tabelas / "I4_orientacoes_em_andamento.csv", index=False)
    salva_barra(i4, "nivel", "n_orientacoes",
                "I4 -- Orientacoes em andamento por nivel",
                saida_figuras / "I4_orientacoes_em_andamento.png")

    # I5
    i5 = i5_rede_coautoria(pesquisadores)
    i5.to_csv(saida_tabelas / "I5_rede_coautoria.csv", index=False)

    print("[+] Indicadores e graficos gerados em:")
    print(f"    Tabelas:  {saida_tabelas}")
    print(f"    Figuras:  {saida_figuras}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--entrada", type=Path, required=True,
                   help="Pasta com os JSONs anonimizados")
    p.add_argument("--saida-tabelas", type=Path, default=Path("./tabelas"),
                   help="Pasta destino das tabelas (CSV)")
    p.add_argument("--saida-figuras", type=Path, default=Path("./figuras"),
                   help="Pasta destino dos graficos (PNG)")
    args = p.parse_args()
    executa(args.entrada, args.saida_tabelas, args.saida_figuras)


if __name__ == "__main__":
    main()
