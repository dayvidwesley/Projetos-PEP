# Prova oral N1 — Júlia Gabriela Brito Ferreira e Samuel Lorenzo Schirmbeck

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. Vocês modelaram a relação Ordem de Produção/Itens como composição e traduziram isso com `ON DELETE CASCADE`. Por que o CASCADE expressa composição e não agregação? E na relação Fornecedor/Pedido, por que esse mesmo CASCADE não caberia?

2. O POP está todo detalhado em MongoDB, com pipelines de agregação, mas a Tabela 4 aponta o PostgreSQL como SGBD de referência. Os dois resolveriam o mesmo problema de extração? Em que situação você escolheria um e descartaria o outro?

3. Vocês citam polyglot persistence apoiados em Stonebraker, Çetintemel e Zdonik (2005). Explique o conceito e dê um exemplo de dois bancos diferentes convivendo numa mesma operação industrial, dizendo qual tipo de dado ficaria em cada um.

4. Vocês usaram tempo de ciclo numa linha de produção para ilustrar o ciclo dado → informação → conhecimento → decisão. Refaça esse caminho oralmente: o que é o dado, o que vira informação, o que é conhecimento e qual decisão concreta fecha o ciclo.

5. Na Figura 1 vocês usam os estereótipos «PK» e «FK» no diagrama de classes. A partir desse diagrama, onde está garantida a 2FN na tabela `ordens_producao` e o que caracterizaria uma violação dessa forma normal ali?
