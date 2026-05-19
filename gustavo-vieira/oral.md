# Prova oral N1 — Gustavo Vieira Vale

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. A seção 2.2 trata arquitetura só "em camadas". Cite MVC, Clean Architecture e arquitetura hexagonal: como cada um trata o banco, e em qual ele é mais explicitamente um detalhe de infraestrutura?

R.: 
O MVC é uma arquitetura simples que divide o software em apenas 3 responsabilidades conectadas entre si: o Modelo, que agrupa as regras do negócio, a Visão, que é a interface do usuário, e, o Controlador, que recebe as ações e coordena as outras duas responsabilidades.

A Arquitetura Hexagonal é uma evolução do MVC, que utiliza portas e adaptadores. A ideia do modelo é conectar a interface (portas) com o mundo externo por meio dos adaptadores. Dessa forma, o núcleo da aplicação fica isolado do mundo externo.

Já a Clean Architecture utiliza a regra de dependência, ou seja, o código das camadas externas pode apontar para dentro, mas o código de dentro nunca pode conhecer o código de fora. Esse tipo de arquitetura divide o software em 4 camadas, sendo a mais interna as Entidades. As entidades não precisam de uma conexão ao banco de dados para funcionar, funcionam sozinhas em código limpo. A camada seguinte são os Casos de Uso, os quais vão ditar ações específicas do sistema (como um passo a passo das Ordens de Produção). Em seguida vem os Adaptadores de Interface, que é um conversor de dados, e, por fim, os Frameworks, onde ficam os detalhes técnicos da infraestrutura do software. É nesse caso em que o banco de dados é mais um detalhe de infraestrutura, pois, quando ele é alterado, apenas a camada externa está sendo modificada.

2. O histórico do banco está em três frases. Reconstrua: arquivos sequenciais e IMS nos anos 60, Codd em 1970, consolidação do SQL nos 80–90, NoSQL e polyglot persistence a partir dos 2000.
   
3. Você menciona NoSQL mas não as propriedades transacionais. O que é ACID e BASE, por que seu cenário precisa de ACID e em que tipo de cenário industrial precisaria de BASE?

6. Você escolheu SQLite por simplicidade. Em que situações ele é insuficiente frente a PostgreSQL ou MySQL? Cite limitações concretas de concorrência, volume e acesso por rede.

7. Você diz que "Melhoria de Processos" diferencia o Engenheiro de Produção do de Software. Ambos escrevem SQL, então o que define a especificidade do EP, e como o 5W2H da Tabela 18 materializa isso?
