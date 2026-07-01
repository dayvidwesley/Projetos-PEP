# Correção N1 — Gustavo Barcelos e João Vitor Reis
Data: 17/05/2026
Trabalho: POP para Extração e Análise de Dados em Sistemas de Informação via Banco de Dados MySQL — no Contexto de Atuação do Engenheiro de Produção

## Fundamentação teórica (peso 30%)

A fundamentação tem boa amplitude e organização em três blocos. A introdução é bem articulada, com pergunta de pesquisa formulada e objetivos específicos enumerados (i, ii, iii, iv), o que é o padrão acadêmico correto. A citação à ABNT NBR ISO 9001:2015 para legitimar o POP como prática documentada é um cuidado normativo a favor.

A seção 2.1 traz o ciclo dado→informação→conhecimento com um exemplo concreto excelente no Quadro 1: "150 unidades em estoque" como dado, "Estoque abaixo do mínimo" como informação, "Necessidade de reposição imediata" como conhecimento. Esse nível de aplicação ao contexto industrial é exatamente o que dá força ao texto.

A seção 2.2 cobre arquitetura em camadas (Pressman/Maxim), hexagonal (Cockburn 2005 como referência primária) e Clean Architecture (Martin 2017), e o Quadro 2 sintetiza os padrões arquiteturais com origem, papel do BD e aplicação em Engenharia de Produção — esse cruzamento é útil.

A seção 2.3 cobre cinco SGBDs (MySQL, PostgreSQL, MongoDB, Redis, Cassandra) com profundidade, e a discussão de polyglot persistence em 2.3.10, junto com o Quadro 7 (exemplo de arquitetura polyglot em planta industrial), articula bem a tese central. O Quadro 5 (comparativo técnico MySQL × PostgreSQL) e o Quadro 6 (comparativo geral dos cinco SGBDs) são bem feitos.

Três pontos a corrigir:

- **O histórico do banco de dados por décadas não aparece**. O roteiro do trabalho pede a evolução em décadas (60 com IMS, 70 com Codd, 80-90 com SQL, 2000 com NoSQL, 2010+ com polyglot persistence). Vocês entram direto no modelo relacional (Codd 1970) sem o percurso histórico.

- **A seção 2.2 pula a sub-seção 2.2.2** (vai de 2.2.1 N-Tier direto para 2.2.3 Hexagonal). O Quadro 2 cita MVC com origem em Reenskaug 1979, mas o texto não traz a definição. MVC deveria ser desenvolvido em 2.2.2.

- **Agregação versus composição (modelagem UML, parte/todo) não são tratadas**. O roteiro do trabalho lista esse par como conteúdo esperado. Na seção 2.3.4, vocês usam "agregações" no sentido SQL (SUM, AVG, COUNT), o que é uma operação de consulta — distinta da agregação estrutural da modelagem.

Nota do critério: 8,5.

## Qualidade da revisão bibliográfica (peso 20%)

Esse é o critério com a falha mais grave do trabalho. A lista de referências contém apenas 7 entradas (Date, Elmasri e Navathe, Silberschatz/Korth/Sudarshan, Stair e Reynolds, MySQL, Fowler, MongoDB), mas o corpo do texto cita ao menos 15 autores adicionais que não constam nas referências:

- Schwab (2016) — citado na introdução
- Laudon e Laudon (2022) e (2020) — citado em dois anos diferentes, qual é o correto?
- Davenport e Harris (2007) — citado na introdução
- Slack, Brandon-Jones e Johnston (2018) — citado na introdução
- Correa e Correa (2017) — citado na introdução
- Codd (1970) — citado na introdução e na 2.3.1
- ABNT (2015) — citado na introdução (NBR ISO 9001)
- Pressman e Maxim (2020) — citado em 2.2.1
- Cockburn (2005) — citado em 2.2.3
- Martin (2017) — citado em 2.2.4
- Reenskaug (1979) — citado no Quadro 2
- PostgreSQL (2026), Redis (2026), Cassandra (2026) — citados nas respectivas seções
- Sadalage e Fowler (2012) — citado em 2.3.10

Toda citação no texto exige entrada correspondente nas referências. A omissão dessas entradas é desvio ABNT direto e desclassifica o critério em uma revisão acadêmica rigorosa. Para a N2 isso precisa ser inteiramente reconstruído.

Nota do critério: 6,5.

## Normalização e modelagem de dados (peso 20%)

