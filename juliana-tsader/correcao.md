# Correção N1 — Juliana Tsader
Data: 19/05/2026
Trabalho: POP para Acesso, Extração e Análise de Dados sobre Currículos Lattes do PPGEP/UFG

## Observação inicial

O trabalho foi muito além do escopo da N1. Você não só fechou a fundamentação e o planejamento, como executou o procedimento sobre 26 currículos reais e produziu cinco indicadores bibliométricos com gráficos, anonimização LGPD e código versionado. Isso é, na prática, o que se cobra na N2. Para a N2 propriamente dita, basta consolidar essa execução (acrescentar Qualis e fator de impacto, como você mesma sugere no trabalho futuro) e cuidar dos pontos de formato apontados abaixo.

Sobre a organização da pasta: os arquivos ficaram em `juliana-tsader/POP Práticas.pdf` e `.docx`, e há um arquivo solto `juliana-tsader/N1` (sem extensão, vazio). O padrão da disciplina é `<aluno>/N1/<arquivo>.pdf`. Reorganize para a N2.

## Fundamentação teórica (peso 30%)

Três blocos cobertos com profundidade e bem articulados. No SIG, Laudon e Laudon (2020) e o ciclo dado → informação → conhecimento → decisão estão tratados com clareza, com o banco posicionado como camada onde o ciclo nasce e Schwab (2016) para a Indústria 4.0. Em arquitetura, Fowler (2003) para o padrão em camadas e Martin (2017) para a Clean Architecture/hexagonal, com o banco como detalhe que pode ser substituído, materializado na Figura 1 com a camada de infraestrutura destacada. O bloco de bancos traz o histórico completo do IMS dos anos 60 a Codd (1970, com fonte primária), SQL nos 80–90, NoSQL nos 2000 e polyglot persistence (Sadalage e Fowler, 2012). A Tabela 1 comparando relacional × documental por unidade, esquema, relacionamentos, transações (ACID × BASE), escala e exemplo em EP é o tipo de síntese que a rubrica espera.

Lacunas pontuais: o MVC não aparece (a Aula-04 trata) e a governança de TI (audit trail, COBIT) ficou de fora. Para a N2, incluir esses dois pontos eleva a fundamentação ao máximo.

Nota do critério: 9,0.

## Qualidade da revisão bibliográfica (peso 20%)

Bibliografia bem selecionada e variada: livros-texto (Date, Laudon e Laudon, Martin, Fowler, Sadalage e Fowler), papers acadêmicos com volume/número/páginas (Codd 1970 na *Communications of the ACM*, Mena-Chalco e Cesar-Junior 2009 com DOI, Newman 2004 na PNAS) e Schwab para o pano de fundo da Indústria 4.0. Citações em ABNT consistentes e articuladas no texto. O uso de Newman como base teórica para a análise de rede de coautoria é um diferencial.

Nota do critério: 9,0.

## Normalização e modelagem de dados (peso 20%)

Esse é o ponto mais alto do trabalho. As três formas normais estão definidas corretamente (1FN com valor atômico, 2FN eliminando dependências parciais da chave primária e 3FN eliminando dependências transitivas entre atributos não-chave), sem o erro recorrente de trocar 2FN por 3FN. Relacionamentos 1:1, 1:N e N:M com tabela associativa estão certos. A distinção agregação × composição vem com tradução em SQL (FK+JOIN para agregação, FK+`ON DELETE CASCADE` para composição) e em MongoDB (referência por `ObjectId` para agregação, documentos embutidos para composição) — exatamente como a Aula-05 cobra.

E, no melhor, a Figura 2 é o modelo conceitual do próprio cenário: Pesquisador como entidade central, com `formacao_academica`, `atuacao_profissional` e `orientacoes` em composição (embutidas no documento) e `Artigo`, `Banca` e `Projeto_pesquisa` em agregação N:M (coleções referenciadas). O desenho aplica a teoria diretamente ao caso.

Nota do critério: 9,5.

## Procedimento de conexão documentado (peso 15%)

As cinco etapas estão claras (anonimização, conexão, carga, pipelines, interpretação), o ambiente está caracterizado (Python 3.10, pymongo, MongoDB 7.0 em `localhost:27017`, pandas, matplotlib, Compass para inspeção visual) e o código está versionado no GitHub da turma. A anonimização prévia, com mapa determinístico em CSV separado fora do repositório público, é uma boa prática de LGPD bem implementada — vai além do que a maioria entrega. Cada indicador foi implementado em pipeline MongoDB e em pandas em paralelo, garantindo execução mesmo sem o servidor. Reprodutibilidade alta.

Nota do critério: 9,5.

## Formatação ENEGEP/SBPO (peso 15%)

Template ENEGEP correto, seções na ordem (Introdução, Fundamentação, Metodologia, Resultados, Conclusão, Referências), tabelas e figuras numeradas com fonte, ABNT correta. Discussão consistente fechando o ciclo. Conclusão com aprendizados e trabalho futuro.

Desconto principal: a primeira página não traz título do artigo, autoria, afiliação, resumo nem palavras-chave — o texto começa direto em "1. Introdução". O template ENEGEP/SBPO exige todos esses elementos no rosto do artigo. Isso precisa entrar antes da N2.

Nota do critério: 7,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 9,0 | 30% | 2,70 |
| Revisão bibliográfica | 9,0 | 20% | 1,80 |
| Normalização e modelagem | 9,5 | 20% | 1,90 |
| Procedimento de conexão | 9,5 | 15% | 1,425 |
| Formatação ENEGEP/SBPO | 7,5 | 15% | 1,125 |
| **Total** | | | **9,0** |

## Para a N2

1. Acrescentar título, autoria, afiliação, resumo e palavras-chave na primeira página, no template ENEGEP/SBPO.
2. Reorganizar a pasta no padrão `juliana-tsader/N1/...` (apagar o arquivo solto `N1` sem extensão e mover os PDFs/docx para a subpasta).
3. Incluir o MVC na fundamentação de arquitetura e um parágrafo de governança de TI/audit trail.
4. Consolidar os indicadores com estrato Qualis e fator de impacto, conforme você mesma propôs no trabalho futuro, e fechar com a comparação documental × relacional anunciada.
