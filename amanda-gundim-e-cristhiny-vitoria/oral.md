# Prova oral N1 — Amanda Gundim e Cristhiny Vitória

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. Vocês definem a 2FN como "atributos não chave dependem integralmente da chave primária". Com chave simples isso é automático. Qual é o pré-requisito da 2FN, o que é dependência parcial e como ela é eliminada?
R: O pré-requisito da Segunda Forma Normal é a Primeira Forma Normal e, normalmente, é aplicada em tabelas com chave composta. Com relação à dependência parcial, ela pode ser definida como quando um atributo depende apenas de parte da chave primária e não da parte completa (o que gera redundâncias e inconsistências). Para que a dependência parcial seja eliminada, os atributos são separados em tabelas específicas, pois assim cada informação depende totalmente de uma chave primária correspondente.


2. PostgreSQL é ACID e MongoDB é BASE. O que cada sigla significa e por que essa diferença muda o tipo de aplicação adequada a cada um?
R: ACID = Atomicidade, Consistência, Isolamento e Durabilidade. Associado a bancos relacionais.
   BASE = Basically Available, Soft State e Eventual Consistency. Associado a bancos não relacionais.
   Essa diferença influencia diretamente o tipo de aplicação adequada para cada modelo, porque sistemas como ERPs e sistemas financeiros normalmente exigem maior consistência e confiabilidade dos dados, características presentes no ACID. Já aplicações como Big Data e IoT precisam lidar com grandes volumes de acessos e informações, favorecendo modelos mais flexíveis e escaláveis, como o BASE.


3. Diferenciem dado, informação, conhecimento e decisão. Por que esse ciclo só fecha quando o engenheiro acessa o banco direto, sem depender de relatório pronto?
R: Dado pode ser definido como um registro bruto, sem tratamento ou interpretação. A informação é o resultado da organização e contextualização de um conjunto de dados. A partir da análise das informações obtidas, o engenheiro em questão adquire conhecimento sobre o processo analisado. Então, a partir desse conhecimento, é possível que sejam tomadas decisões mais estratégicas e assertivas. Com relação ao ciclo de decisão só se fechar quando o engenheiro acessa o banco direto, isso ocorre devido à autonomia analítica que ele obtém, permitindo análises mais rápidas, flexíveis e adaptadas à necessidade real da operação.


4. Qual o teste prático que separa agregação de composição? Como cada uma é traduzida em SQL (chave estrangeira) e no MongoDB (referência ou documento embutido)?
R: O teste prático que separa agregação de composição é verificar se a entidade dependente consegue existir sem a entidade principal. Na agregação, as entidades conseguem existir separadamente. Já na composição, a entidade dependente só existe dentro da principal. Em SQL, ambas normalmente utilizam chave estrangeira, porém na composição costuma existir dependência mais forte, podendo utilizar regras como ON DELETE CASCADE. No MongoDB, agregações podem utilizar referências entre documentos, enquanto composições normalmente utilizam documentos embutidos.


5. Martin trata o banco como detalhe de infraestrutura. O que isso significa em termos de dependência entre camadas, e por que sustenta trocar PostgreSQL por MongoDB sem reescrever a regra de negócio?
R: Martin segue a visão da Clean Architecture em que os bancos de dados são tratados como um detalhe na infraestrutura e não como o centro do sistema. Ou seja, as regras de negócio não devem depender diretamente da tecnologia do banco utilizada. As dependências devem apontar para as camadas internas da aplicação, e não para os mecanismos externos. Em consequência disso, é possível alterar trocar PostgreSQL por MongoDB sem reescrever a regra de negócio.
