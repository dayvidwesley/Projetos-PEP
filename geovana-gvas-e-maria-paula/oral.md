# Prova oral N1 — Geovana Gvas e Maria Eduarda

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. A seção 2.1 trata SIG e ERP como se fossem a mesma coisa. Diferenciem os dois conceitos e o nível decisório que cada um atende.
   O ERP é um sistema de gestão integrada de processos operacionais e transacionais, mas é utilizado principalmente a nível operacional, registrando transações do dia a dia. O SIG gera relatórios consolidados a nível tático e gerencial, podendo extrair dados do ERP e de outras fontes.

2. Vocês usam "agregação" e "composição" ora como funções SQL (SUM, JOIN), ora como relacionamento UML/ER. São a mesma coisa? Qual a definição correta em modelagem de dados?
 Não são a mesma coisa, em SQL funções de agregação são funções que agregam e resumem dados. Em UML/ER agregação é uma relação "todo-parte", em que paartes podem existir separadamente do todo, enquanto a composição representa uma relação mais forte, em que a parte depende do todo para existir.

3. As três formas normais são citadas sem definição. Definam 1FN, 2FN e 3FN com um exemplo de violação numa tabela de ordens de produção.
   A 1FN (primeira forma normal) exige que cad campo da tabela tenha apenas um valor. A violação disso seria uma ordem de produção com vários produtos armazenados no mesmo campo, como "produto A", "produto B". A 2FN exige que os atributos dependam da chave inteira e não apenas de parte dela, a violçaão seria quando uma tabela com chave "número da ordem + código do produto", o nome do produto depende apenas do código do produto. 3FN exige que não existam dependencias entre atributos não chave, a violação seria seria armazenar o nome do fornecedor e também da sua cidade na tabela de ordens, sendo que a cidade depende do fornecedor e não da ordem de produção.

4. A Fase 1 do POP descreve a conexão só em texto. Descrevam o código Python que conecta no PostgreSQL: string de conexão, `psycopg2.connect`, cursor com um SELECT e tratamento de erro
A onexão com postgreeSQL em python é realizada por meio da biblioteca psycopg2. Primeiro, define-se a string de conexão com parâmetros como host, porta, nome do banco, usuário e senha, em seguida utiliza-se psycopg2.connect() para estabelecer a conexão. Após conectar, cria-se um cursor para executar os comandos SQL, como um select para testar a comunicação com o banco. O tratamento de erro é feito com try/except, permitindo capturar falhas de autenticação, conexão ou execução de consultas sem interromper o programa.

5. Vocês citam polyglot persistence. Numa fábrica com ERP, MES e sensores IoT, que dados vão para o relacional e quais para um documental ou colunar? Justifiquem por estrutura, volume e velocidade.
   Em uma fábrica os dados do ERP e do MES, como ordens de produção, estoque, cadstro de produtos e fornecedores, devem ficar em bancos relacionais, pois possuem estrutura fixa, relacionamentos consistentes e necessidades de integridade transacional. Já os dados de sensores IoT, como temperatura, vibração e pressão em tempo real, saõ mais adequados para banco documentais ou colunares, pois apresentam grande volume e estrutura variável. Os bancos documentais oferecem flexibilidade para dados heterogeneos, enquanto os colunares suportam melhor altas taxas de escrita e processamento massivo em tempo real.
