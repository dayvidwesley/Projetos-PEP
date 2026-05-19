# Prova oral N1 — Gabriel Campos e Rafael Campos

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. Vocês citam o ciclo dado → informação → conhecimento (Stair e Reynolds) sem ilustrar. Diferenciem os estágios, mostrem onde entra a decisão e dê um exemplo de consulta SQL que transforma dado bruto em informação útil.

RESPOSTA: Dado é valor bruto sem contexto; Informação é o dado quando recebe significado; Conhecimento é quando a informação é analisada e a partir disso é feita a tomada de decisão. Um exemplo é quando dados são armazenados de forma bruta em uma tabela "pedidos" e através de consulta SQL são transformados em informaçao útil apresentando a quantidade de pedidos por setor, permitindo análises operacionais e apoio à tomada de decisão,

2. Vocês citam Brewer (2012) para o BASE. Como o teorema CAP justifica o BASE do MongoDB, e por que o PostgreSQL prioriza o ACID?

RESPOSTA: O teorema CAP afirma que sistemas distribuídos não conseguem garantir simultaneamente Consistência, Disponibilidade  e Tolerância a Partições. O MongoDB adota o modelo BASE justamente porque prioriza disponibilidade e escalabilidade, aceitando consistência eventual em determinadas situações. O BASE significa Basically Available, Soft State e Eventual Consistency, ou seja, o sistema mantém disponibilidade mesmo que os dados demorem um curto período para ficarem totalmente consistentes. Já o PostgreSQL prioriza o modelo ACID porque trabalha fortemente com integridade e confiabilidade transacional. O ACID garante Atomicidade, Consistência, Isolamento e Durabilidade, características essenciais em aplicações que não podem correr risco de inconsistência, como sistemas financeiros, ERPs e controle de estoque.

3. Numa tabela `item_pedido` com chave composta `(pedido_id, produto_id)` e atributos `quantidade`, `preço_unitário` e `nome_produto`, qual atributo viola a 2FN e como corrigir?

RESPOSTA: Na tabela “item_pedido”, considerando a chave composta (pedido_id, produto_id), o atributo que viola a Segunda Forma Normal (2FN) é o “nome_produto”. Isso ocorre porque ele depende apenas de “produto_id” e não da chave composta inteira. A 2FN exige que todos os atributos não-chave dependam da chave completa, e não apenas de parte dela. A correção consiste em remover o atributo “nome_produto” da tabela “item_pedido” e criar uma tabela separada de produtos.

4. Vocês citam `ON DELETE CASCADE` como composição em SQL. Em que situação o CASCADE causa perda indevida de dados, e quando RESTRICT ou SET NULL são preferíveis?

RESPOSTA: O uso do ON DELETE CASCADE pode
causar perda indevida de dados quando a exclusão de um registro pai remove automaticamente registros filhos que ainda possuem relevância para o sistema. Por exemplo, ao excluir um cliente, todos os pedidos vinculados a ele poderiam ser apagados automaticamente, causando perda do histórico de vendas da empresa. Nesses casos, utilizar RESTRICT pode ser mais adequado, pois impede a exclusão do registro pai enquanto existirem registros relacionados. Já o SET NULL é preferível quando o relacionamento pode deixar de existir sem necessidade de apagar os dados filhos.

5. Vocês citam MVC e Clean Architecture. Qual a diferença essencial entre os dois e em qual o banco é mais explicitamente tratado como detalhe de infraestrutura?

RESPOSTA: A principal diferença entre MVC e Clean Architecture está no foco estrutural da aplicação. O MVC organiza o sistema em três camadas principais: Model, View e Controller, separando interface, regras de negócio e controle da aplicação. Já a Clean Architecture possui foco maior em independência das regras de negócio, organizando o sistema em camadas concêntricas onde as regras centrais não dependem de tecnologias externas. Na Clean Architecture, o banco de dados é tratado explicitamente como um detalhe de infraestrutura, ou seja, a aplicação principal não deve depender diretamente do banco utilizado. Isso permite trocar PostgreSQL por MongoDB, por exemplo, sem alterar as regras centrais do sistema. No MVC essa separação existe, mas normalmente o banco de dados ainda fica mais acoplado à estrutura da aplicação.
