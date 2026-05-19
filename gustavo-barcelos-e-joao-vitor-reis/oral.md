# Prova oral N1 — Gustavo Barcelos e João Vitor Reis

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. O Quadro 2 cita MVC (Reenskaug, 1979) sem desenvolver. O que é o MVC, quais seus três componentes e como ele se diferencia da arquitetura em camadas (N-Tier)?

O MVC é uma arquitetura que sistematiza um padrão para a organização do software utilizado.  Ele é criado para separar responsabilidades para uma aplicação que, nesse caso, se baseiam nos componentes (Model - que acessa e manipula as informações do banco de dados, View - que representa a interface visual utilizada pelo usuário para exibição de informações e Controller - que atua como intermediário recebendo e processando as ações para coordenar a comunicação entre os dados). O MVC separa interface, controle e dados dentro da aplicação. Já o N-Tier separa o sistema em camadas maiores, como apresentação, negócios e banco de dados.

2. O histórico dos bancos por décadas não aparece. Reconstruam (60 IMS, 70 Codd, 80–90 SQL, 2000 NoSQL, 2010+ polyglot) e justifiquem a coexistência dos cinco SGBDs que vocês discutem.
   
 O histórico da evolução dos bancos de dados é como uma resposta às mudanças tecnológicas e às novas necessidades das organizações ao longo do tempo., ou seja, ao longo dos anos a necessidade de cada época vai se alterando e com ele as ferramentas tecnológicas empregadas para solucionar os problemas do contexto em questão. Para isso, vale mencionar uma linha cronológica do desenvolvimento histórico do banco de Dados.

Iniciando durante a Década de 1960, houve o surgimento do MS (Information Management System), o qual foi desenvolvido pela IBM para o programa “Apollo,” o IMS, na ocasião, utilizava o modelo hierárquico, no qual os dados eram organizados em estruturas de árvore. Esse modelo oferecia alta performance para operações previsíveis, porém possuía baixa flexibilidade para consultas complexas e alterações estruturais. Após 10 anos, criou-se o Modelo Relacional de Codd, iniciado por Edgar F. Codd, no contexto, ele publicou o artigo que introduziu o modelo relacional, revolucionando a organização dos dados em tabelas relacionadas por chaves primárias e estrangeiras. O modelo relacional trouxe independência lógica dos dados, integridade referencial e simplificação das consultas.

Em seguida, nas décadas de 80 e 90 houve, de fato, a consolidação do SQL, na ocasião, a linguagem SQL tornou-se padrão de mercado e os SGBDs relacionais passaram a dominar sistemas corporativos. Surgiram soluções como Oracle, DB2, SQL Server, MySQL e PostgreSQL, amplamente utilizadas em ERPs, sistemas financeiros e aplicações industriais devido às propriedades ACID e à confiabilidade transacional. 
Nos anos 2000, houve mais uma revolução no mundo de dados, o surgimento do NoSQL, implulsionado pelo  crescimento da internet, Big Data e computação distribuída evidenciou limitações dos bancos relacionais para lidar com grandes volumes de dados não estruturados. A partir dele, surgiram então bancos NoSQL, como MongoDB, Redis e Cassandra, priorizando escalabilidade horizontal, flexibilidade de schema e alta disponibilidade.
 Consolidou-se, em 2010, o Polyglot Persistente, o qual quebrou paradigmas e introduziu a ideia de que nenhum banco de dados é ideal para todos os problemas. A estratégia polyglot persistence propõe utilizar múltiplos SGBDs simultaneamente, escolhendo cada tecnologia conforme o tipo de dado e o padrão de acesso requerido.

Tratando-se da coexistência dos cinco SGBDs discutidos no trabalho (MySQL, PostgreSQL, MongoDB, Redis e Cassandra) justifica-se justamente por essa evolução histórica e pela especialização funcional de cada tecnologia:, então, a partir de cada período histórico, a evolução do banco de dados lapidou-se e estruturou-se a partir da necessidade do contexto.

Na prática, o  MySQL é adequado para sistemas transacionais tradicionais, como estoque, ordens de produção e qualidade, devido à simplicidade e ampla adoção. O PostgreSQL, por outro lado, é utilizado quando há necessidade de consultas analíticas complexas, conformidade SQL avançada e suporte a dados geoespaciais. 

