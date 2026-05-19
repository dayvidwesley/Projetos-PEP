# Prova oral N1 — Donizette Neto e João Gabriel Azevedo

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. Vocês definem a 2FN como "tabelas com identificadores múltiplos em que cada detalhe possua conexão com o conjunto identificador". Reformulem na terminologia clássica: o que é dependência funcional, dependência parcial e por que a 2FN só faz sentido com chave composta?
   R: Dependência parcial é quando um atributo não primário depende apenas de uma chave da chave composta. A dependência funcional ocorre quando um atributo de uma tabela depende de outro atributo para ser identificado. Por isso, a 2FN só faz sentido em tabelas com chave composta, pois somente nesse caso existe a possibilidade de um campo depender de apenas uma parte da chave.
   
2. A Figura 1 modela Pedido com `id_cliente` e `id_produto` direto. Se um pedido tem cinco produtos, o diagrama representa isso? Que entidade nova surge e com que cardinalidade de cada lado?
   R: Infelizmente não representa corretamente. Se um pedido tem cinco produtos, o modelo com id_produto direto dentro de pedidos só permite representar um produto por pedido. A entidade nova que surge é: itens_pedido com a cardinalidade N:M.

3. Na implementação em MySQL, qual cláusula do `CREATE TABLE` distingue composição de agregação? O que acontece com os itens se ela for configurada errada e o pedido for removido?
   R: A cláusula é o "ON DELETE CASCADE", aplicado em uma chave estrangeira. Essa cláusula indica que, quando o registro principal for excluído, os registros dependentes também serão removidos automaticamente. Se essa regra for configurada de forma incorreta, os itens podem permanecer sem relação no banco após a exclusão do pedido ou registros podem ser apagados indevidamente caso o ON DELETE CASCADE seja usado em uma relação de agregação.

4. Vocês citam polyglot persistence (Sadalage e Fowler). No cenário da ferragista, em que tipo de dado o MongoDB seria preferível ao MySQL, e em que ponto o MySQL é insubstituível?
   R: No cenário da ferragista, o MongoDB seria preferível para dados mais flexíveis, variáveis ou não estruturados, como histórico de alterações de estoque e observações livres sobre pedidos. Já o MySQL é mais adequado para os dados centrais da operação, como fornecedores, produtos, clientes, pedidos, itens de pedido, entre outros. Esses dados exigem consistência, chaves primárias, chaves estrangeiras e consultas relacionais, características mais bem atendidas por um banco relacional.

5. Apliquem o ciclo dado → informação → conhecimento → decisão à ferragista: dê um exemplo de cada etapa e mostre como uma consulta SQL liga o dado à informação.
   R:
