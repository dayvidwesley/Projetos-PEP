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
