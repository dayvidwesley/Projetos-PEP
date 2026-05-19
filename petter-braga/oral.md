# Prova oral N1 — Petter de Oliveira Braga Attux

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. Você usou o exemplo do forno (temperatura 82°C → acima de 75°C → reduzir gás em 10%) para o ciclo dado/informação/conhecimento. Onde entra a decisão e o que diferencia conhecimento de informação nesse caso?
No caso apresentado, o conhecimento e decisão entra na parte humana, ou seja quando vamos interpretar os dados e tomar uma decisão. O sistema apenas irá fornece-los, mas a parte da analise e aplicação é responsabilidade da pessoa.

2. No Quadro 3 você compara relacional, NoSQL e NewSQL. Para uma base de ordens de produção e estoque, qual paradigma você escolheria e qual critério do quadro pesa mais nessa escolha? 
Para uma base de ordens de produção e estoque, o melhor é usar o relacional, pois vamos trabalhar com dados padronizados, o que foge da tese do NoSQL de ter dados mais amplos e variados.

3. Você explicou bem a 2FN com a chave composta (id_pedido, id_produto). Por que guardar o nome do produto nessa tabela viola a 2FN, e como isso se diferencia de uma violação de 3FN?
No 2FN pela chave da tabela depender de dois "id's" e o nome estar vinculado apenas a um id, assim ficando apenas parcial. No 3FN já seria por que o campo iria depedender de outro campo que não é a chave.

4. A arquitetura no artigo está só em camadas. Onde o banco de dados se encaixa no padrão MVC, e o que muda quando o engenheiro acessa o banco direto em vez de pela interface? No caso o BD fica no Model, quando acessamos pelo pgadmin pulamos o Controler e o View e vamos direto ao Model

5. Você classificou itens de uma ordem de produção como composição e componentes de um produto como agregação. Qual é o teste que separa as duas, e como cada uma seria implementada no PostgreSQL e no MongoDB?
Para testarmos fazemos a seguinte pergunata: Faz sentido esses componente existir sozinho? Caso faça ele é caracterizado com Agregação, caso não faça ele é caracterizado como composição. Nao sei como seria implementado na interface de ambos ainda, não abordei isso nos estudos para a N1.
