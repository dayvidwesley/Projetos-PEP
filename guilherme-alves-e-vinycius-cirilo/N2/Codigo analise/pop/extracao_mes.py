# -*- coding: utf-8 -*-
"""
extracao_mes.py — Etapa 3 do POP ("Extrair") no SGBD documental MongoDB/MES.

Cada função encapsula um *pipeline de agregação* (o análogo documental do
GROUP BY relacional) e devolve um pandas.DataFrame. Exercita os conceitos da
N1: estágios $match, $unwind, $group, $project, $sort e o uso de documentos
embutidos (o array "paradas" dentro de cada apontamento — uma composição).
"""
import pandas as pd


# --------------------------------------------------------------------------- #
# 3.F  Base de OEE — agregação dos apontamentos por máquina e por mês
#       Disponibilidade, Performance e Qualidade derivam destes somatórios.
# --------------------------------------------------------------------------- #
def base_oee(db):
    """Soma os tempos e contagens de peças por recurso e mês.

    OEE = Disponibilidade x Performance x Qualidade, onde:
      Disponibilidade = tempo_operando / tempo_planejado
      Performance     = (ciclo_ideal_seg * pecas_total) / (tempo_operando_min*60)
      Qualidade       = pecas_boas / pecas_total
    """
    pipeline = [
        {"$group": {
            "_id": {"recurso": "$recurso_codigo",
                    "recurso_nome": "$recurso_nome",
                    "centro": "$centro_trabalho",
                    "ano_mes": "$ano_mes"},
            "tempo_planejado_min": {"$sum": "$tempo_planejado_min"},
            "tempo_operando_min":  {"$sum": "$tempo_operando_min"},
            "tempo_parado_min":    {"$sum": "$tempo_parado_min"},
            "pecas_total":         {"$sum": "$pecas_total"},
            "pecas_boas":          {"$sum": "$pecas_boas"},
            "pecas_refugo":        {"$sum": "$pecas_refugo"},
            # tempo ideal de produção = ciclo ideal * peças produzidas
            "tempo_ideal_seg":     {"$sum": {"$multiply": ["$tempo_ciclo_ideal_seg",
                                                            "$pecas_total"]}},
            "apontamentos":        {"$sum": 1},
        }},
        {"$project": {
            "_id": 0,
            "recurso": "$_id.recurso",
            "recurso_nome": "$_id.recurso_nome",
            "centro": "$_id.centro",
            "ano_mes": "$_id.ano_mes",
            "tempo_planejado_min": 1, "tempo_operando_min": 1,
            "tempo_parado_min": 1, "pecas_total": 1, "pecas_boas": 1,
            "pecas_refugo": 1, "tempo_ideal_seg": 1, "apontamentos": 1,
        }},
        {"$sort": {"ano_mes": 1, "recurso": 1}},
    ]
    return pd.DataFrame(list(db.apontamentos_producao.aggregate(pipeline)))


# --------------------------------------------------------------------------- #
# 3.G  Pareto das paradas — "Seis Grandes Perdas"
#       $unwind no array embutido "paradas" (composição) + $group por motivo.
# --------------------------------------------------------------------------- #
def pareto_paradas(db):
    pipeline = [
        {"$unwind": "$paradas"},
        {"$group": {
            "_id": "$paradas.motivo",
            "tempo_total_min": {"$sum": "$paradas.duracao_min"},
            "ocorrencias": {"$sum": 1},
        }},
        {"$project": {"_id": 0, "motivo": "$_id",
                      "tempo_total_min": 1, "ocorrencias": 1}},
        {"$sort": {"tempo_total_min": -1}},
    ]
    return pd.DataFrame(list(db.apontamentos_producao.aggregate(pipeline)))


# --------------------------------------------------------------------------- #
# 3.H  Refugo / qualidade por produto
# --------------------------------------------------------------------------- #
def refugo_por_produto(db):
    pipeline = [
        {"$group": {
            "_id": {"sku": "$produto_sku", "nome": "$produto_nome"},
            "pecas_total":  {"$sum": "$pecas_total"},
            "pecas_boas":   {"$sum": "$pecas_boas"},
            "pecas_refugo": {"$sum": "$pecas_refugo"},
        }},
        {"$project": {"_id": 0, "sku": "$_id.sku", "produto": "$_id.nome",
                      "pecas_total": 1, "pecas_boas": 1, "pecas_refugo": 1}},
        {"$sort": {"pecas_refugo": -1}},
    ]
    return pd.DataFrame(list(db.apontamentos_producao.aggregate(pipeline)))


# --------------------------------------------------------------------------- #
# 3.I  Inspeções de qualidade — Pareto de tipos de defeito
# --------------------------------------------------------------------------- #
def pareto_defeitos(db):
    pipeline = [
        {"$group": {
            "_id": "$tipo_defeito",
            "defeitos": {"$sum": "$defeitos"},
            "amostras": {"$sum": "$tamanho_amostra"},
            "inspecoes": {"$sum": 1},
            "reprovadas": {"$sum": {"$cond": ["$aprovado", 0, 1]}},
        }},
        {"$project": {"_id": 0, "tipo_defeito": "$_id",
                      "defeitos": 1, "amostras": 1,
                      "inspecoes": 1, "reprovadas": 1}},
        {"$sort": {"defeitos": -1}},
    ]
    return pd.DataFrame(list(db.inspecoes_qualidade.aggregate(pipeline)))


# --------------------------------------------------------------------------- #
# 3.J  Manutenção — base para MTBF e MTTR (somente corretivas para MTBF)
# --------------------------------------------------------------------------- #
def base_manutencao(db):
    pipeline = [
        {"$group": {
            "_id": {"maquina": "$maquina_codigo", "tipo": "$tipo"},
            "ordens": {"$sum": 1},
            "tempo_total_min": {"$sum": "$duracao_min"},
            "custo_total": {"$sum": "$custo"},
        }},
        {"$project": {"_id": 0, "maquina": "$_id.maquina", "tipo": "$_id.tipo",
                      "ordens": 1, "tempo_total_min": 1, "custo_total": 1}},
        {"$sort": {"maquina": 1, "tipo": 1}},
    ]
    return pd.DataFrame(list(db.manutencoes.aggregate(pipeline)))


def extrair_tudo(db):
    """Executa todos os pipelines e devolve um dicionário de DataFrames."""
    return {
        "base_oee": base_oee(db),
        "pareto_paradas": pareto_paradas(db),
        "refugo_produto": refugo_por_produto(db),
        "pareto_defeitos": pareto_defeitos(db),
        "base_manutencao": base_manutencao(db),
    }
