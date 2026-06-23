# -*- coding: utf-8 -*-
"""
conexao.py — Camada de conexão do POP (Procedimento Operacional Padrão).

Etapa 1 do POP: "Conectar".

Implementa a abertura de conexão aos dois SGBDs contemplados no trabalho:
  * PostgreSQL (ERP)  — paradigma relacional, via driver psycopg2 (SQLAlchemy).
  * MongoDB    (MES)  — paradigma documental, via driver pymongo.

Boas práticas de governança adotadas (cf. Seção 3.4 do artigo):
  * As credenciais NÃO são fixadas no código: são lidas de variáveis de
    ambiente. Caso ausentes, recai sobre os valores didáticos da turma
    apenas para garantir a reprodutibilidade do exercício acadêmico.
  * O usuário utilizado possui apenas permissão de leitura (SELECT / find).
"""
import os
from sqlalchemy import create_engine, text
from pymongo import MongoClient

# --------------------------------------------------------------------------- #
# Parâmetros de conexão (lidos do ambiente; fallback didático da turma)
# --------------------------------------------------------------------------- #
PG_URI = os.getenv(
    "PEP_PG_URI",
    "postgresql+psycopg2://erp:Fg669s8OGBgxTqL1C6gHv6FX7EJR"
    "@pep-postgresql.arch7.dev:5432/erp",
)
MONGO_URI = os.getenv(
    "PEP_MONGO_URI",
    "mongodb://mes:UT1EF3jReDHpf547q5P8BWivqLsx"
    "@pep-mongo.arch7.dev:27018/?authSource=admin",
)
PG_SCHEMA = "erp"
MONGO_DB = "mes"


def engine_postgres():
    """Cria uma engine SQLAlchemy (driver psycopg2) para o ERP PostgreSQL.

    Usa-se SQLAlchemy como camada fina sobre o psycopg2 para integração
    nativa e segura com o pandas.read_sql.
    """
    eng = create_engine(PG_URI, connect_args={"connect_timeout": 30})
    # Teste de conexão — deve retornar 19+ tabelas no schema 'erp'.
    with eng.connect() as c:
        n = c.execute(
            text(
                "SELECT count(*) FROM information_schema.tables "
                "WHERE table_schema = :s"
            ),
            {"s": PG_SCHEMA},
        ).scalar()
        print(f"[OK] PostgreSQL/ERP conectado — {n} tabelas no schema '{PG_SCHEMA}'.")
    return eng


def cliente_mongo():
    """Cria o MongoClient para o MES MongoDB e devolve (client, db)."""
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=30000)
    db = client[MONGO_DB]
    n = len(db.list_collection_names())
    print(f"[OK] MongoDB/MES conectado — {n} coleções no banco '{MONGO_DB}'.")
    return client, db


if __name__ == "__main__":
    # Teste rápido de conectividade (Etapa 1 do POP).
    eng = engine_postgres()
    client, db = cliente_mongo()
    client.close()
    eng.dispose()
    print("[OK] Teste de conexão concluído com sucesso.")
