# Correção N1 — Gabriel Costa e Luís Humberto
Data: 16/05/2026
Trabalho: Procedimento Operacional Padrão para Extração e Análise de Dados em Banco de Dados Aplicado à Engenharia de Produção

## Fundamentação teórica (peso 30%)

A revisão de literatura cobre uma boa variedade de sistemas industriais e modelos arquiteturais. A parte mais sólida do trabalho está em arquitetura de software: vocês descrevem MVC, arquitetura em camadas, Clean Architecture (Martin) e arquitetura hexagonal (Cockburn como referência primária), com vantagens e desvantagens de cada modelo, e fecham com um exemplo industrial de aplicação. A seção 2.2 sobre UML, citando Fowler, abre bem o caminho conceitual para modelagem.

A discussão sobre os sistemas industriais (ERP, MES, WMS, SCADA, CRM, BI) é abrangente e ajuda a situar o engenheiro de produção no ecossistema digital, embora cada subseção fique no nível de uma definição rápida sem aprofundamento conceitual.

Três lacunas significativas pesam contra:

- **Histórico do banco de dados ausente**. O roteiro do trabalho pede a evolução por décadas (anos 60 com arquivos sequenciais e modelo hierárquico, 70 com Codd e modelo relacional, 80–90 com SQL e RDBMS, 2000 com NoSQL, 2010+ com polyglot persistence). Vocês entram direto na sintaxe SQL (2.3) e mencionam NoSQL (2.4) sem o percurso histórico.
- **Ciclo dado → informação → conhecimento → decisão não aparece**. Esse ciclo é o eixo conceitual que justifica o acesso direto ao banco pelo engenheiro de produção, e está ausente do texto.
- **Codd não é citado**. O fundador do modelo relacional, que aparece em praticamente toda referência sobre BD, não está na bibliografia nem citado no texto.

O trabalho cobre amplitude (vários sistemas industriais) mas perde profundidade nos conceitos centrais da disciplina.

Nota do critério: 7,5.

## Qualidade da revisão bibliográfica (peso 20%)

Quatorze referências, com presença de clássicos no lugar certo: Date para BD, Elmasri e Navathe (citados ao final da 2.12 sobre drivers, mas sem entrada bibliográfica), Fowler para UML, Martin para Clean Architecture, Sadalage e Fowler para NoSQL, Slack/Chambers/Johnston para administração da produção, Sommerville e Pressman para engenharia de software, Cockburn como fonte primária da arquitetura hexagonal, Schwab para Indústria 4.0.

Pontos a corrigir:
- Codd não consta. Para um trabalho sobre banco de dados relacional, a omissão do "A Relational Model of Data for Large Shared Data Banks" (1970) é estranha.
- A referência GIL (2010) aparece na seção 2.11 mas não está na lista de referências. Citação fantasma.
- "Elmasri e Navathe" aparece como referência no parágrafo final da 2.12, sem ano e sem entrada bibliográfica completa.
- A entrada do Cockburn cita "Disponível em: Alistair Cockburn Official Website" sem URL explícita — ABNT exige link completo e data de acesso.

Nota do critério: 7,5.

## Normalização e modelagem de dados (peso 20%)

Esse é o ponto mais frágil do trabalho. A seção 2.11 limita-se a uma frase: "A modelagem envolve conceitos como normalização (1FN–3FN), relacionamentos (1:1, 1:N, N:M) e integridade dos dados". Não há definição do que é 1FN, 2FN ou 3FN, nem das diferenças entre elas, nem exemplos.

A discussão sobre relacionamentos aparece de passagem na seção 2.2 (sobre UML), com a menção de cardinalidades (1:1, 1:N, N:M), mas sem aplicação a um cenário específico.

Não há tratamento de agregação versus composição (mesmo o trabalho citando UML/Fowler na 2.2, esse par conceitual está fora do texto), nem diagrama ER ou de classes do cenário pretendido. O roteiro do trabalho lista esses dois pontos explicitamente como conteúdo esperado.

Para a N2, isso terá que ser reconstruído quase integralmente.

Nota do critério: 6,5.

## Procedimento de conexão documentado (peso 15%)

