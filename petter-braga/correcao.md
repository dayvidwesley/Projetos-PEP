# Correção N1 — Petter de Oliveira Braga Attux
Data: 17/05/2026
Trabalho: Sistemas de Informação Gerencial e Bancos de Dados: Fundamentação Teórica e POP para Acesso e Extração de Dados com PostgreSQL e MongoDB

## Fundamentação teórica (peso 30%)

O conteúdo é forte e bem encadeado. O SIG está bem tratado: componentes (Laudon e Laudon, O'Brien), a dimensão sociotécnica com o exemplo do MES subutilizado por falta de treinamento, o ciclo dado/informação/conhecimento com um exemplo concreto e bom (temperatura 82°C → forno acima de 75°C → reduzir gás em 10%) e o Quadro 1 com ERP/MES/WMS/BI/SCADA.

O bloco de bancos é o ponto alto. O histórico está detalhado e com datas (hierárquico e IMS de 1966, CODASYL de 1969, o artigo seminal de Codd em 1970, System R, Oracle e DB2, padronização do SQL em 1987, MySQL e PostgreSQL nos anos 90, NoSQL nos 2000 com os 3 Vs, Cassandra/MongoDB/Redis). O Quadro 2 classifica o NoSQL nos quatro tipos com casos de uso, o teorema CAP aparece, e você ainda traz NewSQL e o Quadro 3 comparando os paradigmas. Isso vai além do mínimo.

O elo mais fraco é a arquitetura de software. Você cobre bem a arquitetura em camadas (n-tier) e posiciona o banco como camada de dados/alicerce do SIG, mas não trata o MVC nem a Clean Architecture/arquitetura hexagonal, que estão na rubrica e na Aula-04. Some um parágrafo de cada, com Martin para a arquitetura limpa, e esse bloco fica no mesmo nível dos outros dois.

Nota do critério: 8,5.

## Qualidade da revisão bibliográfica (peso 20%)

Boa variedade: livros-texto canônicos (Date, Elmasri e Navathe, Laudon e Laudon, O'Brien, Oliveira, Pressman e Maxim, Sommerville, Stair e Reynolds, Sadalage e Fowler), um artigo de periódico com volume, número e páginas (Stonebraker e Cattell, *Communications of the ACM*) e a documentação oficial do PostgreSQL. Citações em ABNT corretas e articuladas no corpo do texto. Faltou alguma norma técnica e mais artigos acadêmicos para diversificar, mas o conjunto está bem selecionado.

Nota do critério: 8,5.

## Normalização e modelagem de dados (peso 20%)

Aqui está um acerto importante: as três formas normais estão definidas e, principalmente, bem exemplificadas, sem a confusão recorrente entre 2FN e 3FN. A 2FN com a chave composta (id_pedido, id_produto) e o nome do produto dependendo só de id_produto, e a 3FN com cidade/estado dependendo da cidade e não da PK cliente, mostram que o conceito está dominado. Relacionamentos 1:1, 1:N, N:M com tabela associativa e atributos de junção, e agregação versus composição, todos corretos e com exemplos de produção.

O que segura o critério é a ausência de um modelo próprio diagramado. Os exemplos são ilustrativos, espalhados, e não há um diagrama ER ou de classes consolidando um cenário. A teoria está sólida; falta transformá-la num modelo desenhado. Para a N2 o diagrama do modelo real é obrigatório.

Nota do critério: 7,5.

## Procedimento de conexão documentado (peso 15%)

O procedimento gráfico está concreto e reprodutível. Para o PostgreSQL via pgAdmin 4 você descreve desde o registro do servidor até as abas General e Connection, com a porta 5432 e o Query Tool. Para o MongoDB via Compass, o formato da string `mongodb://usuario:senha@host:porta/nome_do_banco`, o Connect e a aba Aggregations. Alguém consegue seguir esses passos.

Faltam duas coisas para fechar o critério: o esboço do código Python (psycopg2 e pymongo, que a rubrica pede) e as queries planejadas, ou seja, o que você pretende extrair na N2. Para N1 o procedimento gráfico já é um bom começo; deixe registrado o que será cobrado na parte prática.

Nota do critério: 7,5.

## Formatação ENEGEP/SBPO (peso 15%)

Esse é o desconto principal. O trabalho não usa o template oficial ENEGEP/SBPO: está num formato de artigo genérico, sem o cabeçalho do evento, com seções em caixa-alta numeradas e o resumo embutido no parágrafo. A organização interna é boa (quadros numerados com fonte, ABNT correta), mas a estrutura não segue a ordem exigida: não há seção de Metodologia rotulada (a seção 6 faz as vezes), não há Resultados nem uma Conclusão/Considerações Finais, mesmo como planejamento. O conteúdo está lá, é uma questão de migrar para o template ENEGEP e fechar com Metodologia, Resultados Esperados e Conclusão.

Nota do critério: 6,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 8,5 | 30% | 2,55 |
| Revisão bibliográfica | 8,5 | 20% | 1,70 |
| Normalização e modelagem | 7,5 | 20% | 1,50 |
| Procedimento de conexão | 7,5 | 15% | 1,125 |
| Formatação ENEGEP/SBPO | 6,0 | 15% | 0,90 |
| **Total** | | | **7,8** |

## Para a N2

1. Migrar o texto para o template oficial ENEGEP/SBPO, com a estrutura na ordem (Resumo, Introdução, Fundamentação, Metodologia, Resultados, Conclusão, Referências).
2. Completar a arquitetura de software com MVC e Clean Architecture (Martin), no mesmo nível dos blocos de SIG e bancos.
3. Desenhar o diagrama do modelo de dados real e aplicar as formas normais sobre ele.
4. Acrescentar o código Python de conexão (psycopg2/pymongo) e as queries que serão executadas na parte prática.

## Prova oral

Nota: 8,0

Quatro respostas corretas (o ciclo do dado ao conhecimento, a escolha do relacional, a 2FN frente à 3FN e o banco no Model do MVC). Na última, sobre implementar composição e agregação em PostgreSQL e MongoDB, faltou fechar a resposta.

# Correção N2 — Petter de Oliveira Braga Attux
Data: 27/06/2026
Trabalho: Acesso, Extração e Análise de Dados em Sistema ERP com PostgreSQL: Execução do Procedimento Operacional Padrão sobre Banco de Dados Real

A N2 é enxuta (sete páginas) mas faz o ciclo inteiro de forma honesta: conecta ao ERP fornecido, extrai com quatro queries pertinentes, deriva indicadores gerenciais com números e fecha o ciclo dado→decisão de maneira explícita. Resolveu a principal lacuna de formatação da N1, com Resultados e Conclusão preenchidos.

## Conexão e extração de dados (peso 25%)

A conexão ao banco erp está documentada com os parâmetros no Quadro 1 (host, porta 5432, banco, usuário) e o passo a passo no DBeaver (seção 2.3), reprodutível por quem tem acesso. As ressalvas: não há print da tela conectada nem código Python, a conexão e a extração foram feitas só pelo Editor SQL do DBeaver, e a etapa "Explorar" do POP ficou em prosa, sem o diagrama do modelo de dados real que cobrei na N1. O MongoDB, que aparecia na N1, saiu da prática (você assumiu o PostgreSQL, o que é uma escolha legítima, mas a comparação prática não acontece).

Nota do critério: 7,0.

## Qualidade das queries e análises (peso 25%)

As quatro consultas são pertinentes e bem construídas. A de ranking de produção usa JOIN com produto e agregação; a de produção × vendas usa SUM(CASE WHEN ...) para pivotar produzido contra vendido, que é uma boa técnica; a de saldo de estoque é a mais elaborada, com duplo JOIN (produto e tipo_movimento) e três agregações condicionais por natureza. Todas respondem perguntas reais de EP (capacidade, absorção pelo mercado, sazonalidade, ruptura). Não há query trivial demais nem errada. O teto do critério fica em não usar subquery, CTE ou window function, recursos que apareceriam naturalmente em análises mais profundas. Um detalhe a conferir: a coluna "Diferença" do Quadro 7 não é produzida pela query mostrada.

Nota do critério: 7,5.

## Indicadores gerados e interpretação (peso 20%)

Os indicadores gerenciais da seção 5 estão com números e bem amarrados: concentração da produção (cerca de 51% em dois produtos), taxa de absorção pelo mercado por item, sazonalidade de cerca de 18% e risco de ruptura no Booster Duplo. E a seção 6 fecha o ciclo dado→informação→conhecimento→decisão de forma explícita e numérica, com decisões concretas (priorizar capacidade nos dois itens de maior volume, atenção à reposição do Booster Duplo). O que falta para subir é forma: os indicadores estão só em quadros, sem nenhum gráfico, e a etapa "Analisar" pede tabelas e gráficos.

Nota do critério: 7,5.

## Código documentado e reprodutível (peso 15%)

As queries têm comentário de cabeçalho e estão legíveis nos quadros. Mas não há código Python, requirements ou README, e a reprodução depende de reescrever as consultas no DBeaver com as credenciais do Quadro 1. Sem nenhum artefato versionado na pasta além do PDF. Para um trabalho que defende a autonomia analítica do engenheiro, um script que conecta e roda as quatro queries fecharia bem o argumento.

Nota do critério: 6,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Conexão e extração de dados | 7,0 | 25% | 1,75 |
| Qualidade das queries e análises | 7,5 | 25% | 1,875 |
| Indicadores gerados e interpretação | 7,5 | 20% | 1,50 |
| Código documentado e reprodutível | 6,5 | 15% | 0,975 |
| **Soma ponderada (85%)** | | | **6,10** |

A N2 não terá prova oral. A nota final, renormalizando os quatro critérios (85% da rubrica) para a escala de 0 a 10, é **7,2**. Com o ponto extra atribuído na N2, a nota final fica **8,2**.

Trabalho correto e bem fechado, mas curto. Faltou um gráfico de pelo menos um indicador (a curva de concentração da produção, por exemplo) e o diagrama do modelo de dados que extraiu.
