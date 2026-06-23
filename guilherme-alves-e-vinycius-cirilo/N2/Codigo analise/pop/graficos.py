# -*- coding: utf-8 -*-
"""
graficos.py — Geração das figuras (Etapa 4 do POP, evidências visuais).

Cada função salva um PNG em resultados/figuras/. Usa matplotlib/seaborn.
"""
import os
import matplotlib
matplotlib.use("Agg")           # backend não-interativo (execução em lote)
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams["figure.dpi"] = 130
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["axes.titleweight"] = "bold"

META_OEE = 0.85   # meta de classe mundial (referência Nakajima)


def _salvar(fig, dir_fig, nome):
    caminho = os.path.join(dir_fig, nome)
    fig.savefig(caminho)
    plt.close(fig)
    print(f"[fig] {nome}")
    return caminho


def fig_oee_maquina(oee_maq, dir_fig):
    fig, ax = plt.subplots(figsize=(8, 4.2))
    cores = ["#2a9d8f" if v >= META_OEE else
             ("#e9c46a" if v >= 0.60 else "#e76f51") for v in oee_maq["oee"]]
    ax.bar(oee_maq["recurso_nome"], oee_maq["oee"] * 100, color=cores)
    ax.axhline(META_OEE * 100, ls="--", color="gray",
               label=f"Meta classe mundial ({META_OEE*100:.0f}%)")
    ax.set_ylabel("OEE (%)")
    ax.set_title("OEE por máquina — 2025")
    ax.set_ylim(0, 100)
    for i, v in enumerate(oee_maq["oee"] * 100):
        ax.text(i, v + 1.5, f"{v:.1f}%", ha="center", fontsize=9)
    ax.legend()
    plt.xticks(rotation=15)
    return _salvar(fig, dir_fig, "fig1_oee_maquina.png")


def fig_oee_componentes(oee_maq, dir_fig):
    fig, ax = plt.subplots(figsize=(8, 4.2))
    x = range(len(oee_maq))
    w = 0.25
    ax.bar([i - w for i in x], oee_maq["disponibilidade"] * 100, w,
           label="Disponibilidade", color="#264653")
    ax.bar(list(x), oee_maq["performance"] * 100, w,
           label="Performance", color="#2a9d8f")
    ax.bar([i + w for i in x], oee_maq["qualidade"] * 100, w,
           label="Qualidade", color="#e9c46a")
    ax.set_xticks(list(x))
    ax.set_xticklabels(oee_maq["recurso_nome"], rotation=15)
    ax.set_ylabel("(%)")
    ax.set_ylim(0, 105)
    ax.set_title("Fatores do OEE por máquina — Disponibilidade x Performance x Qualidade")
    ax.legend()
    return _salvar(fig, dir_fig, "fig2_oee_componentes.png")


def fig_oee_mensal(oee_mes, dir_fig):
    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.plot(oee_mes["ano_mes"], oee_mes["oee"] * 100, marker="o",
            color="#264653", label="OEE")
    ax.plot(oee_mes["ano_mes"], oee_mes["disponibilidade"] * 100, marker="s",
            ls="--", alpha=.6, label="Disponibilidade")
    ax.plot(oee_mes["ano_mes"], oee_mes["performance"] * 100, marker="^",
            ls="--", alpha=.6, label="Performance")
    ax.plot(oee_mes["ano_mes"], oee_mes["qualidade"] * 100, marker="d",
            ls="--", alpha=.6, label="Qualidade")
    ax.axhline(META_OEE * 100, ls=":", color="gray")
    ax.set_ylabel("(%)")
    ax.set_title("Evolução mensal do OEE e seus fatores — 2025")
    ax.set_ylim(0, 105)
    ax.legend(ncol=2, fontsize=8)
    plt.xticks(rotation=45)
    return _salvar(fig, dir_fig, "fig3_oee_mensal.png")


def fig_pareto_paradas(par, dir_fig):
    fig, ax1 = plt.subplots(figsize=(9, 4.5))
    horas = par["tempo_total_min"] / 60.0
    ax1.bar(par["motivo"], horas, color="#e76f51")
    ax1.set_ylabel("Horas paradas")
    ax1.set_title("Pareto das paradas de produção — Seis Grandes Perdas")
    plt.setp(ax1.get_xticklabels(), rotation=30, ha="right", fontsize=8)
    ax2 = ax1.twinx()
    ax2.plot(par["motivo"], par["pct_acumulado"], color="#264653",
             marker="o")
    ax2.axhline(80, ls="--", color="gray")
    ax2.set_ylabel("% acumulado")
    ax2.set_ylim(0, 105)
    return _salvar(fig, dir_fig, "fig4_pareto_paradas.png")


def fig_refugo_produto(ref, dir_fig):
    fig, ax = plt.subplots(figsize=(8.5, 4.2))
    d = ref.sort_values("taxa_refugo_pct", ascending=True)
    ax.barh(d["sku"], d["taxa_refugo_pct"], color="#e76f51")
    ax.set_xlabel("Taxa de refugo (%)")
    ax.set_title("Taxa de refugo por produto — 2025")
    for i, v in enumerate(d["taxa_refugo_pct"]):
        ax.text(v + 0.02, i, f"{v:.2f}%", va="center", fontsize=8)
    return _salvar(fig, dir_fig, "fig5_refugo_produto.png")


def fig_abc(abc, dir_fig):
    fig, ax1 = plt.subplots(figsize=(9, 4.5))
    cores = {"A": "#2a9d8f", "B": "#e9c46a", "C": "#e76f51"}
    ax1.bar(abc["sku"], abc["receita_liquida"] / 1000,
            color=[cores[c] for c in abc["classe_abc"]])
    ax1.set_ylabel("Receita líquida (R$ mil)")
    ax1.set_title("Curva ABC de faturamento por produto — 2025")
    ax2 = ax1.twinx()
    ax2.plot(abc["sku"], abc["pct_acumulado"], color="#264653", marker="o")
    ax2.axhline(80, ls="--", color="gray")
    ax2.axhline(95, ls=":", color="gray")
    ax2.set_ylabel("% acumulado da receita")
    ax2.set_ylim(0, 105)
    handles = [plt.Rectangle((0, 0), 1, 1, color=cores[c]) for c in "ABC"]
    ax1.legend(handles, [f"Classe {c}" for c in "ABC"], loc="center right")
    plt.setp(ax1.get_xticklabels(), rotation=20)
    return _salvar(fig, dir_fig, "fig6_curva_abc.png")


def fig_previsao(prev_sku, dir_fig):
    fig, ax = plt.subplots(figsize=(8.5, 4.2))
    d = prev_sku.sort_values("mape_pct")
    ax.bar(d["sku"], d["mape_pct"], color="#264653")
    ax.set_ylabel("MAPE (%)")
    ax.set_title("Erro percentual médio absoluto (MAPE) da previsão de demanda")
    for i, v in enumerate(d["mape_pct"]):
        ax.text(i, v + 0.3, f"{v:.1f}%", ha="center", fontsize=8)
    plt.setp(ax.get_xticklabels(), rotation=20)
    return _salvar(fig, dir_fig, "fig7_mape_previsao.png")