Esse foi o critério mais bem cuidado. A Tabela 1 (Drivers e Bancos) sintetiza o pareamento entre SGBD e biblioteca de conexão (PostgreSQL/psycopg2, MySQL/mysql-connector, MongoDB/pymongo, SQL Server/ODBC/pyodbc), o que dá um quadro claro do ferramental.

A Figura 1 traz o modelo de string de conexão do PostgreSQL com os cinco parâmetros essenciais (host, port, dbname, user, password). Isso é exatamente o tipo de elemento que torna o procedimento reprodutível.

A Figura 2 é o ponto alto do trabalho: o fluxograma "POP — Procedimento Padrão Operacional para Acesso ao Banco de Dados", com seis fases (Solicitação e Autorização, Preparação, Conexão, Extração e Uso dos Dados, Boas Práticas e Segurança incluindo LGPD, Encerramento) e responsáveis indicados (Engenheiro de Produção, TI/Governança, DBA). Esse fluxograma articula o procedimento numa visão sistêmica que sustenta a tese do trabalho. A inclusão do tema LGPD na fase 5 também é pertinente.

O que falta para fechar o critério com nota cheia: o trecho de código Python real executando a conexão (uma chamada `psycopg2.connect(...)` por exemplo) e um exemplo de query simples. Vocês descrevem o "como" em fluxograma, mas não mostram a execução. Esse adensamento será cobrado na N2.

Nota do critério: 8,5.

## Formatação ENEGEP/SBPO (peso 15%)

Template oficial, resumo e palavras-chave, seções numeradas, tabela e figuras numeradas com fonte indicada, referências em ABNT (com ressalvas já comentadas).

Pontos a ajustar:

- Numeração das seções: aparecem dois "2.10" (CRM e BI/Analytics) e dois "2.12" (Arquitetura de Software e Strings/Drivers). Renumerar.
- A seção 4 (Resultados) tem uma única linha: "A discussão teórica e prática gerou o mapa mental e fluxograma". Para ser uma seção de Resultados, mesmo em N1, precisa pelo menos uma página interpretando o que o fluxograma da Figura 2 entrega como contribuição.
- Não há seção 5 de Conclusão ou Considerações Finais.
- A redação tem alguns lapsos ("o seu sistema de informação gerencial funciona, como acontece a conexão") e uma palavra que escapou em 2.3 ("a sintaxe da linguagem ." com espaço antes do ponto). Revisão de português.
- Várias citações com nome no corpo do texto (ex.: "Slack, Chambers e Johnston (2009)", "Davenport (1998)") estão corretas; outras passagens fazem afirmações sem citação que deveriam vir referenciadas.

Nota do critério: 7,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 7,5 | 30% | 2,25 |
| Revisão bibliográfica | 7,5 | 20% | 1,50 |
| Normalização e modelagem | 6,5 | 20% | 1,30 |
| Procedimento de conexão | 8,5 | 15% | 1,275 |
| Formatação ENEGEP/SBPO | 7,0 | 15% | 1,05 |
| **Total** | | | **7,4** |

## Para a N2

Cinco frentes principais:

1. Incluir uma seção de histórico do banco de dados, cobrindo anos 60 (IMS, hierárquico), 70 (Codd, relacional), 80–90 (SQL, RDBMS comerciais), 2000 (NoSQL), 2010+ (polyglot persistence).
2. Desenvolver a seção de normalização: definir 1FN, 2FN e 3FN com exemplos do cenário industrial que vocês escolherem, e marcar agregação versus composição na modelagem.
3. Incluir o ciclo dado → informação → conhecimento → decisão como eixo da introdução ou em SIG, com exemplo concreto.
4. Construir o diagrama ER da base de dados que será usada na parte prática.
5. Adensar a Figura 2 (fluxograma) com o código Python correspondente à fase de Conexão (psycopg2.connect, cursor, SELECT) e à fase de Extração (cursor.fetchall + um pandas DataFrame).

## Prova oral

Nota: 9,5

Respondeu as cinco em texto completo: histórico dos bancos por década, as três formas normais com exemplo, agregação e composição, o ciclo do dado até a decisão e ACID frente a BASE, tudo bem desenvolvido.

# Correção N2 — Gabriel Costa e Luís Humberto
Data: 27/06/2026
Trabalho: Procedimento Operacional Padrão para Extração e Análise de Dados em Banco de Dados Aplicado à Engenharia de Produção

