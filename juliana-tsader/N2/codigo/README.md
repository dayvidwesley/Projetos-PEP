# Codigo - POP de extracao e analise de dados via MongoDB

Implementacao da parte pratica do trabalho de Praticas em Engenharia
de Producao (UFG, 2026/1). O dataset utilizado e a saida do
scriptLattes para o corpo docente do PPGEP/UFG.

## Estrutura

| Arquivo | Funcao |
|---|---|
| `01_anonimizar.py` | Substitui nomes e id_lattes por pseudonimos (LGPD) |
| `02_carregar_mongodb.py` | Insere documentos anonimizados em uma colecao MongoDB |
| `03_analisar.py` | Executa pipelines de agregacao e gera figuras/tabelas |
| `requirements.txt` | Dependencias Python |

## Pre-requisitos

* Python 3.10+
* Instancia local do MongoDB (`mongod`) na porta 27017,
  OU URI valida de um cluster Atlas
* `pip install -r requirements.txt`

## Uso

```bash
# 1. Anonimiza (LGPD - obrigatorio antes de qualquer compartilhamento)
python 01_anonimizar.py \
    --entrada ../scriptLattes-main/PPGEP/arquivos/json \
    --saida ../dados/anonimizados

# 2. Carrega no MongoDB
python 02_carregar_mongodb.py \
    --entrada ../dados/anonimizados \
    --uri mongodb://localhost:27017 \
    --db ppgep_lattes

# 3. Gera indicadores e figuras
python 03_analisar.py \
    --entrada ../dados/anonimizados \
    --saida-tabelas ../tabelas \
    --saida-figuras ../figuras
```

## Sobre a anonimizacao

O script `01_anonimizar.py` produz dois artefatos:

1. JSONs anonimizados na pasta de saida -- seguros para commit
2. Arquivo `mapa_anonimizacao.csv` na pasta-pai da saida -- contem o
   mapeamento pseudonimo -> nome original. **Esse arquivo NAO deve ser
   commitado.** Adicione-o ao `.gitignore`.

## Observacoes sobre o modelo

A colecao `pesquisadores` mantem o documento agregado (composicao do
modelo conceitual). Em paralelo, as colecoes `artigos` e `orientacoes`
guardam referencias ao pesquisador (`pesquisador_id`) para demonstrar
o padrao de agregacao em NoSQL.
