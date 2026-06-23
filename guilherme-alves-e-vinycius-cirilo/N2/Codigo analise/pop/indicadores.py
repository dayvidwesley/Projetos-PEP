# -*- coding: utf-8 -*-
"""
indicadores.py — Etapa 4 do POP ("Analisar").

Transforma os DataFrames brutos (extração) em indicadores clássicos de
Engenharia de Produção: OEE e seus três fatores, FPY/refugo, MTBF/MTTR,
curva ABC, e MAPE da previsão de demanda.
"""
import numpy as np
import pandas as pd


# --------------------------------------------------------------------------- #
# OEE — Overall Equipment Effectiveness  (Nakajima, 1988)
# --------------------------------------------------------------------------- #
def calcular_oee(base):
    """Recebe a base agregada (por recurso x mês) e acrescenta os 3 fatores
    do OEE e o OEE total. Funciona em qualquer granularidade já agrupada."""
    df = base.copy()
    df["disponibilidade"] = df["tempo_operando_min"] / df["tempo_planejado_min"]
    df["performance"] = df["tempo_ideal_seg"] / (df["tempo_operando_min"] * 60.0)
    # Performance é limitada a 100% (ciclo real nunca melhor que o ideal).
    df["performance"] = df["performance"].clip(upper=1.0)
    df["qualidade"] = df["pecas_boas"] / df["pecas_total"]
    df["oee"] = df["disponibilidade"] * df["performance"] * df["qualidade"]
    return df


def _agrega_oee(base, chaves):
    """Reagrega a base por 'chaves' e recalcula o OEE sobre os somatórios."""
    soma = (base.groupby(chaves, as_index=False)
                .agg({"tempo_planejado_min": "sum",
                      "tempo_operando_min": "sum",
                      "tempo_parado_min": "sum",
                      "tempo_ideal_seg": "sum",
                      "pecas_total": "sum",
                      "pecas_boas": "sum",
                      "pecas_refugo": "sum"}))
    return calcular_oee(soma)


def oee_por_maquina(base):
    return _agrega_oee(base, ["recurso", "recurso_nome", "centro"]) \
        .sort_values("oee", ascending=False)


def oee_por_mes(base):
    return _agrega_oee(base, ["ano_mes"]).sort_values("ano_mes")


def oee_global(base):
    soma = base[["tempo_planejado_min", "tempo_operando_min", "tempo_parado_min",
                 "tempo_ideal_seg", "pecas_total", "pecas_boas",
                 "pecas_refugo"]].sum().to_frame().T
    return calcular_oee(soma).iloc[0]


# --------------------------------------------------------------------------- #
# Pareto — acrescenta percentual e percentual acumulado
# --------------------------------------------------------------------------- #
def adicionar_pareto(df, coluna_valor):
    df = df.sort_values(coluna_valor, ascending=False).reset_index(drop=True)
    total = df[coluna_valor].sum()
    df["pct"] = 100 * df[coluna_valor] / total
    df["pct_acumulado"] = df["pct"].cumsum()
    return df


# --------------------------------------------------------------------------- #
# Refugo / FPY (First Pass Yield)
# --------------------------------------------------------------------------- #
def indicadores_refugo(refugo_produto):
    df = refugo_produto.copy()
    df["taxa_refugo_pct"] = 100 * df["pecas_refugo"] / df["pecas_total"]
    df["fpy_pct"] = 100 * df["pecas_boas"] / df["pecas_total"]
    return df.sort_values("taxa_refugo_pct", ascending=False)


