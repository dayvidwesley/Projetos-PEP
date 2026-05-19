# Correção N1 — Amanda Gundim e Cristhiny Vitória
Data: 16/05/2026
Trabalho: Análise Comparativa entre Bancos de Dados Relacionais e Não Relacionais: um Estudo Prático com PostgreSQL e MongoDB

## Fundamentação teórica (peso 30%)

A dupla cobriu os três blocos pedidos (SIG, arquitetura de software, banco de dados) com boa amplitude e ancoragem em autores de referência. A seção 2.1 traz a classificação SPT/SIG/SAD/SAE com base em Laudon, o ciclo dado→informação→conhecimento→decisão fica claro e o pensamento sistêmico é discutido com Guerreiro et al. e Lima/Redaelli. A parte de governança de TI, mencionada na Aula-03, ficou de fora e seria bom citar.

Em arquitetura (2.2), camadas, Clean Architecture, hexagonal e cliente-servidor aparecem com Fowler e Martin como base. A discussão fica bem encaminhada, mas a articulação com o tema central do trabalho (BD como camada de infraestrutura desacoplada) só aparece de passagem no fim de 2.3.1. Esse gancho poderia ter virado fio condutor.

Na parte de BD, há um ponto frágil que vale destacar: o histórico do BD por décadas (anos 60 com arquivos sequenciais, 70 com Codd e modelo relacional, 80-90 com SQL, 2000 com NoSQL, 2010+ com polyglot persistence) está pedido no roteiro e não aparece. Vocês entram direto no Codd como fundador do relacional. Recuperar esse percurso ajuda a justificar por que o MongoDB surge e em que contexto. Também notei que a definição de 2FN na seção 2.5 ficou mais simples do que devia: "atributos não chave dependem integralmente da chave primária" só fecha em chave composta. Vale reforçar que 2FN pressupõe 1FN e ataca dependências parciais.

Pontos fortes: três blocos sustentados, citações de autores fortes (Codd via Elmasri, Martin para Clean Architecture, Sadalage/Fowler para NoSQL), definições conceitualmente corretas.

Nota do critério: 8,0.

## Qualidade da revisão bibliográfica (peso 20%)

Esse foi o ponto mais forte do trabalho. A bibliografia tem variedade real: Date, Elmasri e Navathe, Silberschatz/Korth/Sudarshan, Fowler, Martin, Sadalage, Banker, Laudon, Lima/Redaelli, Guerreiro et al., Arantes et al. em paper IEEE. Mistura livros consagrados com artigos acadêmicos e documentação oficial, e as citações no corpo seguem ABNT de forma consistente.

Dois deslizes pequenos: o sobrenome aparece como "Rendaelli" em algumas passagens e "Redaelli" em outras (conferir Revista Foco) e duas referências de site (Database Star e Carvalho) poderiam ter sido substituídas por figuras de Elmasri ou Date, que vocês já citam. Não compromete o critério.

Nota do critério: 9,0.

## Normalização e modelagem de dados (peso 20%)

As três formas normais estão definidas, com a ressalva sobre a 2FN feita acima. Relacionamentos 1:1, 1:N e N:N aparecem com cardinalidade correta e tabela associativa mencionada para os N:N. Agregação e composição estão bem distinguidas, com os exemplos clássicos de fornecedor/pedido e ordem de produção/itens, e a tradução para SQL (FK) e MongoDB (referência ou documento embutido) aparece.

A Figura 2 (diagrama ER de Funcionário/Departamento/Projeto) e a Figura 3 (diagrama de Student/Course) ilustram o conceito, mas são exemplos das fontes e não do cenário próprio. Como o trabalho de vocês é comparativo entre SGBDs, essa escolha tem coerência. Na N2, com a base de dados fornecida, vai ser preciso construir um diagrama desse banco para sustentar o critério de "exemplos do próprio caso".

Nota do critério: 8,0.

## Procedimento de conexão documentado (peso 15%)

A seção 3.6 lista os elementos esperados: parâmetros de conexão do Postgres (host, porta, banco, usuário, autenticação) com pgAdmin, e string de conexão do MongoDB com Compass. Em 3.3 vocês também mencionam psycopg2 e pymongo. O escopo está coerente com o que se espera de um POP em fase de planejamento.

O que falta para chegar ao topo do critério é mostrar a coisa funcionando: exemplo de string de conexão, trecho de código Python com cursor de uma query simples, captura de tela do pgAdmin ou Compass conectado. Esse adensamento é exatamente o que a N2 vai exigir.

Nota do critério: 7,0.

## Formatação ENEGEP/SBPO (peso 15%)

Template oficial, cabeçalho, resumo, palavras-chave, numeração das seções, tabelas e figuras numeradas e referenciadas no texto. Referências em ABNT. A parte formal está bem cuidada.

O ponto a corrigir é estrutural: faltam as seções de Resultados e Conclusão. A especificação do trabalho diz que na N1 essas seções podem aparecer parciais ou como planejamento, e parte desse conteúdo até está espalhado na metodologia. Mas formalmente o artigo termina em "3.7 Procedimento de extração e análise" e parte direto para as referências. Recomendo encerrar com pelo menos um "4. Resultados esperados" e uma "5. Considerações parciais" amarrando o que será feito na N2.

Nota do critério: 7,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 8,0 | 30% | 2,40 |
| Revisão bibliográfica | 9,0 | 20% | 1,80 |
| Normalização e modelagem | 8,0 | 20% | 1,60 |
| Procedimento de conexão | 7,0 | 15% | 1,05 |
| Formatação ENEGEP/SBPO | 7,5 | 15% | 1,125 |
| **Total** | | | **8,0** |

## Para a N2

Três frentes a endereçar antes da entrega prática:

1. A partir da base de dados fornecida, construir o diagrama do modelo de dados desse cenário, com 1FN/2FN/3FN aplicadas ao próprio caso e agregações/composições identificadas no modelo.
2. Documentar a conexão de verdade: string de conexão, código Python rodando, print do pgAdmin/Compass conectado.
3. Fechar com as seções 4 e 5 efetivamente: indicadores extraídos, queries que respondem a uma pergunta de Engenharia de Produção e amarra final no ciclo dado→decisão.
