# Prova oral N1 — Juliana Tsader

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. A primeira página do artigo começa direto em "1. Introdução", sem título, autoria, resumo nem palavras-chave. Para que servem esses elementos no template ENEGEP/SBPO e o que se perde quando eles faltam?

2. Na Figura 2 você colocou `formacao_academica`, `atuacao_profissional` e `orientacoes` em composição com o pesquisador, e `Artigo`, `Banca` e `Projeto_pesquisa` em agregação N:M. Aplique o teste prático que separa as duas: por que uma orientação não sobrevive sem o pesquisador, mas um artigo sim?

3. Você escolheu MongoDB (documental) em vez de PostgreSQL (relacional) para o cenário Lattes. Justifique pela natureza do dado, usando os critérios da Tabela 1 que pesaram mais nessa decisão.

4. Você diz na 2.4 que bancos documentais permitem desnormalização deliberada. Isso significa que a 2FN e a 3FN deixam de valer? E como a 1FN é tratada num documento JSON com listas, por exemplo `formacao_academica`?

5. A seção 2.2 cobre camadas e Clean Architecture, mas não trata MVC. Onde o banco de dados se encaixa no padrão MVC, e como o MVC se diferencia da Clean Architecture quanto ao tratamento do banco?
