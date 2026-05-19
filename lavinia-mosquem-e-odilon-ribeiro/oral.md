# Prova oral N1 — Lavínia Mosquem Padilha da Silva e Odilon Ribeiro Pimentel

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. Vocês definiram composição como o caso ordem de produção/itens, com `ON DELETE CASCADE`, e agregação como fornecedor/pedido. Pelo teste da dependência, por que o pedido sobrevive sem o fornecedor mas o item não sobrevive sem a ordem?

2. O artigo trata bem a governança de TI com o audit trail. Explique o que é o audit trail e por que ele dá ao engenheiro algo que uma planilha compartilhada nunca dá.

3. Na 2FN, vocês escrevem que todo atributo não-chave depende da chave primária completa. Dê um exemplo de uma tabela que está na 1FN mas viola a 2FN, e mostre como corrigir.

4. A metodologia adota o Databricks com Delta Lake. Esse ambiente é relacional, NoSQL ou outra coisa? Justifique a escolha dele em função do tipo de dado logístico que vocês vão analisar.

5. Vocês citam polyglot persistence. No fluxo sensor → banco → análise → decisão → ação que aparece no texto, em que parte entraria um banco NoSQL e por quê?
