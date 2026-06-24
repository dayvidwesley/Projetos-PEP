"""
01_anonimizar.py
================

Script de anonimizacao dos curriculos Lattes (LGPD).

Le os JSONs originais extraidos pelo scriptLattes, substitui nomes e
identificadores diretos por pseudonimos sequenciais (Pesquisador_001,
Pesquisador_002, ...) e salva os arquivos anonimizados em outra pasta.

Tambem grava um arquivo `mapa_anonimizacao.csv` em pasta segura para
permitir auditoria interna -- esse mapa NAO deve ser comitado no
repositorio publico do GitHub.

Uso:
    python 01_anonimizar.py --entrada <pasta_origem> --saida <pasta_destino>

Exemplo:
    python 01_anonimizar.py --entrada ./dados_originais --saida ./dados_anonimizados
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def normaliza(texto: str) -> str:
    """Remove acentos e converte para minusculas, para comparacoes robustas."""
    if not texto:
        return ""
    nfkd = unicodedata.normalize("NFKD", texto)
    sem_acento = "".join([c for c in nfkd if not unicodedata.combining(c)])
    return sem_acento.lower().strip()


def variacoes_de_citacao(nome_citacoes: str) -> list[str]:
    """Recebe a string 'nome_citacoes' do Lattes (separada por ';') e retorna
    cada variacao individualmente."""
    if not nome_citacoes:
        return []
    return [v.strip() for v in nome_citacoes.split(";") if v.strip()]


# ---------------------------------------------------------------------------
# Construcao do mapa de pseudonimos
# ---------------------------------------------------------------------------

def construir_mapa(arquivos_json: list[Path]) -> dict[str, dict[str, Any]]:
    """Le todos os JSONs e cria um mapa
    {id_lattes_original: {pseudonimo, nome_original, citacoes}}.

    A ordem dos pseudonimos eh alfabetica, garantindo determinismo entre
    execucoes.
    """
    pesquisadores: list[dict[str, Any]] = []

    for caminho in arquivos_json:
        with caminho.open(encoding="utf-8") as f:
            dados = json.load(f)
        info = dados.get("informacoes_pessoais", {})
        pesquisadores.append({
            "arquivo": caminho.name,
            "id_lattes": info.get("id_lattes", ""),
            "nome_completo": info.get("nome_completo", ""),
            "nome_citacoes": info.get("nome_citacoes", ""),
        })

    pesquisadores.sort(key=lambda p: normaliza(p["nome_completo"]))

    mapa: dict[str, dict[str, Any]] = {}
    for i, p in enumerate(pesquisadores, start=1):
        pseudo = f"Pesquisador_{i:03d}"
        novo_id = f"ID_{i:03d}"
        mapa[p["id_lattes"]] = {
            "pseudonimo": pseudo,
            "novo_id": novo_id,
            "nome_original": p["nome_completo"],
            "citacoes": variacoes_de_citacao(p["nome_citacoes"]),
            "arquivo_original": p["arquivo"],
        }
    return mapa


# ---------------------------------------------------------------------------
# Substituicao dos campos sensiveis nos documentos
# ---------------------------------------------------------------------------

CAMPOS_SENSIVEIS_REMOVER = {
    "endereco_profissional",
    "url",
    "atualizacao_cv",
    "texto_resumo",
    "telefone",
    "email",
}


def _substitui_em_string(texto: str, mapa: dict[str, dict[str, Any]]) -> str:
    """Substitui qualquer ocorrencia dos nomes (ou variacoes) dentro de uma
    string pelos pseudonimos correspondentes."""
    if not texto:
        return texto
    for info in mapa.values():
        # Substituicao do nome completo
        if info["nome_original"]:
            padrao = re.escape(info["nome_original"])
            texto = re.sub(padrao, info["pseudonimo"],
                           texto, flags=re.IGNORECASE)
        # Substituicao das variacoes de citacao
        for citacao in info["citacoes"]:
            if len(citacao) < 4:
                continue
            padrao = re.escape(citacao)
            texto = re.sub(padrao, info["pseudonimo"],
                           texto, flags=re.IGNORECASE)
    return texto


def anonimiza_documento(doc: Any, mapa: dict[str, dict[str, Any]]) -> Any:
    """Percorre recursivamente um documento (JSON parseado) e substitui
    nomes e identificadores sensiveis."""
    if isinstance(doc, dict):
        novo = {}
        for chave, valor in doc.items():
            if chave in CAMPOS_SENSIVEIS_REMOVER:
                continue
            if chave == "id_lattes" and isinstance(valor, str):
                novo[chave] = mapa.get(valor, {}).get("novo_id", "ID_XXX")
            elif chave == "nome_completo" and isinstance(valor, str):
                for info in mapa.values():
                    if info["nome_original"] == valor:
                        novo[chave] = info["pseudonimo"]
                        break
                else:
                    novo[chave] = "Pesquisador_XXX"
            elif chave == "nome_citacoes":
                novo[chave] = "Pesquisador_XXX"
            else:
                novo[chave] = anonimiza_documento(valor, mapa)
        return novo

    if isinstance(doc, list):
        return [anonimiza_documento(item, mapa) for item in doc]

    if isinstance(doc, str):
        return _substitui_em_string(doc, mapa)

    return doc


# ---------------------------------------------------------------------------
# Pipeline principal
# ---------------------------------------------------------------------------

def executa(entrada: Path, saida: Path) -> None:
    saida.mkdir(parents=True, exist_ok=True)

    arquivos = sorted(entrada.glob("*.json"))
    if not arquivos:
        raise SystemExit(f"Nenhum JSON encontrado em {entrada}")

    print(f"[+] {len(arquivos)} curriculos encontrados em {entrada}")
    print("[+] Construindo mapa de pseudonimos...")
    mapa = construir_mapa(arquivos)

    # Salva mapa em CSV para auditoria (NAO comitar este arquivo)
    mapa_csv = saida.parent / "mapa_anonimizacao.csv"
    with mapa_csv.open("w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["pseudonimo", "novo_id", "nome_original",
                           "id_lattes_original", "arquivo_original"])
        for id_original, info in mapa.items():
            escritor.writerow([
                info["pseudonimo"], info["novo_id"], info["nome_original"],
                id_original, info["arquivo_original"],
            ])
    print(f"[+] Mapa salvo em {mapa_csv} (NAO COMITAR)")

    print("[+] Anonimizando documentos...")
    for caminho in arquivos:
        with caminho.open(encoding="utf-8") as f:
            doc = json.load(f)
        doc_anon = anonimiza_documento(doc, mapa)

        id_original = doc.get("informacoes_pessoais", {}).get("id_lattes", "")
        pseudo = mapa.get(id_original, {}).get("pseudonimo", "Pesquisador_XXX")
        destino = saida / f"{pseudo}.json"
        with destino.open("w", encoding="utf-8") as f:
            json.dump(doc_anon, f, ensure_ascii=False, indent=2)

    print(f"[+] Concluido. Arquivos anonimizados em: {saida}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--entrada", type=Path, required=True,
                   help="Pasta com os JSONs originais do scriptLattes")
    p.add_argument("--saida", type=Path, required=True,
                   help="Pasta destino dos JSONs anonimizados")
    args = p.parse_args()
    executa(args.entrada, args.saida)


if __name__ == "__main__":
    main()
