# Prova oral N1 — Guilherme Alves e Vinycius Cirilo

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. A Tabela 1 cita BASE como contraponto do ACID, sem expandir. O que significa cada letra de BASE e como o teorema CAP justifica a escolha entre ACID e BASE em sistemas distribuídos?

Resposta: 
- BASE significa Basically Available, Soft state, Eventual consistency. Basicamente disponível quer dizer que o sistema responde mesmo que parte dos nós esteja com problema, ainda que a resposta possa ser parcial ou desatualizada. Soft state significa que o estado do sistema pode mudar com o tempo mesmo sem novas escritas, porque os nós estão se sincronizando entre si. Eventual consistency é a promessa de que, dado tempo suficiente sem novas atualizações, todos os nós convergirão para o mesmo valor.      
O teorema CAP diz que em sistema distribuído só se garantem duas de três propriedades: Consistência, Availability e Partition tolerance. Como partição de rede é inevitável, a escolha real é entre C e A. ACID escolhe C; BASE escolhe A.
Na prática: ERP financeiro é ACID (não posso ter saldo divergente entre nós). Telemetria de sensor é BASE (prefiro leitura atrasada a perder o dado).



2. As Figuras 1 e 2 mostram `GROUP BY` no SQL e `$group` no MongoDB como equivalentes. Em que situação essa equivalência se quebra, por exemplo num JOIN de várias tabelas com relacionamentos profundos?

Resposta: 
- A equivalência só vale enquanto a agregação é sobre uma única tabela ou coleção. Quebra quando precisa cruzar fontes.
No SQL, JOIN é operação de primeira classe, o otimizador decide a estratégia de junção. No MongoDB, o equivalente é o $lookup, que é mais caro e degrada rápido em joins encadeados de três ou quatro coleções.
Por isso o MongoDB evita o cenário através da denormalização: ou embute o filho no documento, ou duplica controladamente. SQL coloca a complexidade no query e o NoSQL coloca no esquema.

3. Vocês definem composição com `ON DELETE CASCADE`. Em que cenário industrial o CASCADE causa perda indevida de dados, e quando RESTRICT ou SET NULL são mais seguros?

4. Vocês combinam PostgreSQL, MongoDB e Redis (polyglot persistence). Se um sensor grava falha de máquina no MongoDB, como o ERP no PostgreSQL fica sabendo? Que padrão de integração resolve isso?

5. Vocês recomendam credenciais em variáveis de ambiente ou cofres de segredos. O que distingue os dois e em que cenário cada um é preferível?
