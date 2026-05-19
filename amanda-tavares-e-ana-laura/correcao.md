# Correção N1 — Amanda Tavares e Ana Laura
Data: 16/05/2026
Trabalho: Procedimento Operacional Padrão para Extração e Análise de Indicadores Comerciais e de Estoque via Salesforce CRM — Estudo de Caso em Unidade de Concessionária Premium

## Observação inicial

O cabeçalho lista meu nome (Dayvid W. P. Martins) como coautor junto com vocês duas. Eu não sou autor do trabalho de vocês. Isso precisa ser corrigido na próxima versão do artigo, antes da N2. Provavelmente é resquício do template ENEGEP que circulou pré-preenchido.

Também notei que a pasta tem dois PDFs (`N1 PEP.pdf` e `POP ENEGEP - PRÁTICAS.pdf`) com o mesmo conteúdo. Manter só um.

## Fundamentação teórica (peso 30%)

Esse foi o ponto mais forte do trabalho. Os três blocos pedidos (SIG, arquitetura e banco de dados) aparecem com boa profundidade e o que mais me agradou é que cada conceito vem amarrado ao caso real, não como teoria descolada.

Em 2.1, vocês explicam o ciclo dado→informação→conhecimento com um exemplo do próprio caso: "68 veículos novos vendidos" como dado, "volume de março 100% superior ao orçado" como informação, "revisar projeção de compra para o segundo trimestre" como conhecimento orientando decisão. Isso é exatamente o nível de concretude que a rubrica espera. Os níveis operacional, tático e estratégico de SI também aparecem bem situados.

Em 2.2, o histórico do banco de dados está presente (anos 60 com IMS, 70 com Codd, 2000 com NoSQL, 2010 com polyglot persistence). Aproveitar essa última nuance para dizer que o próprio Salesforce internamente combina relacional para transacional com estruturas flexíveis para metadados foi um bom fechamento.

Em 2.6, a articulação entre arquitetura em camadas, Salesforce como camada de dados e o argumento de Martin sobre BD como detalhe está coerente e sustenta a tese central de que o POP é robusto à mudança da forma de acesso (CSV hoje, API SOQL amanhã).

Um deslize a corrigir: na seção 2.4, a ilustração da 2FN ("todos os atributos dependem exclusivamente do chassi") não é didaticamente adequada. Em tabela com chave simples a 2FN é atendida por construção, ela só ganha sentido quando há chave composta e dependência parcial. Vale reformular usando um caso com chave composta no Salesforce, por exemplo uma tabela associativa entre veículo e campanha.

Pontos fortes: histórico de BD presente, exemplos do próprio caso na maioria dos conceitos, ciclo dado→decisão concretizado, articulação real entre os três blocos.

Nota do critério: 9,0.

## Qualidade da revisão bibliográfica (peso 20%)

Bibliografia variada e adequada. Vocês citam Codd em 1970 (referência primária do modelo relacional, não através de Elmasri ou Date), Davenport e Prusak para a definição de conhecimento, Fowler e Sadalage para NoSQL, Martin para Clean Architecture, Laudon para SIG, Salesforce como documentação oficial, O'Brien/Marakas e Stair/Reynolds como apoio. Citações em ABNT consistentes.

Senti falta de pelo menos uma referência clássica de banco de dados (Elmasri e Navathe ou Silberschatz/Korth/Sudarshan) para ancorar a parte de modelagem e normalização. Tem como incluir na revisão da N2 sem reescrever a seção.

Nota do critério: 9,0.

## Normalização e modelagem de dados (peso 20%)

Vocês aplicaram normalização e relacionamentos ao próprio cenário do Salesforce, o que é exatamente o que a rubrica pede. As 1FN/2FN/3FN aparecem com exemplos do caso (chassi como identificador, marca depende da montadora e não do modelo), e a ressalva sobre a 2FN já está feita acima. Os relacionamentos 1:N (unidade/oportunidades, veículo/histórico) e N:M (veículo/campanha) estão bem identificados.

Dois ajustes a fazer:

A passagem em 2.5 que diz "as linhas de faturamento e margem são composições das linhas de volume" mistura composição estrutural (modelagem ER, parte/todo onde o filho não existe sem o pai) com composição aritmética (faturamento = volume × preço). São coisas diferentes. O exemplo melhor para composição no contexto seria Ordem de Venda e seus Itens, ou Campanha e suas Regras, onde a parte realmente não existe sem o todo.

E falta o diagrama do modelo de dados — diagrama ER ou de classes representando as entidades do Salesforce que vocês discutem (Unidade, Oportunidade, Veículo, Histórico de Preços, Campanha). Sem isso, a seção fica em texto puro. Esse diagrama vai ser exigido na N2, então adianta começar.

Nota do critério: 8,0.

## Procedimento de conexão documentado (peso 15%)

A seção 3.2 define um POP em seis etapas (obtenção, validação, tratamento com pandas, cálculo de indicadores, visualização, registro no GitHub), o Quadro 3 descreve a estrutura dos dois arquivos e o Quadro 4 lista os indicadores com fórmula de cálculo. O conjunto é reprodutível e está coerente com a realidade da concessionária.

Vale observar que o procedimento, na forma proposta, não é uma conexão direta ao banco no sentido estrito que o roteiro do trabalho pede (string de conexão, ferramenta gráfica tipo pgAdmin, código psycopg2). É uma conexão intermediada: vocês acessam o Salesforce, extraem CSV e tratam com pandas. Isso é defensável dada a restrição de acesso por perfil (gestor x colaborador) e até casa com o argumento da Clean Architecture, mas para fechar o critério com nota cheia faltam dois detalhes: trecho de código `pandas.read_csv` exemplificando a leitura e, idealmente, uma menção à alternativa via simple_salesforce ou SOQL como evolução do procedimento para a N2.

Nota do critério: 8,0.

## Formatação ENEGEP/SBPO (peso 15%)

Template oficial, cabeçalho, resumo, palavras-chave, seções numeradas, quadros numerados (1 a 4) e citados no texto, referências em ABNT. A forma está bem cuidada.

Dois pontos a corrigir:

- O cabeçalho com meu nome como coautor, já comentado no início.
- O artigo encerra em "4. Considerações Finais" sem uma seção 4 dedicada a Resultados (mesmo que como planejamento) e uma seção 5 de Conclusão. O Quadro 4 cobre parte do papel de "resultados planejados", mas estruturalmente ficaria mais ENEGEP separar: 4. Resultados Esperados, 5. Considerações Finais.

Nota do critério: 8,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 9,0 | 30% | 2,70 |
| Revisão bibliográfica | 9,0 | 20% | 1,80 |
| Normalização e modelagem | 8,0 | 20% | 1,60 |
| Procedimento de conexão | 8,0 | 15% | 1,20 |
| Formatação ENEGEP/SBPO | 8,0 | 15% | 1,20 |
| **Total** | | | **8,5** |

## Para a N2

Quatro frentes a endereçar:

1. Corrigir o cabeçalho do artigo, removendo meu nome da autoria.
2. Construir o diagrama ER (ou de classes) das entidades do Salesforce que vocês citam — Unidade, Oportunidade, Veículo, Histórico de Preços, Campanha, com cardinalidades e marcando agregação vs composição no modelo.
3. Adensar o procedimento com código pandas mostrando a leitura dos dois CSVs, o cálculo de pelo menos dois indicadores do Quadro 4 e a geração de um gráfico.
4. Reformular o exemplo de composição (Ordem de Venda × Itens, por exemplo) e revisar a explicação da 2FN com chave composta.