O Quadro 3 (formas normais básicas) apresenta 1FN, 2FN e 3FN com "objetivo principal" e "problema evitado", mas em uma linha cada. Essa síntese não é suficiente como definição técnica. A 2FN, por exemplo, é descrita apenas como "Remover dependências parciais — Dados duplicados", sem explicar o que é uma dependência parcial nem o pré-requisito de chave composta. A 3FN aparece como "Eliminar dependências transitivas — Inconsistência de dados", também sem desenvolvimento.

O Quadro 4 traz os relacionamentos 1:1, 1:N e N:M com exemplos em Engenharia de Produção (Máquina/ficha técnica, Fornecedor/pedidos, Produtos/ordens de produção), o que está correto.

Não há diagrama ER próprio do contexto da fábrica de componentes automotivos que vocês usam como ilustrativo. E, como já comentado em fundamentação, agregação e composição UML não são tratadas.

Nota do critério: 7,0.

## Procedimento de conexão documentado (peso 15%)

A Figura 1 (fluxograma do POP) é um diferencial visual: o procedimento aparece desenhado com pontos de decisão concretos (dados disponíveis? Tipo de BD? Resultados coerentes? Resultados atendem aos objetivos?) e ciclos de refinamento. Esse desenho dá legibilidade ao procedimento.

As etapas são descritas em texto, com menção a comandos SQL (SELECT, WHERE, JOIN, GROUP BY), a comandos de inspeção de schema (SHOW TABLES, DESCRIBE) e a `mysql-connector-python` como driver.

O que falta para fechar com nota cheia: o trecho de código Python real fazendo a conexão (`mysql.connector.connect(host=, port=, user=, password=, database=)`, cursor, primeiro SELECT), a string de conexão exemplificada e idealmente uma captura de tela do MySQL Workbench ou DBeaver com a conexão estabelecida. Sem isso, o procedimento fica claro no fluxograma mas pendente no detalhe técnico de reprodução. Esse adensamento será cobrado na N2.

Nota do critério: 7,5.

## Formatação ENEGEP/SBPO (peso 15%)

Template ENEGEP oficial, cabeçalho do XLV ENEGEP, resumo em itálico, palavras-chave, quadros e figura numerados com fonte indicada, referências em formato ABNT.

Pontos graves a corrigir:

- **Erro de numeração na seção 2.2**: vai de 2.2.1 (N-Tier) direto para 2.2.3 (Hexagonal). Renumerar.
- **Erro de numeração grosso na seção final**: depois da seção 3 (Metodologia, com subseção 3.1), o trabalho vai direto para "8. CONSIDERAÇÕES FINAIS". Não há seções 4, 5, 6 ou 7 no artigo. As Considerações Finais deveriam ser a seção 4 (ou 5, se houvesse seção 4 de Resultados Esperados). Esse salto numerático é o tipo de detalhe que compromete a avaliação formal do artigo.
- "Elaborado pelo autor" no singular em várias fontes de quadros, embora a autoria seja em dupla.
- Falta seção dedicada a Resultados (mesmo que parciais, como planejamento da N2).

Nota do critério: 6,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 8,5 | 30% | 2,55 |
| Revisão bibliográfica | 6,5 | 20% | 1,30 |
| Normalização e modelagem | 7,0 | 20% | 1,40 |
| Procedimento de conexão | 7,5 | 15% | 1,125 |
| Formatação ENEGEP/SBPO | 6,5 | 15% | 0,975 |
| **Total** | | | **7,4** |

## Para a N2

Cinco frentes:

1. Reconstruir a lista de referências, incluindo todos os autores citados no texto (Schwab, Laudon, Davenport e Harris, Slack/Brandon-Jones/Johnston, Correa e Correa, Codd, ABNT, Pressman e Maxim, Cockburn, Martin, Reenskaug, PostgreSQL, Redis, Cassandra, Sadalage e Fowler).
2. Corrigir as numerações: completar a seção 2.2 com MVC (2.2.2) e renumerar a seção final ("8. Considerações Finais" para a numeração correta, idealmente seção 5 após uma nova seção 4 de Resultados Esperados).
3. Incluir uma seção de histórico do banco de dados por décadas e desenvolver agregação versus composição UML, com exemplos da fábrica de componentes automotivos que serve de contexto.
4. Desenvolver as definições das formas normais com terminologia técnica: dependência funcional, dependência parcial, dependência transitiva, com exemplos concretos no contexto industrial.
5. Adensar a Figura 1 com o código Python real (mysql-connector-python) que executa a conexão e uma query simples, mais a string de conexão exemplificada.

