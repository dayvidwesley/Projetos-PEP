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

Resposta:
- A escolha entre ON DELETE CASCADE, RESTRICT ou SET NULL depende do tipo de relação entre as entidades: se é composição ou agregação.
O CASCADE só faz sentido em composição, quando a parte não existe sem o todo. O exemplo clássico é a a ordem de produção e itens: cada item existe só por causa daquela ordem específica. Se a ordem é apagada, é seguro e desejável que os itens sejam apagados junto, pra manter a base consistente.
O problema aparece quando o CASCADE é usado em uma relação de agregação, onde a parte existe de forma independente do todo. Um caso crítico é a relação entre Fornecedor e Pedido de Compra: se essa relação tiver CASCADE, apagar um fornecedor (por encerramento de contrato, por exemplo) apaga junto todo o histórico de pedidos feitos com ele, comprometendo a rastreabilidade financeira e a auditoria. Os pedidos são entidades autônomas e precisam continuar na base mesmo depois que o fornecedor sai. Outro exemplo é de setor e funcionário: se um setor for desativado com CASCADE configurado, todos os funcionários vinculados seriam apagados  o que é um erro grave, já que os colaboradores existem independentemente da estrutura organizacional atual.
Nesses casos de agregação, o RESTRICT e o SET NULL são mais seguros. O RESTRICT impede a exclusão da entidade principal enquanto houver registros vinculados a ela no caso do fornecedor, o sistema bloquearia a exclusão enquanto houvesse pedidos associados, forçando o engenheiro a tratar esses registros antes. Já o SET NULL é útil quando a parte pode continuar existindo desvinculada do todo: ao apagar um setor, o campo de setor no cadastro do funcionário fica nulo, preservando o colaborador e seu histórico.

4. Vocês combinam PostgreSQL, MongoDB e Redis (polyglot persistence). Se um sensor grava falha de máquina no MongoDB, como o ERP no PostgreSQL fica sabendo? Que padrão de integração resolve isso?

Resposta:
- O ERP no PostgreSQL fica sabendo do evento por meio de uma comunicação assíncrona baseada em eventos. O padrão de integração que resolve esse problema é a Arquitetura Orientada a Eventos (Event-Driven Architecture), utilizando o modelo Publish-Subscribe (Pub/Sub) ou Change Data Capture (CDC) intermediado por um Message Broker (como RabbitMQ, Kafka ou Redis). Assim que a falha é persistida no MongoDB, um evento é publicado e imediatamente consumido pelo ERP, que atualiza o PostgreSQL e dispara as ações operacionais necessárias.

5. Vocês recomendam credenciais em variáveis de ambiente ou cofres de segredos. O que distingue os dois e em que cenário cada um é preferível?

Resposta: 
- As variáveis de ambiente são preferíveis em cenários simples, como desenvolvimento local, trabalhos acadêmicos, protótipos e pequenos sistemas, porque são fáceis de configurar e já evitam que a senha fique escrita no código. Já os cofres de segredos são preferíveis em ambientes de produção, sistemas industriais, equipes grandes ou situações com dados sensíveis, pois oferecem criptografia, controle de acesso, auditoria e rotação de credenciais. Portanto, ambos aumentam a segurança, mas o cofre de segredos é mais indicado quando há maior criticidade, governança e necessidade de rastreabilidade.
