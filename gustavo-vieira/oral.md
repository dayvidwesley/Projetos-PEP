# Prova oral N1 — Gustavo Vieira Vale

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. A seção 2.2 trata arquitetura só "em camadas". Cite MVC, Clean Architecture e arquitetura hexagonal: como cada um trata o banco, e em qual ele é mais explicitamente um detalhe de infraestrutura?

R.: 
O MVC é uma arquitetura simples que divide o software em apenas 3 responsabilidades conectadas entre si: o Modelo, que agrupa as regras do negócio, a Visão, que é a interface do usuário, e, o Controlador, que recebe as ações e coordena as outras duas responsabilidades.

A Arquitetura Hexagonal é uma evolução do MVC, que utiliza portas e adaptadores. A ideia do modelo é conectar a interface (portas) com o mundo externo por meio dos adaptadores. Dessa forma, o núcleo da aplicação fica isolado do mundo externo.

Já a Clean Architecture utiliza a regra de dependência, ou seja, o código das camadas externas pode apontar para dentro, mas o código de dentro nunca pode conhecer o código de fora. Esse tipo de arquitetura divide o software em 4 camadas, sendo a mais interna as Entidades. As entidades não precisam de uma conexão ao banco de dados para funcionar, funcionam sozinhas em código limpo. A camada seguinte são os Casos de Uso, os quais vão ditar ações específicas do sistema (como um passo a passo das Ordens de Produção). Em seguida vem os Adaptadores de Interface, que é um conversor de dados, e, por fim, os Frameworks, onde ficam os detalhes técnicos da infraestrutura do software. É nesse caso em que o banco de dados é mais um detalhe de infraestrutura, pois, quando ele é alterado, apenas a camada externa está sendo modificada.

2. O histórico do banco está em três frases. Reconstrua: arquivos sequenciais e IMS nos anos 60, Codd em 1970, consolidação do SQL nos 80–90, NoSQL e polyglot persistence a partir dos 2000.

R.: 
Anos 1960 - Arquivos sequenciais e IMS predominavam. Eram sistemas baseados em arquivos e bancos hierárquicos, com baixa flexibilidade e forte dependência da estrutura física dos dados.
Anos 1970 - Início do Modelo Relacional, onde os dados eram organizados em tabelas que se relacionavam entre si. Teve início por Edgar F. Codd.
Anos 1980-1990 - Foi onde houve a consolidação do Modelo Relacional proposto por Codd na década anterior. Os SGBDs relacionais e a linguagem SQL tornaram-se padrão para armazenamento e consulta de dados corporativos. Bancos SQL: Oracle, PostgreSQL, MySQL etc
Anos 2000 - Surgimento dos bancos NoSQL para lidar com grande volume de dados, principalmente quando são pouco estruturados. Além disso, a partir desta época que houve a utilização de vários bancos de dados dependendo da aplicação.

3. Você menciona NoSQL mas não as propriedades transacionais. O que é ACID e BASE, por que seu cenário precisa de ACID e em que tipo de cenário industrial precisaria de BASE?

R.:
ACID e BASE são conjuntos de propriedades do banco de dados. Essas propriedades são relacionadas ao comportamento e à confiabilidade deste banco. 
O ACID é mais comum em bancos relacionais e significa Atomicidade, Consistência, Isolamento e Durabilidade. Isso é importante no meu cenário pois eu preciso que os dados sejam confiáveis e consistentes. Além disso, como a Melhoria de Processos depende do relacionamento entre tabelas e da geração de indicadores, qualquer inconsistência comprometeria a análise e as decisões de melhoria.
Já o BASE costuma aparecer em bancos NoSQL, significando propriedades de alta disponbilidade, mudanças de estado e consistência ao longo do tempo. Seria necessário em cenários de indústria que exigisse monitoramento de máquinas, telemetrias ou até sensores loT.

4. Você escolheu SQLite por simplicidade. Em que situações ele é insuficiente frente a PostgreSQL ou MySQL? Cite limitações concretas de concorrência, volume e acesso por rede.

R.:
Uma das desvantagens de utilizar o SQLite é que, quando ocorre escrita, o banco pode bloquear o arquivo, ou seja, em empresas maiores (com maior número de usuários, sistema web ou muitas atualizações simultâneas) isso pode gerar gargalos consideráveis. O PostgreSQL e MySQL possuem elementos mais robustos em relação a isso. Outra desvantagem é sobre o volume: se o banco de dados for muito grande há perda de desempenho do SQLite. Sempre que houver maior complexidade e volume de dados, PostgreSQL e MySQL são mais recomendados. Por fim, a principal limitação é arquitetual pois é um banco baseado em arquivo, ou seja, não opera como um servidor de banco de dados. PostgreSQL e MySQL trabalham nativamente com conexão cliente-servidor.

5. Você diz que "Melhoria de Processos" diferencia o Engenheiro de Produção do de Software. Ambos escrevem SQL, então o que define a especificidade do EP, e como o 5W2H da Tabela 18 materializa isso?

R.:
A diferença entre os engenheiros não é a ferramenta, como Python ou SQL, mas sim no objetivo da análise de dados e no tipo de problema que cada profissional resolve. Enquanto que o Engenheiro de Software trabalha mais com a infraestrutura lógica do banco de dados (com foco em desenvolvimento, performance do sistema, funcionamento etc), o Engenheiro de Produção utiliza o banco de dados como um meio para compreender e melhorar os processos. O foco da Engenharia de Produção é a eficiência, redução de gargalos, desperdícios, e, principalmente, apoio na tomada de decisão. A Tabela 18 materializa essa lógica pois mostra que o "trabalho" do engenheiro não termina na geração dos indicadores, mas sim interpretar o processo por meio de dados concretos e confiáveis e estruturar a intervenção organizacional.

