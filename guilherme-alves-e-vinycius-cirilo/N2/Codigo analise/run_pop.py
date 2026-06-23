# -*- coding: utf-8 -*-
"""
run_pop.py — Orquestrador do Procedimento Operacional Padrão (N2).

Executa, em sequência, as cinco etapas do POP descritas na N1:
  1. Conectar  -> pop.conexao
  2. Explorar  -> impressão do esquema (resumida)
  3. Extrair   -> pop.extracao_erp (SQL) + pop.extracao_mes (pipelines)
  4. Analisar  -> pop.indicadores + pop.graficos
  5. Interpretar -> consolidação das tabelas/figuras (a discussão vai no artigo)

Saídas:
  resultados/tabelas/*.csv   (todas as tabelas de indicadores)
  resultados/figuras/*.png   (todos os gráficos)
  resultados/indicadores_resumo.json (números-chave para o artigo)

Uso:
    python run_pop.py
"""
import os
import io
import sys
import json

# Garante saída UTF-8 mesmo no console Windows (cp1252).
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from pop import conexao, extracao_erp, extracao_mes, indicadores, graficos

# --------------------------------------------------------------------------- #
# Caminhos de saída
# --------------------------------------------------------------------------- #
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_TAB = os.path.join(BASE, "resultados", "tabelas")
DIR_FIG = os.path.join(BASE, "resultados", "figuras")
os.makedirs(DIR_TAB, exist_ok=True)
os.makedirs(DIR_FIG, exist_ok=True)


def salvar_tabela(df, nome):
    caminho = os.path.join(DIR_TAB, nome + ".csv")
    df.to_csv(caminho, index=False, encoding="utf-8-sig", sep=";",
              decimal=",", float_format="%.4f")
    print(f"[csv] {nome}.csv  ({len(df)} linhas)")


def secao(titulo):
    print("\n" + "=" * 72 + f"\n{titulo}\n" + "=" * 72)


