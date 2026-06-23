# -*- coding: utf-8 -*-
"""
extracao_erp.py — Etapa 3 do POP ("Extrair") no SGBD relacional PostgreSQL/ERP.

Cada função encapsula uma consulta SQL e devolve um pandas.DataFrame.
As queries exercitam deliberadamente os conceitos teóricos da N1:
  * JOINs entre tabelas normalizadas (agregação 1:N / N:M);
  * funções de agregação (SUM, AVG, COUNT) com GROUP BY;
  * tabela associativa (item_pedido) materializando a relação N:M
    Pedido <-> Produto.
"""
import pandas as pd


# --------------------------------------------------------------------------- #
# 3.A  Faturamento por produto  (curva ABC / Pareto de receita)
# --------------------------------------------------------------------------- #
SQL_FATURAMENTO_PRODUTO = """
SELECT  p.sku,
        p.nome                                   AS produto,
        f.nome                                   AS familia,
        SUM(ip.quantidade)                       AS qtd_vendida,
        SUM(ip.quantidade * ip.preco_unitario
            * (1 - ip.desconto_pct/100.0))       AS receita_liquida,
        SUM(ip.quantidade * p.custo_padrao_unitario) AS custo_total,
        SUM(ip.quantidade * ip.preco_unitario
            * (1 - ip.desconto_pct/100.0))
          - SUM(ip.quantidade * p.custo_padrao_unitario) AS margem_contribuicao
FROM        erp.item_pedido  ip
JOIN        erp.pedido_venda pv ON pv.id = ip.pedido_id
JOIN        erp.produto      p  ON p.id  = ip.produto_id
JOIN        erp.familia_produto f ON f.id = p.familia_id
WHERE       pv.status = 'FATURADO'
GROUP BY    p.sku, p.nome, f.nome
ORDER BY    receita_liquida DESC;
"""


# --------------------------------------------------------------------------- #
# 3.B  Faturamento mensal  (sazonalidade da receita)
# --------------------------------------------------------------------------- #
SQL_FATURAMENTO_MENSAL = """
SELECT  to_char(pv.data_pedido, 'YYYY-MM')        AS ano_mes,
        SUM(ip.quantidade * ip.preco_unitario
            * (1 - ip.desconto_pct/100.0))         AS receita_liquida,
        COUNT(DISTINCT pv.id)                       AS pedidos
FROM        erp.item_pedido  ip
JOIN        erp.pedido_venda pv ON pv.id = ip.pedido_id
WHERE       pv.status = 'FATURADO'
GROUP BY    1
ORDER BY    1;
"""


# --------------------------------------------------------------------------- #
# 3.C  Aderência ao Plano-Mestre de Produção (PMP)
#       qtd produzida (ordem_producao) vs qtd planejada (plano_mestre)
# --------------------------------------------------------------------------- #
SQL_ADERENCIA_PLANO = """
SELECT  pm.ano_mes,
        p.sku,
        p.nome                          AS produto,
        SUM(pm.qtd_planejada)           AS qtd_plano_mestre,
        COALESCE(SUM(op.qtd_planejada),0) AS qtd_ordens_producao
FROM        erp.plano_mestre pm
JOIN        erp.produto p ON p.id = pm.produto_id
LEFT JOIN   erp.ordem_producao op
            ON op.produto_id = pm.produto_id AND op.ano_mes = pm.ano_mes
GROUP BY    pm.ano_mes, p.sku, p.nome
ORDER BY    pm.ano_mes, p.sku;
"""


# --------------------------------------------------------------------------- #
# 3.D  Acurácia da previsão de demanda
#       previsao_demanda vs vendas reais (item_pedido)
# --------------------------------------------------------------------------- #
SQL_PREVISAO_VS_REAL = """
WITH vendas AS (
    SELECT  ip.produto_id,
            to_char(pv.data_pedido, 'YYYY-MM') AS ano_mes,
            SUM(ip.quantidade)                 AS qtd_real
    FROM        erp.item_pedido  ip
    JOIN        erp.pedido_venda pv ON pv.id = ip.pedido_id
    WHERE       pv.status = 'FATURADO'
    GROUP BY    1, 2
)
SELECT  pd.ano_mes,
        p.sku,
        pd.qtd_prevista,
        COALESCE(v.qtd_real, 0) AS qtd_real
FROM        erp.previsao_demanda pd
JOIN        erp.produto p ON p.id = pd.produto_id
LEFT JOIN   vendas v ON v.produto_id = pd.produto_id AND v.ano_mes = pd.ano_mes
ORDER BY    pd.ano_mes, p.sku;
"""


# --------------------------------------------------------------------------- #
# 3.E  Curva de custo de insumos por fornecedor (relação N:M via item_compra)
# --------------------------------------------------------------------------- #
SQL_COMPRAS_FORNECEDOR = """
SELECT  fo.nome                                   AS fornecedor,
        COUNT(DISTINCT c.id)                       AS compras,
        SUM(ic.quantidade * ic.custo_unitario)     AS valor_comprado
FROM        erp.item_compra ic
JOIN        erp.compra     c  ON c.id  = ic.compra_id
JOIN        erp.fornecedor fo ON fo.id = c.fornecedor_id
WHERE       c.status = 'RECEBIDA' OR c.status = 'CONCLUIDA' OR c.status IS NOT NULL
GROUP BY    fo.nome
ORDER BY    valor_comprado DESC;
"""


def extrair_tudo(engine):
    """Executa todas as consultas e devolve um dicionário de DataFrames."""
    dfs = {
        "faturamento_produto": pd.read_sql(SQL_FATURAMENTO_PRODUTO, engine),
        "faturamento_mensal": pd.read_sql(SQL_FATURAMENTO_MENSAL, engine),
        "aderencia_plano": pd.read_sql(SQL_ADERENCIA_PLANO, engine),
        "previsao_vs_real": pd.read_sql(SQL_PREVISAO_VS_REAL, engine),
        "compras_fornecedor": pd.read_sql(SQL_COMPRAS_FORNECEDOR, engine),
    }
    return dfs
