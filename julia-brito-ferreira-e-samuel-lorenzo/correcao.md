# Correção N1 — Júlia Gabriela Brito Ferreira e Samuel Lorenzo Schirmbeck
Data: 17/05/2026
Trabalho: Procedimento Operacional Padrão para Acesso, Extração e Análise de Dados em Bancos de Dados Aplicados à Engenharia de Produção

## Observação inicial

O cabeçalho lista meu nome (Dayvid Wesley Pereira Martins) como primeiro autor, antes de vocês dois. Eu não sou autor do trabalho. Isso precisa ser corrigido na próxima versão, antes da N2 — autoria apenas da dupla.

## Fundamentação teórica (peso 30%)

Cobertura completa e bem articulada dos três blocos. SIG com a classificação completa TPS/SIG/DSS/EIS, complementada por ERP/MES/SCADA, pensamento sistêmico com Senge (1990) em fonte primária, e o ciclo dado→informação→conhecimento→decisão concretizado com exemplo de tempo de ciclo e linha de produção. Arquitetura tratada em camadas, MVC, Clean Architecture (Martin) e arquiteturas orientadas a serviços/microsserviços, com o banco posicionado corretamente como detalhe de infraestrutura desacoplada. Histórico do banco completo: anos 60 com IMS, Codd em 1970 (fonte primária), consolidação dos SGBDs nos anos 80-90, NoSQL nos 2000, polyglot persistence com Stonebraker, Çetintemel e Zdonik (2005) em fonte primária. A Tabela 1 (comparativo relacional × documental) está completa, incluindo ACID × BASE e escala vertical × horizontal.

Nota do critério: 9,5.

## Qualidade da revisão bibliográfica (peso 20%)

Bibliografia extensa (cerca de trinta entradas) e bem selecionada, com fontes primárias no lugar certo: Codd (1970), Chen (1976) para o modelo entidade-relacionamento, Booch/Rumbaugh/Jacobson para UML, Stonebraker et al. (2005), Senge (1990), além de papers recentes de manufatura inteligente (2022–2026) e a ISO 9001:2015 como referência normativa para o POP. Citações em ABNT consistentes. Critério muito bem atendido.

Nota do critério: 9,5.

## Normalização e modelagem de dados (peso 20%)

As três formas normais aparecem definidas corretamente, com relacionamentos 1:1, 1:N e N:M e regra de inserção de chave estrangeira por cardinalidade. Agregação e composição estão bem distinguidas, com a tradução em SQL via `ON DELETE CASCADE` para composição. A seção 2.5 (entidades, atributos, transformação) aplica os conceitos a um cenário produtivo próprio (máquinas, operadores, ordens_producao com FK), e a Tabela 2 mapeia entidades, tabelas e relacionamentos. A Figura 1 é um Diagrama de Classes UML próprio do cenário, com estereótipos «PK» e «FK» e multiplicidades — exatamente o tipo de modelagem que a rubrica espera.

Falta apenas o diagrama do dataset real, que será fornecido na N2.

Nota do critério: 9,0.

## Procedimento de conexão documentado (peso 15%)

O POP está estruturado em sete etapas com 26 passos numerados e resultados esperados por etapa. Há código `pymongo` real e bem documentado (conexão com `MongoClient`, listagem de coleções, inspeção de amostras) e pipelines de agregação MongoDB completos (`$match`, `$group`, `$sort`, `$lookup`, `$dateToString`) para volume por produto, temperatura média por máquina, paradas não planejadas e série histórica mensal. A Tabela 4 detalha as tecnologias para PostgreSQL e MongoDB. O cuidado com governança aparece (recomendação de variáveis de ambiente para credenciais).

Dois ajustes: os códigos são hipotéticos (adequado à N1, mas a execução real virá na N2), e há um leve descompasso entre o POP — todo detalhado em MongoDB — e a Tabela 4, que indica PostgreSQL como SGBD "de referência". Convém alinhar o discurso: ou o POP cobre os dois SGBDs em paralelo, ou assume o MongoDB como foco e justifica.

Nota do critério: 9,0.

## Formatação ENEGEP/SBPO (peso 15%)

Template ENEGEP oficial, resumo em itálico, palavras-chave, seções numeradas, tabelas e figuras numeradas com fonte, referências em ABNT. Bom nível formal.

Descontos: o nome do professor no cabeçalho (já comentado) e a ausência de uma seção de Conclusão/Considerações Finais claramente demarcada — o artigo encerra na descrição das etapas e tecnologias. Recomendo fechar com uma seção 4 de Resultados Esperados e uma seção 5 de Considerações Finais.

Nota do critério: 8,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 9,5 | 30% | 2,85 |
| Revisão bibliográfica | 9,5 | 20% | 1,90 |
| Normalização e modelagem | 9,0 | 20% | 1,80 |
| Procedimento de conexão | 9,0 | 15% | 1,35 |
| Formatação ENEGEP/SBPO | 8,0 | 15% | 1,20 |
| **Total** | | | **9,1** |

## Para a N2

1. Corrigir o cabeçalho, removendo meu nome da autoria.
2. Alinhar o POP e a Tabela 4: deixar explícito se o foco prático é PostgreSQL, MongoDB ou os dois em paralelo.
3. Executar os códigos e pipelines sobre o dataset fornecido, com diagrama do modelo real (ER no PostgreSQL e/ou de coleções no MongoDB) e prints da conexão.
4. Acrescentar seção 4 (Resultados) e seção 5 (Considerações Finais) para fechar o artigo no padrão ENEGEP.

## Prova oral

Nota: 10,0

As cinco com profundidade: o CASCADE expressando composição e por que não cabe em Fornecedor/Pedido, PostgreSQL frente a MongoDB com sensores heterogêneos, a polyglot persistence, o ciclo do tempo de ciclo até a decisão e a 2FN garantida na tabela ordens_producao.
