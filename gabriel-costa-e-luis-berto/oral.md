# Prova oral N1 — Gabriel Costa e Luís Humberto

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. O histórico dos bancos por décadas não aparece no texto. Reconstruam: anos 60 (IMS/hierárquico), 70 (relacional/Codd), 80–90 (SQL/RDBMS), 2000 (NoSQL), 2010+ (polyglot persistence).

2. A 2FN e a 3FN são citadas sem definição. Definam 1FN, 2FN e 3FN, com o pré-requisito de cada e um exemplo de violação numa tabela de produção.

3. Vocês citam Fowler e UML mas não tratam agregação versus composição. Definam as duas e o teste prático que as separa, com um exemplo industrial de cada.

4. O ciclo dado → informação → conhecimento → decisão não aparece no texto. Diferenciem os quatro estágios com um caso em que uma consulta SQL vira informação para a decisão.

5. O texto cita NoSQL mas não trata ACID nem BASE. O que cada sigla significa e por que um ERP precisa de ACID e não tolera bem o BASE?

# Prova Oral N1 — Banco de Dados em Engenharia de Produção
Disciplina: Práticas em Engenharia de Produção

Discentes:
- Gabriel Costa de Andrade Sodré
- Luís Humberto Franco de Carvalho

# 1. Evolução histórica dos bancos de dados por décadas

A evolução dos bancos de dados ocorreu de forma gradual, acompanhando as necessidades tecnológicas e industriais de cada período. Na década de 1960 surgiram os primeiros bancos de dados hierárquicos, sendo o principal exemplo o IMS (Information Management System), desenvolvido pela IBM. Nesse modelo, os dados eram organizados em estrutura de árvore, em que existiam registros “pais” e “filhos”. Apesar de eficiente para a época, o modelo apresentava grande rigidez estrutural, forte dependência física dos dados e dificuldade para realizar alterações ou expansões no sistema.

Na década de 1970 ocorreu uma grande transformação com o surgimento do modelo relacional proposto por Edgar F. Codd. Nesse novo paradigma, os dados passaram a ser organizados em tabelas relacionadas entre si por meio de chaves primárias e estrangeiras. Esse modelo trouxe maior flexibilidade, independência lógica, redução de redundâncias e melhor integridade dos dados. Além disso, foi nesse período que começaram os fundamentos da linguagem SQL. Durante as décadas de 1980 e 1990 houve a consolidação dos bancos relacionais e dos Sistemas Gerenciadores de Banco de Dados Relacionais (RDBMS), como Oracle, SQL Server, MySQL e PostgreSQL. O SQL tornou-se padrão universal para comunicação com bancos relacionais. Nessa fase, as empresas passaram a utilizar amplamente sistemas ERP integrados, exigindo confiabilidade, integridade e controle transacional através do modelo ACID.

A partir dos anos 2000, com o crescimento da internet, Big Data e aplicações distribuídas, surgiram os bancos NoSQL. Esses bancos foram desenvolvidos para suportar grandes volumes de dados não estruturados e aplicações com necessidade de alta escalabilidade. Diferentemente do modelo relacional, os bancos NoSQL trabalham com estruturas flexíveis, como documentos, grafos, chave-valor e famílias de colunas. Exemplos incluem MongoDB, Cassandra e Redis. A partir de 2010 consolidou-se o conceito de persistência poliglota. Nesse modelo, as organizações passaram a utilizar diferentes tipos de bancos simultaneamente, escolhendo cada tecnologia conforme a necessidade da aplicação. Um ERP pode utilizar PostgreSQL, enquanto sensores industriais podem armazenar dados em MongoDB e ferramentas analíticas podem utilizar Data Warehouses. Esse cenário está diretamente relacionado à Indústria 4.0 e à integração de sistemas industriais discutida no artigo.

# 2. Definição de 1FN, 2FN e 3FN

A normalização é um processo utilizado para organizar bancos de dados relacionais, reduzir redundâncias e evitar inconsistências. O artigo menciona a normalização entre 1FN e 3FN como parte fundamental da modelagem relacional.

A Primeira Forma Normal (1FN) estabelece que todos os atributos de uma tabela devem possuir valores atômicos, ou seja, uma célula não pode armazenar múltiplos valores simultaneamente. O principal objetivo é eliminar grupos repetitivos. Um exemplo de violação ocorre quando uma tabela de produção armazena vários operadores em uma única coluna, como “João, Carlos”. Nesse caso, o correto seria criar linhas separadas para cada operador.

A Segunda Forma Normal (2FN) exige que a tabela esteja anteriormente na 1FN e que todos os atributos não-chave dependam totalmente da chave primária. O problema surge quando existe dependência parcial em chaves compostas. Um exemplo ocorre em uma tabela de ordens de produção onde o nome do produto depende apenas do código do produto e não da chave composta inteira. A solução consiste em separar as informações em tabelas específicas, reduzindo redundâncias.

