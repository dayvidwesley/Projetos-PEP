# Correção N1 — Donizette Neto e João Gabriel Azevedo
Data: 16/05/2026
Trabalho: Procedimento Operacional Padrão para Extração e Análise de Dados em Banco de Dados no Contexto da Engenharia de Produção

## Fundamentação teórica (peso 30%)

A fundamentação cobre os três blocos esperados com boa amplitude. Em 2.1, o SIG é definido com clareza, o pensamento sistêmico ganha exemplo concreto (atraso na produção ligado a estoque, compras, mão de obra e máquinas), os níveis operacional, tático e estratégico aparecem e o ciclo dado→informação→conhecimento→decisão é citado. Falta apenas a classificação clássica em SPT/SIG/SAD/SAE — incluir na próxima revisão.

Em 2.2, a discussão de arquitetura encadeia bem: camadas (Sommerville), MVC, Clean Architecture (Martin) e fecha com o argumento de que o banco pertence à infraestrutura mas é onde o registro operacional vive. Esse fechamento sustenta a tese central do POP.

Em 2.3, o histórico do banco de dados está completo e ancorado em referências primárias: Bachman (1973) para a fase pré-relacional, Codd (1970) com citação direta, Chamberlin e Boyce (1974) para o SEQUEL original, Sadalage e Fowler (2012) para polyglot persistence. Isso eleva o critério.

A seção 2.5, sobre agregação e composição, é o ponto mais forte do trabalho. Vocês trazem Booch et al. (referência primária de UML), distinguem corretamente a relação "todo-parte" com partes independentes (fornecedor/produto) da relação onde a parte não existe sem o todo (pedido/itens), e ainda mostram que a tradução em SQL é via FK e em NoSQL via documento embutido. Esse nível de articulação é o que a rubrica espera.

O ponto a corrigir: as definições das formas normais em 2.4 usam apelidos próprios não-padronizados ("Vínculo Pleno com a Identidade", "Conexão Direta e Exclusiva") e a redação fica vaga. A 2FN cita "tabelas com identificadores múltiplos", o que aponta para chave composta, mas não explicita o conceito de dependência parcial. Reescrever na terminologia técnica clássica (dependência funcional, chave composta, dependência parcial, dependência transitiva) traria mais precisão.

Nota do critério: 9,0.

## Qualidade da revisão bibliográfica (peso 20%)

Bibliografia bem construída, com destaque para o uso de fontes primárias: Bachman 1973, Booch et al. 2005, Chamberlin e Boyce 1974, Codd 1970, Han et al. 2011 em paper IEEE. Sadalage e Fowler aparecem, Martin para Clean Architecture, Sommerville e Pressman/Maxim para engenharia de software, Date para BD. ABNT consistente.

Senti falta de pelo menos uma referência clássica de SIG (Laudon ou O'Brien) e uma referência forte de modelagem de BD (Elmasri e Navathe ou Silberschatz). As referências Ávila/Mello e Bazzotti/Garcia aparecem com "[s.d.]" (sem data), o que enfraquece o critério ABNT — vale procurar a data correta.

Nota do critério: 8,5.

## Normalização e modelagem de dados (peso 20%)

As três formas normais estão definidas (com a ressalva do uso de apelidos não-padrão, já comentada). Os relacionamentos 1:1, 1:N e N:M aparecem corretamente. Agregação e composição estão bem tratadas, com a tradução em SQL e NoSQL explicitamente apresentada — esse nível de detalhe é o que a rubrica espera no topo do critério.

A Figura 1 é um diferencial: diagrama ER próprio do cenário, com quatro entidades (fornecedor, produto, pedido, cliente) e chaves identificadas. Aproveitar esse diagrama na N2 é exatamente o que a rubrica espera.

Há um problema de modelagem no diagrama que precisa ser revisto antes da N2: a entidade "pedido" tem `id_cliente` e `id_produto` diretamente, o que implica que cada pedido contém um único produto. No mundo real de uma ferragista, um pedido tipicamente reúne vários produtos em quantidades diferentes (relação N:M entre Pedido e Produto). A modelagem correta exige uma entidade associativa do tipo "Item de Pedido" (ou "Pedido_Produto") com `id_pedido`, `id_produto`, `quantidade` e `preco_unitário`. Sem isso, ou cada pedido vira várias linhas duplicando dados do cabeçalho (violando 2FN), ou o sistema só permite pedidos com um item.

Nota do critério: 8,5.

## Procedimento de conexão documentado (peso 15%)

A escolha do MySQL 8.0 hospedado na Aiven.io traz o procedimento para perto de um cenário corporativo real. Vocês mostram a tela do serviço Aiven com os parâmetros (host, port, user, password, database name, SSL mode), explicitam a configuração via arquivo `.env` carregado por `python-dotenv`, exibem o código Python que constrói o dict de configuração com `os.getenv`, citam o `mysql-connector` como biblioteca de conexão e mostram o MySQL Workbench como ferramenta gráfica com aba de SSL configurada.

O cuidado com a anonimização dos dados pessoais (CPF, CNPJ, e-mails, telefones) também é um ponto importante e mostra atenção à LGPD, mesmo em escopo acadêmico.

O que falta para fechar com nota cheia é apenas o trecho final da conexão: o `mysql.connector.connect(**config)` sendo executado e devolvendo o cursor, com pelo menos uma query SELECT de exemplo rodando contra alguma das quatro tabelas. Esse fechamento será cobrado na N2.

Nota do critério: 9,5.

## Formatação ENEGEP/SBPO (peso 15%)

Template oficial, cabeçalho, resumo, palavras-chave, seções numeradas (com seção 4 dedicada a Resultados Esperados, como o padrão ENEGEP pede), tabelas e figuras numeradas e referenciadas. Bom nível formal.

Dois ajustes a fazer:

- Há duas figuras numeradas como "Figura 4" no texto (uma do método de configuração de credenciais, outra do MySQL Workbench). Renumerar para Figura 4 e Figura 5.
- A "Figura 3" é citada antes de aparecer no texto e a referência cruzada à "Figura 4" no parágrafo da Workbench na verdade quer indicar a tela do Workbench, mas o número está repetido. Revisar ordem de citação.
- Falta uma seção 5 de Conclusão/Considerações Finais distinta da "4. Resultados esperados" — mesmo em N1 isso é esperado para fechar o artigo no padrão ENEGEP.

Nota do critério: 8,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 9,0 | 30% | 2,70 |
| Revisão bibliográfica | 8,5 | 20% | 1,70 |
| Normalização e modelagem | 8,5 | 20% | 1,70 |
| Procedimento de conexão | 9,5 | 15% | 1,425 |
| Formatação ENEGEP/SBPO | 8,0 | 15% | 1,20 |
| **Total** | | | **8,7** |

## Para a N2

Quatro frentes principais:

1. Revisar o diagrama ER incluindo a entidade associativa "Item de Pedido" entre Pedido e Produto, com quantidade e preço unitário, e marcando agregação versus composição visualmente no modelo.
2. Reescrever as três formas normais usando terminologia técnica padrão (dependência funcional, chave composta, dependência parcial, dependência transitiva), com exemplo do próprio caso da ferragista.
3. Executar a conexão real com `mysql.connector.connect(**config)`, mostrar o cursor recebendo o resultado de pelo menos uma query simples e capturar o print do retorno.
4. Renumerar as figuras (corrigir a duplicação da Figura 4) e adicionar uma seção 5 de Considerações Finais separada de Resultados Esperados.
