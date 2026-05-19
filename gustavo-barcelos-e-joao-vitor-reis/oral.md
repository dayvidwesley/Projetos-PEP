# Prova oral N1 — Gustavo Barcelos e João Vitor Reis

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. O Quadro 2 cita MVC (Reenskaug, 1979) sem desenvolver. O que é o MVC, quais seus três componentes e como ele se diferencia da arquitetura em camadas (N-Tier)?
- O MVC é uma arquitetura que sistematiza um padrão para a organização do software utilizado.  Ele é criado para separar responsabilidades para uma aplicação que, nesse caso, se baseiam nos componentes (Model - que acessa e manipula as informações do banco de dados, View - que representa a interface visual utilizada pelo usuário para exibição de informações e Controller - que atua como intermediário recebendo e processando as ações para coordenar a comunicação entre os dados). O MVC separa interface, controle e dados dentro da aplicação. Já o N-Tier separa o sistema em camadas maiores, como apresentação, negócios e banco de dados.

2. O histórico dos bancos por décadas não aparece. Reconstruam (60 IMS, 70 Codd, 80–90 SQL, 2000 NoSQL, 2010+ polyglot) e justifiquem a coexistência dos cinco SGBDs que vocês discutem.
- O histórico da evolução dos bancos de dados é como uma resposta às mudanças tecnológicas e às novas necessidades das organizações ao longo do tempo., ou seja, ao longo dos anos a necessidade de cada época vai se alterando e com ele as ferramentas tecnológicas empregadas para solucionar os problemas do contexto em questão. Para isso, vale mencionar uma linha cronológica do desenvolvimento histórico do banco de Dados.

Iniciando durante a Década de 1960, houve o surgimento do MS (Information Management System), o qual foi desenvolvido pela IBM para o programa “Apollo,” o IMS, na ocasião, utilizava o modelo hierárquico, no qual os dados eram organizados em estruturas de árvore. Esse modelo oferecia alta performance para operações previsíveis, porém possuía baixa flexibilidade para consultas complexas e alterações estruturais. Após 10 anos, criou-se o Modelo Relacional de Codd, iniciado por Edgar F. Codd, no contexto, ele publicou o artigo que introduziu o modelo relacional, revolucionando a organização dos dados em tabelas relacionadas por chaves primárias e estrangeiras. O modelo relacional trouxe independência lógica dos dados, integridade referencial e simplificação das consultas.

Em seguida, nas décadas de 80 e 90 houve, de fato, a consolidação do SQL, na ocasião, a linguagem SQL tornou-se padrão de mercado e os SGBDs relacionais passaram a dominar sistemas corporativos. Surgiram soluções como Oracle, DB2, SQL Server, MySQL e PostgreSQL, amplamente utilizadas em ERPs, sistemas financeiros e aplicações industriais devido às propriedades ACID e à confiabilidade transacional. 
Nos anos 2000, houve mais uma revolução no mundo de dados, o surgimento do NoSQL, implulsionado pelo  crescimento da internet, Big Data e computação distribuída evidenciou limitações dos bancos relacionais para lidar com grandes volumes de dados não estruturados. A partir dele, surgiram então bancos NoSQL, como MongoDB, Redis e Cassandra, priorizando escalabilidade horizontal, flexibilidade de schema e alta disponibilidade.
 Consolidou-se, em 2010, o Polyglot Persistente, o qual quebrou paradigmas e introduziu a ideia de que nenhum banco de dados é ideal para todos os problemas. A estratégia polyglot persistence propõe utilizar múltiplos SGBDs simultaneamente, escolhendo cada tecnologia conforme o tipo de dado e o padrão de acesso requerido.

Tratando-se da coexistência dos cinco SGBDs discutidos no trabalho (MySQL, PostgreSQL, MongoDB, Redis e Cassandra) justifica-se justamente por essa evolução histórica e pela especialização funcional de cada tecnologia:, então, a partir de cada período histórico, a evolução do banco de dados lapidou-se e estruturou-se a partir da necessidade do contexto.

Na prática, o  MySQL é adequado para sistemas transacionais tradicionais, como estoque, ordens de produção e qualidade, devido à simplicidade e ampla adoção. O PostgreSQL, por outro lado, é utilizado quando há necessidade de consultas analíticas complexas, conformidade SQL avançada e suporte a dados geoespaciais. 

Além disso, o MongoDB atende cenários com dados semiestruturados e variáveis, como sensores IoT industriais. O Redis já é empregado para cache e processamento em tempo real, graças à sua baixíssima latência em memória. Por fim, o Cassandra é indicado para telemetria massiva e séries temporais distribuídas, suportando bilhões de registros com alta disponibilidade.

Assim, os cinco bancos coexistem porque cada um resolve um problema específico da arquitetura moderna de sistemas industriais, formando uma abordagem complementar em vez de concorrente.


3. O trabalho não trata agregação versus composição estrutural. Definam as duas, o teste que as separa e um exemplo de cada na fábrica de componentes automotivos que vocês usam.
-

4. O Quadro 3 define a 2FN como "remover dependências parciais". O que é dependência parcial e por que a 2FN só faz sentido com chave composta? Dê um exemplo concreto.
- 

5. Expandam ACID e BASE. Por que MongoDB, Redis e Cassandra não seguem ACID, e como o teorema CAP explica esse trade-off?
-