Além disso, o MongoDB atende cenários com dados semiestruturados e variáveis, como sensores IoT industriais. O Redis já é empregado para cache e processamento em tempo real, graças à sua baixíssima latência em memória. Por fim, o Cassandra é indicado para telemetria massiva e séries temporais distribuídas, suportando bilhões de registros com alta disponibilidade.

Assim, os cinco bancos coexistem porque cada um resolve um problema específico da arquitetura moderna de sistemas industriais, formando uma abordagem complementar em vez de concorrente.


3. O trabalho não trata agregação versus composição estrutural. Definam as duas, o teste que as separa e um exemplo de cada na fábrica de componentes automotivos que vocês usam.

Realizando um comparativo entre a agregação e a composição estrutural, infere-se que  “Composição” é uma relação que as partes não existem sem o todo. Se, por exemplo, o todo é destruído, as partes deixam de existir automaticamente. No banco de dados relacional, por outro lado, isso se implementa com a opção “Delete On Scade”, isto é, deletar o pai deleta automaticamente os filhos.  No MongoDB, os dados são embutidos dentro do documento pai.


A agregação é uma relação caracterizada pelas partes que existem de forma independente do todo. Se o todo é destruído, as partes continuam existindo. No banco relacional, a chave estrangeira existe mas sem “CASCADE” , visto que deletar o pai é bloqueado ou deixa o filho com referência nula. No MongoDB, usa-se referência por ObjectId.

Uma forma de separar-los é levantar o questionamento do que pode ocorrer se o pai for deletado, o que ocorrerá com os filhos. Caso os filhos fiquem desconexos, logo, é do tipo de composição, ou seja, os filhos dependem existencialmente do pai. Caso contrário, é agregação, os filhos existem independentemente.

4. O Quadro 3 define a 2FN como "remover dependências parciais". O que é dependência parcial e por que a 2FN só faz sentido com chave composta? Dê um exemplo concreto.

Nesse caso, dependência parcial significa que um atributo não-chave depende apenas de parte da chave composta. Então, como a chave primária possui apenas 1 atributo, não existe "parte" da chave, logo, a 2FN só faz sentido quando a chave primária é composta por dois ou mais campos.
Como exemplo, em um sistema de pedidos, uma tabela pode utilizar "Pedido ID + Produto ID" como chave composta para identificar cada item do pedido. Entretanto, o nome do produto depende apenas do "ProdutoID", independentemente do pedido em que ele aparece. Isso caracteriza uma dependência parcial, pois o atributo não depende da chave completa. A 2FN busca eliminar esse problema separando as informações em tabelas específicas, reduzindo redundância e inconsistências.

5. Expandam ACID e BASE. Por que MongoDB, Redis e Cassandra não seguem ACID, e como o teorema CAP explica esse trade-off?

Bancos relacionais (MySQL, PostgreSQL) seguem o modelo ACID, que garante alta integridade e confiabilidade nas transações. Entretanto, bancos NoSQL como MongoDB, Redis e Cassandra foram projetados para ambientes distribuídos e grandes volumes de dados, priorizando escalabilidade e disponibilidade. Nesses cenários, manter todas as garantias ACID pode reduzir desempenho e dificultar a distribuição entre múltiplos servidores, levando esses bancos a adotarem modelos mais flexíveis de consistência.

A razão pela qual MongoDB, Redis e Cassandra não seguem ACID em sua operação distribuída está fundamentada no Teorema CAP, formulado por Eric Brewer em 2000 e formalmente provado por Gilbert e Lynch em 2002. O teorema estabelece que qualquer sistema de dados distribuído pode garantir simultaneamente apenas duas das três seguintes propriedades: Consistência (C para qual todos os nós enxergam os mesmos dados ao mesmo tempo), Disponibilidade (A( Availability) no qual o sistema sempre responde a requisições) e Tolerância a partições (P, onde o sistema continua operando mesmo quando a comunicação entre nós é interrompida). A escolha de quais duas propriedades priorizar define o posicionamento de cada SGBD.
