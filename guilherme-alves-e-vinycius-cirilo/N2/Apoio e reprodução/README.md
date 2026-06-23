# POP — Código da Etapa Prática (N2)

Procedimento Operacional Padrão para **extração e análise de dados** diretamente
em um SGBD relacional (PostgreSQL/ERP) e um SGBD documental (MongoDB/MES), no
contexto da Engenharia de Produção.

Autores: Guilherme Alves Mousinho · Vinycius Cirilo Machado Pêgo
Disciplina: Práticas em Engenharia de Produção — FCT/UFG (Prof. Dayvid W. P. Martins)

---

## Duas formas de rodar o POP

Há **dois caminhos equivalentes** (mesmos dados, mesmos indicadores):

| Caminho | Para quem | Arquivo |
|---|---|---|
| **A) Notebook didático** *(recomendado)* | quem quer **ler e seguir o passo a passo**, com explicação + código + resultado + gráfico na mesma tela | [`../POP.ipynb`](../POP.ipynb) |
| **B) Pacote modular** | quem quer rodar tudo de uma vez por linha de comando | `run_pop.py` + `pop/` |

## Estrutura

```
N2/
├── POP.ipynb             # (A) PROCEDIMENTO PASSO A PASSO — abrir e executar
├── codigo/
│   ├── pop/
│   │   ├── conexao.py        # Etapa 1 — conexão aos dois SGBDs (leitura)
│   │   ├── extracao_erp.py   # Etapa 3 — queries SQL (ERP/PostgreSQL)
│   │   ├── extracao_mes.py   # Etapa 3 — pipelines de agregação (MES/MongoDB)
│   │   ├── indicadores.py    # Etapa 4 — OEE, MTBF/MTTR, ABC, MAPE, refugo...
│   │   └── graficos.py       # Etapa 4 — figuras (matplotlib/seaborn)
│   ├── run_pop.py            # (B) Orquestrador: executa as 5 etapas
│   ├── construir_notebook.py # gera o POP.ipynb
│   ├── gerar_artigo.py       # gera o artigo .docx
│   ├── requirements.txt
│   └── .env.example
└── resultados/
    ├── tabelas/*.csv         # tabelas de indicadores (; decimal vírgula, UTF-8)
    ├── figuras/*.png         # gráficos
    └── indicadores_resumo.json
```

## Como reproduzir

```bash
# 1. Ambiente
python -m venv .venv
.venv\Scripts\activate           # Windows (PowerShell: .venv\Scripts\Activate.ps1)
pip install -r requirements.txt

# 2. Credenciais (recomendado via variáveis de ambiente)
#    Se não definidas, o código usa as credenciais didáticas da turma.
copy .env.example .env           # e edite com usuário/senha de leitura
```

**Caminho A — Notebook (passo a passo):** abra `POP.ipynb` no Jupyter/VS Code e
execute as células de cima para baixo (*Run All*). Cada etapa explica o que faz.

**Caminho B — linha de comando:**
```bash
python run_pop.py               # grava tabelas e figuras em ../resultados/
```

## Indicadores gerados

| Fonte | Indicador | Conceito teórico aplicado (N1) |
|---|---|---|
| MES (Mongo) | OEE e fatores D×P×Q por máquina e por mês | agregação `$group`; composição (array `paradas`) |
| MES (Mongo) | Pareto das paradas (Seis Grandes Perdas) | `$unwind` em documento embutido |
| MES (Mongo) | Refugo / FPY por produto | agregação documental |
| MES (Mongo) | MTBF / MTTR e disponibilidade inerente | manutenções corretivas |
| MES (Mongo) | Pareto de tipos de defeito | inspeções de qualidade |
| ERP (SQL)   | Curva ABC de faturamento e margem | JOIN + GROUP BY (relação N:M) |
| ERP (SQL)   | MAPE da previsão de demanda | CTE + LEFT JOIN |
| ERP + MES   | Aderência da produção real ao plano-mestre | indicador *cross-database* (polyglot persistence) |

## Governança e LGPD

* O usuário de banco utilizado é de **leitura** (SELECT / find).
* As credenciais não são fixadas no código (variáveis de ambiente).
* O dataset é didático e não contém dados pessoais — em conformidade com a LGPD.