# --------------------------------------------------------------------------- #
# MTBF / MTTR  a partir das manutenções corretivas e do tempo operando
# --------------------------------------------------------------------------- #
def mtbf_mttr(base_oee_df, base_manut):
    # Tempo operando total por máquina (em horas).
    op = (base_oee_df.groupby("recurso", as_index=False)["tempo_operando_min"]
          .sum())
    op["horas_operando"] = op["tempo_operando_min"] / 60.0

    corr = base_manut[base_manut["tipo"] == "CORRETIVA"].copy()
    corr = corr.rename(columns={"maquina": "recurso",
                                "ordens": "falhas",
                                "tempo_total_min": "tempo_reparo_min"})
    df = op.merge(corr[["recurso", "falhas", "tempo_reparo_min"]],
                  on="recurso", how="left").fillna({"falhas": 0,
                                                     "tempo_reparo_min": 0})
    # MTBF = tempo operando / nº de falhas;  MTTR = tempo reparo / nº de falhas
    df["mtbf_h"] = np.where(df["falhas"] > 0,
                            df["horas_operando"] / df["falhas"], np.nan)
    df["mttr_h"] = np.where(df["falhas"] > 0,
                            (df["tempo_reparo_min"] / 60.0) / df["falhas"],
                            np.nan)
    df["disponibilidade_inerente_pct"] = 100 * df["mtbf_h"] / (
        df["mtbf_h"] + df["mttr_h"])
    return df[["recurso", "horas_operando", "falhas", "mtbf_h", "mttr_h",
               "disponibilidade_inerente_pct"]]


# --------------------------------------------------------------------------- #
# Curva ABC de faturamento
# --------------------------------------------------------------------------- #
def curva_abc(faturamento_produto):
    df = adicionar_pareto(faturamento_produto.copy(), "receita_liquida")
    def classe(p):
        if p <= 80:
            return "A"
        if p <= 95:
            return "B"
        return "C"
    df["classe_abc"] = df["pct_acumulado"].apply(classe)
    df["margem_pct"] = 100 * df["margem_contribuicao"] / df["receita_liquida"]
    return df


# --------------------------------------------------------------------------- #
# Acurácia da previsão de demanda — MAPE e viés
# --------------------------------------------------------------------------- #
def acuracia_previsao(previsao_vs_real):
    df = previsao_vs_real.copy()
    df = df[df["qtd_real"] > 0].copy()          # meses com venda efetiva
    df["erro_abs_pct"] = 100 * (df["qtd_prevista"] - df["qtd_real"]).abs() \
        / df["qtd_real"]
    # Por SKU
    por_sku = (df.groupby("sku", as_index=False)
                 .agg(mape_pct=("erro_abs_pct", "mean"),
                      qtd_prevista=("qtd_prevista", "sum"),
                      qtd_real=("qtd_real", "sum")))
    por_sku["vies_pct"] = 100 * (por_sku["qtd_prevista"] - por_sku["qtd_real"]) \
        / por_sku["qtd_real"]
    mape_global = df["erro_abs_pct"].mean()
    return por_sku.sort_values("mape_pct"), mape_global


# --------------------------------------------------------------------------- #
# Aderência ao plano-mestre
# --------------------------------------------------------------------------- #
def indicadores_aderencia(aderencia_plano):
    df = aderencia_plano.copy()
    por_sku = (df.groupby(["sku", "produto"], as_index=False)
                 .agg(qtd_plano=("qtd_plano_mestre", "sum"),
                      qtd_op=("qtd_ordens_producao", "sum")))
    por_sku["aderencia_pct"] = 100 * por_sku["qtd_op"] / por_sku["qtd_plano"]
    return por_sku.sort_values("aderencia_pct")


# --------------------------------------------------------------------------- #
# Aderência CRUZADA (ERP x MES) — produção real boa vs plano-mestre
#   Indicador "polyglot": qtd planejada vem do PostgreSQL/ERP (plano_mestre)
#   e a produção realizada (peças boas) vem do MongoDB/MES (apontamentos).
# --------------------------------------------------------------------------- #
def aderencia_producao_real(refugo_produto, aderencia_plano):
    plano = (aderencia_plano.groupby("sku", as_index=False)
             ["qtd_plano_mestre"].sum()
             .rename(columns={"qtd_plano_mestre": "qtd_planejada_erp"}))
    real = refugo_produto[["sku", "produto", "pecas_boas"]].rename(
        columns={"pecas_boas": "qtd_produzida_boa_mes"})
    df = real.merge(plano, on="sku", how="inner")
    df["aderencia_pct"] = 100 * df["qtd_produzida_boa_mes"] / df["qtd_planejada_erp"]
    return df.sort_values("aderencia_pct")
