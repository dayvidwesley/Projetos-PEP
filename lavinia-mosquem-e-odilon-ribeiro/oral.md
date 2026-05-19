# Prova oral N1 — Lavínia Mosquem Padilha da Silva e Odilon Ribeiro Pimentel

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. Vocês definiram composição como o caso ordem de produção/itens, com `ON DELETE CASCADE`, e agregação como fornecedor/pedido. Pelo teste da dependência, por que o pedido sobrevive sem o fornecedor mas o item não sobrevive sem a ordem?

*Resposta (Questão 1):

Porque no caso do pedido de compra e o fornecedor, o fornecedor continua existindo como entidade independente mesmo que não tenha nenhum pedido ativo. Ele tem CNPJ, cadastro, histórico. O pedido some, o fornecedor permanece. Assim, as partes independentes que se relacionam.

No caso da ordem de produção e seus itens, o item da ordem não tem existência própria fora da ordem. Ele não é um produto em si, é uma instrução vinculada àquela ordem específica: “cortar 3 peças do lote X para a OP 447”. Se a OP 447 é cancelada e excluída, esse item não tem mais razão de existir. Por isso o ciclo de vida da parte está subordinado ao ciclo de vida do todo. Se tratando do ON DELETE CASCADE no banco ele apenas implementa isso tecnicamente, e quando a ordem é excluída, o banco automaticamente exclui os itens vinculados.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

2. O artigo trata bem a governança de TI com o audit trail. Explique o que é o audit trail e por que ele dá ao engenheiro algo que uma planilha compartilhada nunca dá.

*Resposta (Questão 2):

Audit trail é uma trilha de auditoria, que é basicamente um registro automático e imutável que o banco de dados mantém de toda operação realizada sobre os dados: quem acessou, o que alterou, qual era o valor anterior, qual ficou, data e hora exatos.

A diferença para a planilha é estrutural, não de configuração. Na planilha compartilhada, se alguém altera um valor, o valor anterior simplesmente desaparece e não há como saber quem alterou, quando, nem o que estava lá antes. Pode até existir o histórico de versões em algumas ferramentas, mas isso é frágil e pode ser desativado.

Para o engenheiro, isso significa que toda análise que ele faz está ancorada em dados com procedência verificável. Se um indicador apontar uma anomalia, ele consegue rastrear quando aquele dado entrou no sistema, quem inseriu e se houve alteração posterior.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

3. Na 2FN, vocês escrevem que todo atributo não-chave depende da chave primária completa. Dê um exemplo de uma tabela que está na 1FN mas viola a 2FN, e mostre como corrigir.

*Resposta (Questão 3):

A 2FN só se aplica quando a tabela tem chave primária composta — formada por dois ou mais campos. A violação acontece quando um atributo não-chave depende só de parte dessa chave, não dela inteira.

O exemplo que usamos no artigo é uma tabela de itens de pedido, cuja chave composta é ID_Pedido mais ID_Produto. Nessa tabela, se eu colocar o campo Nome_Produto, eu estou violando a 2FN — porque o nome do produto depende só do ID_Produto, não do pedido. O nome “Parafuso M8” é uma característica do produto, independe de qual pedido ele está.

A correção é separar: criar uma tabela de Produtos com ID_Produto e Nome_Produto, e na tabela de itens do pedido fico só com o que realmente depende dos dois campos juntos — que é a quantidade pedida. O ID_Produto vira chave estrangeira ligando as duas tabelas.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

4. A metodologia adota o Databricks com Delta Lake. Esse ambiente é relacional, NoSQL ou outra coisa? Justifique a escolha dele em função do tipo de dado logístico que vocês vão analisar.

*Resposta (Questão 4):

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

5. Vocês citam polyglot persistence. No fluxo sensor → banco → análise → decisão → ação que aparece no texto, em que parte entraria um banco NoSQL e por quê?

*Resposta (Questão 5):