Vocês fecharam bem as frentes teóricas da N1: histórico dos bancos por década, formas normais com exemplo do próprio cenário, agregação e composição, o ciclo do dado, e as seções 4 e 5 agora preenchidas. A conexão aos dois bancos também está comprovada. O problema da N2 está na execução analítica, que ficou aquém do que o resto do trabalho prometia.

## Conexão e extração de dados (peso 25%)

A conexão é real e documentada nos dois ambientes, com prints próprios: DBeaver conectado ao schema erp mostrando as tabelas (Figura 4 e o PNG de acesso) e o Compass no banco mes com as seis coleções e a contagem de documentos. Os parâmetros de host, porta e banco estão no texto (p. 11-12). Isso comprova o acesso aos dois SGBDs. O que falta é a string/URI completa e, sobretudo, código: a conexão foi feita só por ferramenta gráfica, sem o psycopg2 que a N1 pediu e que o próprio Apêndice A.15 afirma ter incluído, mas que não aparece em nenhuma das 25 páginas.

Nota do critério: 8,0.

## Qualidade das queries e análises (peso 25%)

Aqui está a maior fragilidade. O artigo não mostra nenhuma query SQL nem nenhum pipeline do Mongo. A seção 4.1 diz genericamente que "foram realizadas consultas em SQL" e que o DBeaver permite exportar para CSV, mas não exibe o texto de nenhuma consulta. A extração que de fato aparece é a exportação bruta das tabelas e coleções: os seis CSVs mes.* e as abas do DRE_.xlsx são dumps, não resultados de query. Extrair não é exportar a tabela inteira, é perguntar ao banco. E os dados do MES, que são ricos (tempo de parada, peças boas, refugo, o array de paradas), foram exportados e não analisados, nenhum indicador de produção saiu deles.

Nota do critério: 5,0.

## Indicadores gerados e interpretação (peso 20%)

O único indicador gerado é a DRE de 2025 (p. 19-20), e ela está bem montada, cruzando lancamento_contabil, grupo_dre e conta_contabil até receita bruta, líquida e lucro. É uma consolidação contábil correta. Mas é só ela, não há gráfico, e a DRE aparece digitada no texto, sem a query ou a planilha que a produz (a xlsx só tem as tabelas-fonte, não a DRE calculada). O fechamento do ciclo fica conceitual: a discussão fala em complementaridade ERP/MES de forma teórica, sem uma decisão de Engenharia de Produção saindo de um indicador. Com os dados do MES na mão, dava para calcular disponibilidade, refugo e OEE e decidir sobre manutenção; isso ficou de fora. Ainda assim, a DRE é um indicador econômico-financeiro real e contabilmente correto, montado cruzando várias tabelas do ERP, e isso conta.

Nota do critério: 6,0.

## Código documentado e reprodutível (peso 15%)

Não há código no artigo. O Apêndice A.15 declara que foi incluído um trecho Python com psycopg2, cursor e DataFrame, mas ele não consta no texto, e o readme.md da pasta está vazio. A DRE não tem rastreabilidade (números no texto, sem a query). Some-se que o Apêndice A é um log de 20 itens narrando o que mudou e pedindo reconsideração de nota, o que é atípico num artigo ENEGEP; o lugar dessas explicações é a mensagem de entrega, não o corpo do artigo.

Nota do critério: 4,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Conexão e extração de dados | 8,0 | 25% | 2,00 |
| Qualidade das queries e análises | 5,0 | 25% | 1,25 |
| Indicadores gerados e interpretação | 6,0 | 20% | 1,20 |
| Código documentado e reprodutível | 4,5 | 15% | 0,675 |
| **Soma ponderada (85%)** | | | **5,125** |

A N2 não terá prova oral. A nota final, renormalizando os quatro critérios (85% da rubrica) para a escala de 0 a 10, é **6,0**. Com o ponto extra atribuído na N2, a nota final fica **7,0**.

A base do trabalho (conexão, modelo, DRE) é sólida; o que faltou foi transformar os dados extraídos do MES em consultas e indicadores. É lacuna que dá para fechar rápido: bastava ao menos uma query SQL e um pipeline do Mongo mostrando a extração e um indicador de produção saindo dos dados do MES.
