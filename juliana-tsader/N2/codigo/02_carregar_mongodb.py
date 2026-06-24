"""
02_carregar_mongodb.py
======================

Carrega os JSONs anonimizados em uma instancia local do MongoDB,
criando uma colecao por entidade conforme o modelo documental
desenhado para o trabalho.

Pre-requisito: MongoDB rodando em mongodb://localhost:27017
(ou em um cluster Atlas, basta trocar a string de conexao).

Uso:
    python 02_carregar_mongodb.py --entrada ./dados_anonimizados \\
        --uri mongodb://localhost:27017 --db ppgep_lattes
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from pymongo import MongoClient


def conecta(uri: str, db: str):
    """Estabelece conexao com o MongoDB e retorna o objeto database.

    A conexao do pymongo eh feita por lazy-loading; o ping abaixo forca
    a verificacao imediata para falhar cedo caso o servidor esteja down.
    """
    cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)
    cliente.admin.command("ping")
    print(f"[+] Conectado em {uri}, base: {db}")
    return cliente[db]


def carrega_documentos(entrada: Path, base) -> None:
    """Insere os documentos anonimizados, espelhando o JSON original em
    uma colecao 'pesquisadores' (modelo agregado, documento embutido).

    Tambem normaliza algumas sub-colecoes para mostrar o padrao de
    referencia, util para demonstrar agregacao em SQL/NoSQL:
      - 'artigos'        (referencia ao pesquisador por id_pseudonimo)
      - 'orientacoes'    (idem)
    """
    arquivos = sorted(entrada.glob("Pesquisador_*.json"))
    print(f"[+] Inserindo {len(arquivos)} documentos em 'pesquisadores'")

    base.pesquisadores.drop()
    base.artigos.drop()
    base.orientacoes.drop()

    for caminho in arquivos:
        with caminho.open(encoding="utf-8") as f:
            doc = json.load(f)
        info = doc.get("informacoes_pessoais", {})
        pseudo = info.get("nome_completo", "Pesquisador_XXX")
        id_pseudo = info.get("id_lattes", "ID_XXX")

        # Insere o documento principal (modelo agregado)
        base.pesquisadores.insert_one(doc)

        # Normaliza artigos para uma colecao propria (referencia por id)
        for art in doc.get("producao_bibliografica", {}).get("artigos_periodicos", []):
            base.artigos.insert_one({
                "pesquisador_id": id_pseudo,
                "pesquisador": pseudo,
                "titulo": art.get("titulo"),
                "ano": art.get("ano"),
                "revista": art.get("revista"),
                "issn": art.get("issn"),
                "doi": art.get("doi"),
                "qualis": art.get("qualis"),
            })

        # Normaliza orientacoes
        orientacoes = doc.get("orientacoes", {})
        for status in ("em_andamento", "concluidas"):
            grupo = orientacoes.get(status, {})
            for nivel, itens in grupo.items():
                if not isinstance(itens, list):
                    continue
                for item in itens:
                    base.orientacoes.insert_one({
                        "pesquisador_id": id_pseudo,
                        "pesquisador": pseudo,
                        "status": status,
                        "nivel": nivel,
                        "titulo": item.get("titulo"),
                        "ano_inicio": item.get("ano_inicio"),
                        "ano_conclusao": item.get("ano_conclusao"),
                        "tipo_trabalho": item.get("tipo_trabalho"),
                        "instituicao": item.get("instituicao"),
                    })

    print(f"[+] pesquisadores: {base.pesquisadores.count_documents({})}")
    print(f"[+] artigos:        {base.artigos.count_documents({})}")
    print(f"[+] orientacoes:    {base.orientacoes.count_documents({})}")


def cria_indices(base) -> None:
    """Cria indices para acelerar as consultas mais comuns."""
    base.pesquisadores.create_index("informacoes_pessoais.id_lattes",
                                    unique=True)
    base.artigos.create_index("pesquisador_id")
    base.artigos.create_index("ano")
    base.orientacoes.create_index([("pesquisador_id", 1), ("status", 1)])
    print("[+] Indices criados")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--entrada", type=Path, required=True,
                   help="Pasta com os JSONs anonimizados")
    p.add_argument("--uri", default="mongodb://localhost:27017",
                   help="URI de conexao do MongoDB")
    p.add_argument("--db", default="ppgep_lattes",
                   help="Nome da base de dados")
    args = p.parse_args()

    base = conecta(args.uri, args.db)
    carrega_documentos(args.entrada, base)
    cria_indices(base)
    print("[+] Carga concluida")


if __name__ == "__main__":
    main()