## Prova oral

Nota: 9,5

As cinco bem desenvolvidas: histórico dos bancos, justificativa de cada SGBD, agregação e composição, a 2FN com dependência parcial e ACID frente a BASE apoiado no teorema CAP.

# Correção N2 — Gustavo Barcelos e João Vitor Reis
Data: 27/06/2026
Trabalho: Análise de Banco de Dados ERP Industrial em PostgreSQL: Modelagem Relacional, Indicadores de PCP e Suporte à Tomada de Decisão Industrial

A N2 de vocês tem um conjunto de queries SQL de alto nível, e a cobertura analítica é ampla e bem fechada em decisão. Mas o trabalho repete a falha mais grave da N1 e deixa de cumprir a etapa "Conectar" do POP, o que segura a nota.

## Conexão e extração de dados (peso 25%)

A extração via SQL está sólida, com as oito consultas reproduzidas e parametrizadas por período. O problema é a etapa "Conectar": não há print de tela do DBeaver conectado nem código Python de conexão, nenhuma string, nenhum psycopg2. A N1 cobrou exatamente isso, e a metodologia da N2 cita DBeaver, mas a conexão estabelecida não é evidenciada. Some-se a troca de SGBD entre a N1 (MySQL) e a N2 (PostgreSQL) sem uma linha justificando a mudança em função do cenário. As queries rodam contra o banco, mas o "Conectar" do POP ficou em aberto.

Nota do critério: 6,5.

## Qualidade das queries e análises (peso 25%)

É o ponto alto. As consultas vão bem além do trivial: window function para percentual do total (Código 1), CTEs encadeadas na aderência do PCP (Código 9, a melhor) e SUM(...) OVER (ORDER BY ... DESC) para o percentual acumulado da curva ABC de produtos e de insumos (Códigos 15 e 17). Cada uma responde uma pergunta real de PCP, mix de vendas, Pareto de clientes, aderência do plano mestre, criticidade de insumos, resultado por centro de custo. Não há query frouxa nem errada. Vocês ainda tiveram a honestidade de mostrar e corrigir um bug do próprio código na seção 7.2 (o head(5) que pegava os de menor consumo). Domínio real de SQL.

Nota do critério: 9,0.

## Indicadores gerados e interpretação (peso 20%)

Oito indicadores, cada um com tabela e gráfico, e a interpretação aterrissa em decisão concreta: concentração de 52,38% das vendas em duas válvulas levando à discussão Make-to-Stock × Make-to-Order, Pareto de clientes (top 5 = 62,26%) puxando key account management, insumos críticos pedindo estoque de segurança e múltiplos fornecedores, aderência do plano mestre apontando revisão da previsão. A seção 9 consolida o ciclo dado→informação→conhecimento→decisão de forma explícita. Ressalva: alguns indicadores (giro de estoque, nível de serviço) ficam só qualitativos por falta de dado de estoque médio, e os dados dos gráficos foram digitados à mão no Python em vez de lidos do resultado da query (ver abaixo).

Nota do critério: 8,5.

## Código documentado e reprodutível (peso 15%)

As rotinas de gráfico em Python estão presentes e comentadas, mas com os dados hardcoded: os DataFrames têm os números digitados, em vez de um pd.read_sql trazendo o resultado da consulta. Isso quebra a reprodutibilidade ponta a ponta, o Python não está conectado ao banco, só replota valores já extraídos à mão. E pesa o que arrasto da N1: o artigo não tem seção de Referências, citando Codd e Pressman/Maxim no corpo sem nenhuma entrada na lista. Esse era o ponto mais grave da N1 e voltou. Sem requirements/README e com a numeração de figuras e códigos embaralhada nas seções 5 e 6.

Nota do critério: 6,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Conexão e extração de dados | 6,5 | 25% | 1,625 |
| Qualidade das queries e análises | 9,0 | 25% | 2,25 |
| Indicadores gerados e interpretação | 8,5 | 20% | 1,70 |
| Código documentado e reprodutível | 6,0 | 15% | 0,90 |
| **Soma ponderada (85%)** | | | **6,475** |

A N2 não terá prova oral. A nota final, renormalizando os quatro critérios (85% da rubrica) para a escala de 0 a 10, é **7,6**. Com o ponto extra atribuído na N2, a nota final fica **8,6**.

Um recado direto: a lista de referências ausente é o tipo de coisa que derruba um artigo num encontro de verdade. Vocês têm um trabalho técnico forte preso num problema que se resolvia numa página.