A Terceira Forma Normal (3FN) exige que a tabela esteja na 2FN e elimina dependências transitivas. Isso significa que atributos não-chave não podem depender de outros atributos não-chave. Um exemplo industrial ocorre quando uma tabela armazena funcionário, setor e gerente do setor simultaneamente. O gerente depende do setor, e não diretamente do funcionário. Nesse caso, o correto é criar uma tabela específica para setores e outra para funcionários. A aplicação correta da normalização é extremamente importante em ambientes industriais, pois reduz inconsistências, melhora a confiabilidade dos indicadores e garante maior integridade para sistemas ERP, BI e bancos relacionais utilizados na Engenharia de Produção.

# 3. Agregação versus composição na UML

O artigo aborda a UML como ferramenta de modelagem de dados e destaca sua importância na representação das entidades e relacionamentos do sistema. Contudo, não diferencia diretamente agregação e composição. A agregação representa um relacionamento fraco do tipo “todo-parte”. Nesse relacionamento, os objetos podem existir independentemente uns dos outros. Em UML, a agregação é representada por um losango branco. Um exemplo industrial é a relação entre empresa e funcionários. Mesmo que a empresa deixe de existir, os funcionários continuam existindo como entidades independentes.

Já a composição representa um relacionamento forte do tipo “todo-parte”, em que a existência da parte depende diretamente do objeto principal. Em UML, ela é representada por um losango preto. Um exemplo industrial é a relação entre ordem de produção e itens da ordem. Caso a ordem seja excluída, os itens associados deixam automaticamente de existir, pois dependem completamente daquela estrutura principal. O principal teste prático para diferenciar agregação e composição consiste em perguntar se a parte continua existindo sem o todo. Caso continue existindo, trata-se de agregação. Caso deixe de existir, trata-se de composição. Na Engenharia de Produção, compreender essa diferença é importante para garantir integridade referencial, rastreabilidade e organização correta das entidades dentro de sistemas ERP, MES e bancos relacionais industriais.

# 4. Ciclo dado → informação → conhecimento → decisão

O artigo enfatiza que o acesso direto ao banco de dados permite transformar dados brutos em informações relevantes para tomada de decisão. Porém, o ciclo completo dado → informação → conhecimento → decisão pode ser detalhado em quatro etapas. O dado representa um registro bruto, sem contexto ou interpretação. Por exemplo, afirmar que “a máquina A produziu 120 peças” ainda não permite uma conclusão gerencial.

A informação surge quando o dado recebe contexto e significado. Ao comparar a produção de 120 peças com uma meta de 200 peças, passa-se a compreender que houve desempenho abaixo do esperado. O conhecimento ocorre quando o profissional interpreta essa informação com experiência técnica e visão sistêmica. Nesse estágio, pode-se concluir que o baixo desempenho ocorreu devido a um elevado tempo de setup, manutenção inadequada ou gargalo operacional. Por fim, a decisão corresponde à ação tomada com base nesse conhecimento. Nesse caso, a empresa pode decidir aplicar SMED para redução de setup, realocar operadores ou programar manutenção corretiva.

Esse ciclo pode ser exemplificado utilizando SQL.

# 5. ACID versus BASE e por que ERP necessita de ACID

O modelo ACID é utilizado principalmente em bancos relacionais tradicionais e garante alta confiabilidade transacional. A Atomicidade determina que uma transação deve ocorrer totalmente ou não ocorrer. Em um ERP, por exemplo, a emissão de uma nota fiscal e a baixa do estoque precisam acontecer juntas. A Consistência garante que os dados permaneçam válidos após qualquer transação. Isso impede situações como estoque negativo ou registros financeiros incorretos. O Isolamento assegura que transações simultâneas não interfiram umas nas outras, evitando conflitos entre usuários acessando o sistema ao mesmo tempo. A Durabilidade garante que, após a confirmação da transação, os dados permaneçam armazenados mesmo em casos de falhas ou desligamentos.

Já o modelo BASE é comum em bancos NoSQL e prioriza disponibilidade e escalabilidade em ambientes distribuídos. O termo Basically Available significa que o sistema permanece disponível mesmo durante falhas. Soft State indica que os dados podem sofrer alterações temporárias. Eventual Consistency significa que a consistência dos dados ocorrerá futuramente, mas não necessariamente de forma imediata.

Sistemas ERP industriais necessitam fortemente do modelo ACID porque trabalham com informações críticas, como estoque, produção, compras, faturamento e finanças. Pequenas inconsistências podem gerar erros em MRP, planejamento produtivo, controle logístico e indicadores estratégicos. O modelo BASE é adequado para aplicações que toleram inconsistências temporárias, como redes sociais, streaming, cache e sistemas de grande distribuição. Entretanto, em ambientes industriais e corporativos, inconsistências momentâneas podem comprometer completamente a confiabilidade operacional. Por esse motivo, sistemas ERP normalmente utilizam bancos relacionais com propriedades ACID, garantindo integridade, rastreabilidade e segurança das informações industriais.