def main():
    resumo = {}

    # ----- Etapa 1: Conectar ------------------------------------------------ #
    secao("ETAPA 1 — CONECTAR")
    engine = conexao.engine_postgres()
    client, db = conexao.cliente_mongo()

    # ----- Etapa 3: Extrair (ERP relacional) -------------------------------- #
    secao("ETAPA 3 — EXTRAIR (ERP / PostgreSQL — SQL)")
    erp = extracao_erp.extrair_tudo(engine)
    for k, v in erp.items():
        print(f"  - {k}: {len(v)} linhas")

    # ----- Etapa 3: Extrair (MES documental) -------------------------------- #
    secao("ETAPA 3 — EXTRAIR (MES / MongoDB — pipelines)")
    mes = extracao_mes.extrair_tudo(db)
    for k, v in mes.items():
        print(f"  - {k}: {len(v)} linhas")

    # ----- Etapa 4: Analisar — OEE ------------------------------------------ #
    secao("ETAPA 4 — ANALISAR (indicadores)")
    base = mes["base_oee"]
    oee_maq = indicadores.oee_por_maquina(base)
    oee_mes = indicadores.oee_por_mes(base)
    oee_g = indicadores.oee_global(base)
    salvar_tabela(indicadores.calcular_oee(base), "oee_recurso_mes")
    salvar_tabela(oee_maq, "oee_por_maquina")
    salvar_tabela(oee_mes, "oee_por_mes")
    print(f"\n  OEE GLOBAL = {oee_g['oee']*100:.1f}%  "
          f"(D={oee_g['disponibilidade']*100:.1f}% | "
          f"P={oee_g['performance']*100:.1f}% | "
          f"Q={oee_g['qualidade']*100:.1f}%)")
    resumo["oee_global"] = {
        "oee": round(float(oee_g["oee"]) * 100, 1),
        "disponibilidade": round(float(oee_g["disponibilidade"]) * 100, 1),
        "performance": round(float(oee_g["performance"]) * 100, 1),
        "qualidade": round(float(oee_g["qualidade"]) * 100, 1),
        "pecas_total": int(base["pecas_total"].sum()),
        "pecas_refugo": int(base["pecas_refugo"].sum()),
    }
    resumo["oee_por_maquina"] = oee_maq[
        ["recurso", "recurso_nome", "centro", "disponibilidade",
         "performance", "qualidade", "oee"]
    ].round(4).to_dict("records")

    # Pareto de paradas
    par = indicadores.adicionar_pareto(mes["pareto_paradas"], "tempo_total_min")
    salvar_tabela(par, "pareto_paradas")
    resumo["pareto_paradas"] = par.assign(
        horas=lambda d: (d["tempo_total_min"] / 60).round(1)
    )[["motivo", "horas", "ocorrencias", "pct", "pct_acumulado"]].round(1) \
        .to_dict("records")

    # Refugo / FPY
    ref = indicadores.indicadores_refugo(mes["refugo_produto"])
    salvar_tabela(ref, "refugo_por_produto")
    resumo["refugo"] = ref[["sku", "produto", "pecas_total",
                            "pecas_refugo", "taxa_refugo_pct", "fpy_pct"]] \
        .round(3).to_dict("records")

    # Pareto de defeitos
    defe = indicadores.adicionar_pareto(mes["pareto_defeitos"], "defeitos")
    salvar_tabela(defe, "pareto_defeitos")
    resumo["pareto_defeitos"] = defe.round(2).to_dict("records")

    # MTBF / MTTR
    mtb = indicadores.mtbf_mttr(base, mes["base_manutencao"])
    salvar_tabela(mtb, "mtbf_mttr")
    resumo["mtbf_mttr"] = mtb.round(2).to_dict("records")

    # Curva ABC
    abc = indicadores.curva_abc(erp["faturamento_produto"])
    salvar_tabela(abc, "curva_abc")
    resumo["curva_abc"] = abc[["sku", "produto", "receita_liquida",
                               "margem_contribuicao", "margem_pct", "pct",
                               "pct_acumulado", "classe_abc"]] \
        .round(2).to_dict("records")
    resumo["receita_total"] = round(float(abc["receita_liquida"].sum()), 2)

    # Acurácia da previsão
    prev_sku, mape_global = indicadores.acuracia_previsao(erp["previsao_vs_real"])
    salvar_tabela(prev_sku, "acuracia_previsao")
    print(f"  MAPE global da previsão = {mape_global:.1f}%")
    resumo["mape_global"] = round(float(mape_global), 1)
    resumo["acuracia_previsao"] = prev_sku.round(2).to_dict("records")

    # Aderência ao plano-mestre (ERP-only: ordens liberadas vs plano)
    ader = indicadores.indicadores_aderencia(erp["aderencia_plano"])
    salvar_tabela(ader, "aderencia_plano")
    resumo["aderencia_plano"] = ader.round(2).to_dict("records")

    # Aderência CRUZADA ERP x MES (produção real boa vs plano-mestre)
    ader_real = indicadores.aderencia_producao_real(
        mes["refugo_produto"], erp["aderencia_plano"])
    salvar_tabela(ader_real, "aderencia_producao_real")
    print("  Aderência produção real (MES) x plano (ERP) calculada "
          "para %d SKUs." % len(ader_real))
    resumo["aderencia_producao_real"] = ader_real.round(2).to_dict("records")

    # Faturamento mensal
    salvar_tabela(erp["faturamento_mensal"], "faturamento_mensal")

    # ----- Figuras ---------------------------------------------------------- #
    secao("ETAPA 4 — FIGURAS")
    graficos.fig_oee_maquina(oee_maq, DIR_FIG)
    graficos.fig_oee_componentes(oee_maq, DIR_FIG)
    graficos.fig_oee_mensal(oee_mes, DIR_FIG)
    graficos.fig_pareto_paradas(par, DIR_FIG)
    graficos.fig_refugo_produto(ref, DIR_FIG)
    graficos.fig_abc(abc, DIR_FIG)
    graficos.fig_previsao(prev_sku, DIR_FIG)

    # ----- Resumo JSON ------------------------------------------------------ #
    with open(os.path.join(BASE, "resultados", "indicadores_resumo.json"),
              "w", encoding="utf-8") as f:
        json.dump(resumo, f, ensure_ascii=False, indent=2)
    print("\n[OK] resultados/indicadores_resumo.json gravado.")

    client.close()
    engine.dispose()
    secao("POP CONCLUÍDO COM SUCESSO")


if __name__ == "__main__":
    main()
