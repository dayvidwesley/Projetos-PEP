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

## Prova oral

Nota: 9,0

As cinco respostas corretas e bem colocadas: 2FN com dependência parcial, ACID e BASE, o ciclo do dado até a decisão, o teste que separa agregação de composição e o banco como detalhe de infraestrutura na Clean Architecture.

# Correção N2 — Amanda Gundim e Cristhiny Vitória
Data: 27/06/2026
Trabalho: Análise Comparativa entre Bancos de Dados Relacionais e Não Relacionais: um Estudo Prático com PostgreSQL e MongoDB

Vocês fecharam as duas frentes estruturais que cobrei na N1: o artigo agora tem as seções 4 e 5 cheias (p. 26-44) e a comparação prática PostgreSQL × MongoDB saiu do plano e virou execução sobre os dois bancos fornecidos. É um avanço real.

## Conexão e extração de dados (peso 25%)

A conexão está documentada nos dois bancos: parâmetros do Postgres (host, porta 5432, banco erp, usuário) na p. 21 e a URI do Mongo na p. 31, com prints do DBeaver e do Compass. O problema é que a extração não acontece dentro do SGBD. Vocês conectam pela ferramenta gráfica, exportam as coleções do Mongo para CSV (p. 31-33) e levam tudo para o Power BI. A etapa "Extrair" do POP pedia consulta rodando no banco (SQL ou pipeline), e isso não aparece: quem reproduz o trabalho de vocês reproduz um relatório de Power BI, não uma consulta ao banco. Some-se a isso o print trocado, a Figura 7 (p. 22) tem legenda "Servidor PostgreSQL conectado via DBeaver" mas mostra a tela do Compass. Confiram, porque é a evidência da conexão do Postgres que fica comprometida.

Nota do critério: 7,0.

## Qualidade das queries e análises (peso 25%)

Não há SQL nem pipeline de agregação do Mongo. Toda a análise foi feita em DAX no Power BI (p. 30-31, 40-42). Avaliando o que de fato foi entregue, as medidas DAX têm complexidade real: CALCULATE com filtro de grupo de DRE, SUMX iterando quantidade por preço para a receita, e a decomposição do OEE em disponibilidade, performance e qualidade. O trecho mais forte é a Tabela_Paradas (p. 42), onde vocês usam UNION/SELECTCOLUMNS/FILTER para desaninhar o array de paradas que vem do documento do Mongo, mostrando que entenderam a diferença estrutural entre o dado relacional e o documental e souberam tratá-la. O que pesa contra é o desalinhamento com o que a N2 pede: a inteligência analítica está toda na camada de BI, depois da extração, e não em consulta ao próprio banco. Para um trabalho que se propõe a comparar PostgreSQL e MongoDB na prática, faltou mostrar a mesma pergunta respondida com um SELECT no Postgres e com um aggregate no Mongo.

Nota do critério: 7,0.

## Indicadores gerados e interpretação (peso 20%)

Aqui o trabalho se destaca. Os painéis cobrem comercial, produção, financeiro e manutenção (Figuras 12 a 20), e a interpretação não é genérica. Vocês lêem o OEE de 80,72% identificando a disponibilidade (~89%) como o componente que mais derruba o índice frente ao benchmark de 85% (p. 35-37), apontam a concentração de 22,27% do faturamento num único cliente como risco comercial (p. 26), e ligam o excesso de manutenção corretiva (159 contra 48 preventivas) à recomendação de reforçar a preventiva (p. 38-39). É o ciclo dado→informação→conhecimento→decisão fechando em decisão concreta, que é o que cobro nessa parte. A Tabela 2 (p. 43), consolidando a comparação dos dois SGBDs a partir da experiência real do trabalho, amarra bem.

Nota do critério: 9,0.

## Código documentado e reprodutível (peso 15%)

O que está documentado são as medidas DAX, transcritas no corpo e legíveis, mais os dois arquivos .pbix que acompanham a entrega. Não há código Python, nem SQL, nem o passo a passo reprodutível da exportação das coleções do Mongo (que foi manual no Compass), nem requirements ou README. A N1 previa psycopg2 e pymongo no procedimento, e nada disso foi executado. A reprodutibilidade fica presa a quem tem Power BI e refaz os cliques.

Nota do critério: 6,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Conexão e extração de dados | 7,0 | 25% | 1,75 |
| Qualidade das queries e análises | 7,0 | 25% | 1,75 |
| Indicadores gerados e interpretação | 9,0 | 20% | 1,80 |
| Código documentado e reprodutível | 6,5 | 15% | 0,975 |
| **Soma ponderada (85%)** | | | **6,275** |

A N2 não terá prova oral. A nota final, renormalizando os quatro critérios (85% da rubrica) para a escala de 0 a 10, é **7,4**. Com o ponto extra atribuído na N2, a nota final fica **8,4**.

Um recado para fechar: o trabalho de vocês é competente na leitura dos indicadores, mas escorrega justamente no que dá nome a ele, a comparação prática entre os dois SGBDs ficou na camada do Power BI, não no banco.
