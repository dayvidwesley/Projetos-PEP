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

## Prova oral

Nota: 9,0

Respostas corretas: dependência funcional e parcial, a entidade itens_pedido em N:M, o ON DELETE CASCADE, a polyglot persistence no cenário da ferragista e o ciclo do dado até a decisão com uma consulta SQL ligando dado e informação.

# Correção N2 — Donizette Neto e João Gabriel Azevedo
Data: 27/06/2026
Trabalho: Procedimento Operacional Padrão para Extração e Análise de Dados em Banco de Dados no Contexto da Engenharia de Produção

Vocês endereçaram as frentes conceituais da N1: a entidade associativa itens_pedido entrou no diagrama (Figura 1, p. 9), as formas normais foram reescritas em terminologia técnica (p. 8-9, com Elmasri e Navathe), e a seção 5 de Considerações Finais foi adicionada. E, principalmente, a conexão saiu do papel.

## Conexão e extração de dados (peso 25%)

Esse é o ponto forte da entrega e o que mais cobrei na N1. A conexão é real e está comprovada: MySQL 8.0 na Aiven com SSL, código carregando credenciais por .env (Figura 4), a função inicializar_banco_de_dados() executando mysql.connector.connect(**config) e o print do terminal na Figura 8 (p. 17) mostrando a conexão estabelecida e 50 clientes retornados. É reprodutível e cuidadoso com a LGPD, com as credenciais fora do código.

Nota do critério: 8,0.

## Qualidade das queries e análises (peso 25%)

Aqui mora a limitação. As únicas queries SQL que vocês de fato exibem rodando são duas, e ambas são de validação: um COUNT(*) em clientes e um SELECT com LIMIT 10 em produtos (p. 14). As análises que importam, faturamento por produto, por cliente e por fornecedor, que aparecem no dashboard da Figura 9, implicam JOIN, GROUP BY e SUM, mas o SQL (ou o DAX) que as gera não está no artigo. A Figura 7 mostra a tela do Power BI com uma instrução SQL começando um JOIN entre itens_pedido e pedido, só que a consulta aparece cortada. A extração séria existe, os números do dashboard provam isso, mas vocês não a mostraram. Para um trabalho cujo tema é extrair dados do banco, deixar a query principal fora do texto custa caro.

Nota do critério: 6,5.

## Indicadores gerados e interpretação (peso 20%)

O dashboard (Figura 9) traz indicadores úteis de gestão: faturamento total de R$ 685,49 mil, ticket médio e os rankings de faturamento por produto, por cliente e por fornecedor. A interpretação amarra isso a decisão concreta, qual produto comprar em maior quantidade, quais marcas têm mais saída, reposição de estoque, gestão de fornecedores (seção 4 e Considerações Finais, p. 18). Fecha o ciclo dado→decisão, ainda que num registro mais qualitativo, sem um número-gatilho específico.

Nota do critério: 8,0.

## Código documentado e reprodutível (peso 15%)

O código de conexão está bem feito: docstring, comentários, tratamento de erro com try/except, .env. Boa engenharia. Pesa contra a ausência do código que gera os indicadores (não dá para reproduzir o dashboard a partir do artigo), a falta de requirements.txt/README e o fato de a pasta N2 do repositório ter só um placeholder de 1 byte, sem scripts versionados. Some-se a divergência de data da referência Bazzotti e Garcia (2003 no texto, 2006 na lista) e a Figura 1, que ainda mantém id_produto dentro de pedido, resíduo do modelo antigo que convive de forma incoerente com a associativa itens_pedido. A duplicação da "Figura 4" que apontei na N1 também persiste.

Nota do critério: 7,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Conexão e extração de dados | 8,0 | 25% | 2,00 |
| Qualidade das queries e análises | 6,5 | 25% | 1,625 |
| Indicadores gerados e interpretação | 8,0 | 20% | 1,60 |
| Código documentado e reprodutível | 7,5 | 15% | 1,125 |
| **Soma ponderada (85%)** | | | **6,35** |

A N2 não terá prova oral. A nota final, renormalizando os quatro critérios (85% da rubrica) para a escala de 0 a 10, é **7,5**. Com o ponto extra atribuído na N2, a nota final fica **8,5**.
