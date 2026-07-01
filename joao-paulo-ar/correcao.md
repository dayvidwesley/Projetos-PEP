# Correção N1 — João Paulo Alves da Rocha
Data: 17/05/2026
Trabalho: Procedimento Operacional Padrão para Extração e Análise de Dados em Banco de Dados aplicado à Engenharia de Produção

## Fundamentação teórica (peso 30%)

A fundamentação cobre os três blocos pedidos com boa profundidade. A introdução articula a problemática com Schwab (2016) sobre Indústria 4.0, Davenport e Harris (2017) sobre organizações orientadas a dados, e Brynjolfsson (2020) sobre o diferencial competitivo da transformação de dados em conhecimento.

A seção 2.1 (SIG) traz a definição via Laudon e Laudon (2021) e faz uma distinção importante: "o SIG não se limita a um software específico, como um ERP... O ERP é apenas uma ferramenta que viabiliza o funcionamento do sistema de informação, enquanto o SIG corresponde ao processo mais amplo". Essa diferenciação é um cuidado conceitual que muitos trabalhos não fazem. A Figura 1 (Processo SIG) com Entrada → Processamento → Saída → Feedback ilustra bem o fluxo.

A seção 2.2 (Arquitetura) traz MVC com Bass/Clements/Kazman e a Figura 2 visual do padrão. Discute também a arquitetura em camadas (interface, lógica, BD) e fecha com a observação correta de que "o acesso direto ao banco de dados torna-se uma prática estratégica para o engenheiro de produção".

A seção 2.3 (Banco de Dados) tem o histórico mais detalhado de tudo no trabalho: anos 50 com armazenamento em papel (Figura 3), arquivos sequenciais, discos magnéticos, anos 60 com modelos hierárquicos e em rede no contexto do CODASYL, 1970 com Codd e o modelo relacional (citado em fonte primária), padronização do SQL, 2000 com NoSQL, ACID e BASE com siglas expandidas em português (Basicamente Disponível, Estado Suave, Eventualmente Consistente), Sadalage e Fowler 2013, e polyglot persistence com Fowler 2012 primário. A menção ao CODASYL é diferencial — poucos trabalhos sobre BD trazem essa referência histórica.

Lacunas a corrigir:

- A seção 2.2 fica em MVC e camadas. Falta Clean Architecture (Martin) e arquitetura hexagonal (Cockburn), que aprofundariam o argumento do BD como detalhe de infraestrutura.
- A classificação clássica em SPT/SIG/SAD/SAE (tipos de sistema de informação) não aparece.
- O ciclo dado→informação→conhecimento→decisão é mencionado mas sem o quarto estágio (decisão) ganhar destaque próprio.

Nota do critério: 8,5.

## Qualidade da revisão bibliográfica (peso 20%)

A lista de referências contém dez entradas pertinentes: Bass/Clements/Kazman (2021), Codd (1970) em fonte primária, Date (2004), Elmasri e Navathe (2018), Fowler (2012), Laudon e Laudon (2021), Pressman e Maxim (2020), Sadalage e Fowler (2013), Senge (2017) com "A Quinta Disciplina" e Turban et al. (2020).

Três problemas a corrigir:

- **Citações no texto sem entrada bibliográfica**: Schwab (2016) citado na introdução, Brynjolfsson (2020) citado na introdução e Davenport e Harris (2017) citado na introdução não aparecem na lista de referências. Toda citação no texto exige entrada correspondente.

- **Fontes das imagens em canais educacionais**: Figuras 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 e 12 são atribuídas a "Alura (2026)", "Curso em Vídeo (2016)", "Aula em Vídeo (2016)", "Hashtag Programação (2022/2023/2026)". Para um artigo ENEGEP, fontes de canais de YouTube ou cursos pagos online são inadequadas — substituir por figuras próprias (especialmente os exemplos de formas normais) ou por figuras extraídas dos livros já citados na bibliografia (Date, Elmasri e Navathe, Silberschatz).

- Faltam referências clássicas para arquitetura: Cockburn (Hexagonal) e Martin (Clean Architecture).

Nota do critério: 6,5.

## Normalização e modelagem de dados (peso 20%)

As três formas normais aparecem definidas tecnicamente e ilustradas com **tabelas exemplo** (Figuras 9, 10 e 11):

- 1FN com a tabela PESSOA decomposta em PESSOA + TELEFONE para eliminar atributo multivalorado
- 2FN com o caso da chave composta `(id_func, id_proj)` decomposta em FUNCIONARIO, FUNCIONARIO_PROJETO e PROJETO para eliminar dependência parcial — exemplo tecnicamente correto
- 3FN com FUNCIONARIO decomposto em FUNCIONARIO + DEPARTAMENTO eliminando dependência transitiva

A Figura 8 mostra a estrutura hierárquica das formas normais (1FN → 2FN → 3FN → BCNF → 4FN → 5FN), o que dá uma visão geral útil.

Pontos a corrigir:

- A seção 2.6 (Agregação e Composição no MER) usa "agregação" no sentido do MER estendido de Chen — quando um relacionamento é tratado como entidade de nível superior, ilustrado pela Figura 12 (Cliente-compra-Produto, onde "compra" vira entidade intermediária). Esse é um sentido válido em modelagem MER, mas distinto do conceito UML/orientado a objetos de agregação, onde "agregação" significa "tem um" com partes independentes (Fornecedor/Pedido) e "composição" significa "parte de" com dependência forte (Ordem/Itens). O roteiro do trabalho pede o sentido UML. Vale unificar a terminologia.

- A composição está corretamente exemplificada (ordem de produção composta por etapas que não existem sem ela).

- Não há diagrama ER próprio do cenário que será analisado. As Figuras 9-11 são exemplos genéricos (PESSOA, FUNCIONARIO, DEPARTAMENTO).

- Os relacionamentos 1:1, 1:N e N:M não recebem seção própria (a Figura 12 mostra um N:N implicitamente, mas sem discussão sistemática).

Nota do critério: 7,5.

## Procedimento de conexão documentado (peso 15%)

A seção 2.7 ("Aplicação prática usando SQL Server e Python") apresenta a escolha do SQL Server como SGBD e Python com a biblioteca `pyodbc` como ambiente de conexão e análise. A Figura 13 lista as três bibliotecas (`pyodbc`, `pandas`, `openpyxl`) e a Figura 14 mostra o esqueleto do código de conexão com placeholders para DRIVER, SERVER, DATABASE, UID e PWD.

A discussão menciona consulta em SQL, organização e tratamento via pandas, exportação para Excel/CSV para uso em dashboards e indicadores gerenciais.

O que falta para fechar o critério com nota cheia:

- A empresa onde o SQL Server seria aplicado não é caracterizada em nenhum lugar do artigo. "Pertencente ao ambiente industrial da empresa" — qual empresa? Que tipo de operação industrial?
- Não há exemplo de query SQL real (um `SELECT` típico de Engenharia de Produção, com `JOIN` entre tabelas).
- Não há resultado do cursor ou exemplo de DataFrame produzido.
- Não há tratamento das credenciais (variáveis de ambiente, .env, cofre de segredos) — a Figura 14 deixa os campos como placeholders mas sem indicar boas práticas de segurança.

Vale também observar que a escolha do SQL Server, embora válida como SGBD relacional, fica fora do conjunto privilegiado pelo roteiro do trabalho (PostgreSQL, MySQL, MongoDB, Cassandra). O SQL Server pode ser mantido se houver justificativa concreta de uso na empresa, mas isso precisa ficar explícito.

Nota do critério: 7,5.

## Formatação ENEGEP/SBPO (peso 15%)

Template ENEGEP oficial usado, cabeçalho do XLV ENEGEP, palavras-chave, figuras numeradas com fonte, referências em ABNT.

Pontos a corrigir:

- O título começa com "(" e termina com ")" — abrir e fechar parênteses ao redor de todo o título é formato estranho que precisa ser ajustado.
- O resumo não está em itálico — o padrão ENEGEP exige itálico para o resumo.
- Faltam seções estruturais centrais: **3. Metodologia**, **4. Resultados** e **5. Conclusão/Considerações Finais**. O artigo termina em 2.7 e vai direto para as Referências. A "aplicação prática" da 2.7 cumpre parcialmente o papel de Metodologia, mas a forma correta é numerá-la como seção 3 e adicionar Resultados (mesmo que como planejamento da N2) e Conclusão.

Nota do critério: 6,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 8,5 | 30% | 2,55 |
| Revisão bibliográfica | 6,5 | 20% | 1,30 |
| Normalização e modelagem | 7,5 | 20% | 1,50 |
| Procedimento de conexão | 7,5 | 15% | 1,125 |
| Formatação ENEGEP/SBPO | 6,5 | 15% | 0,975 |
| **Total** | | | **7,5** |

## Para a N2

Cinco frentes a endereçar:

1. Incluir Schwab (2016), Brynjolfsson (2020) e Davenport e Harris (2017) na lista de referências (estão citados no texto) e adicionar Cockburn e Martin para a discussão de arquitetura.
2. Substituir as figuras atualmente atribuídas a Hashtag Programação, Curso em Vídeo, Aula em Vídeo e Alura por figuras de elaboração própria (especialmente os exemplos de formas normais, que são exemplos didáticos comuns) ou por figuras extraídas dos livros de Date, Elmasri e Navathe, ou Silberschatz já citados.
3. Unificar a terminologia de agregação e composição na seção 2.6 no sentido UML/modelagem orientada a objetos (parte/todo, dependência de existência), conforme o roteiro do trabalho pede.
4. Caracterizar a empresa onde o SQL Server será aplicado, mostrar um diagrama ER do banco real e incluir pelo menos uma query SQL típica de Engenharia de Produção com seu DataFrame resultante.
5. Reorganizar o artigo com a estrutura ENEGEP completa: 1 Introdução, 2 Fundamentação Teórica, 3 Metodologia, 4 Resultados (esperados para a N1, executados na N2), 5 Considerações Finais, Referências. Ajustar o título removendo os parênteses e colocar o resumo em itálico.

## Prova oral

Nota: 9,0

Respostas corretas: agregação no MER frente à UML, o papel do CODASYL, o teorema CAP, as arquiteturas hexagonal e Clean, e a conexão com pyodbc dentro do ciclo do dado até a decisão.

# Correção N2 — João Paulo Alves da Rocha
Data: 27/06/2026
Trabalho: Procedimento Operacional Padrão para Extração e Análise de Dados em Banco de Dados aplicado à Engenharia de Produção

Você endereçou a maioria das frentes da N1: a estrutura ENEGEP está completa, as figuras foram em boa parte reatribuídas a elaboração própria, a terminologia de agregação e composição foi esclarecida (separando o sentido MER do UML) e a empresa foi caracterizada (embalagens flexíveis). A conexão e a extração saíram do papel. O que limita a N2 é a profundidade da exploração e da análise, que ficou presa a uma única tabela.

## Conexão e extração de dados (peso 25%)

A conexão é real e está comprovada: pyodbc com driver ODBC 18 sobre SQL Server, Trusted_Connection, e o print da Figura 16 mais a validação no SSMS (Figuras 13-15). É reprodutível em máquina com a instância, e o uso de autenticação Windows evita expor senha, o que é bom. Duas ressalvas: o banco se chama SANKHYA_MOCKUP, ou seja, é um mockup, enquanto o texto (p. 23) afirma ser a base usada pela empresa, e a extração inteira roda sobre uma única tabela (AD_PCPCEN), o que esvazia a etapa "Explorar" do POP, que pede o reconhecimento do modelo de dados, não de uma tabela só. Mas, como etapa de conexão, está bem servida: conexão real e reprodutível, prints do SSMS e do Python, exploração da tabela e recorte de período correto.

Nota do critério: 8,0.

## Qualidade das queries e análises (peso 25%)

A query de KPIs é boa: agregação condicional com CASE WHEN e LIKE, COUNT(DISTINCT), NULLIF para evitar divisão por zero e a derivação de monocamada por subtração (Figura 18). Mostra domínio de SQL acima do trivial. O problema é que nenhuma consulta usa JOIN, todas leem só a AD_PCPCEN. Isso é exatamente o oposto do que o trabalho defende na teoria, que o diferencial do banco relacional é integrar tabelas. As outras duas queries (Top 5 e tiragem por semana) são simples. Faltou cruzar tabelas, que é onde a extração relacional mostra valor. Há ainda um dado não tratado: a coluna SALDO_TIRAGEM aparece com valores fortemente negativos no SELECT *, sem nenhum comentário.

Nota do critério: 6,5.

## Indicadores gerados e interpretação (peso 20%)

Os indicadores estão lá, com gráficos: seis KPIs em cartões, a rosca de distribuição das OPs, a tiragem por semana e a tabela Top 5 (Figuras 20-23). A leitura conecta a tiragem semanal a PCP, balanceamento de carga e programação de máquinas. Mas o fechamento do ciclo fica genérico: a seção 4.5 e a conclusão afirmam o ciclo dado→informação→conhecimento→decisão sem aterrissar numa decisão concreta tirada dos números ("a semana 19 concentrou tal volume, logo realoco tal recurso"). A interpretação descreve o que cada KPI representa mais do que extrai uma ação.

Nota do critério: 6,5.

## Código documentado e reprodutível (peso 15%)

O notebook foi executado, com saídas e comentários por bloco. Pesa contra: ele guarda três versões do dashboard (duas em plotly e a final em HTML), resíduo que deveria ter sido limpo; as queries são montadas por f-string interpolando as datas direto no SQL, em vez de parâmetros (aqui o risco é baixo, mas é prática a evitar); não há requirements nem README; e o ConsultaSQL.json, apesar do nome, não tem SQL nenhum, é um descritor de layout do dashboard, e ainda descreve um gráfico ("tiragem_diaria") que não bate com o semanal entregue. Resíduos da N1 também ficaram: a Figura 10 segue creditada a um canal, Cockburn e Martin são citados no texto mas não constam nas referências, e o título permanece entre aspas. Ainda assim, o código roda, está comentado por blocos e o artigo documenta cada etapa, o que sustenta a reprodução.

Nota do critério: 7,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Conexão e extração de dados | 8,0 | 25% | 2,00 |
| Qualidade das queries e análises | 6,5 | 25% | 1,625 |
| Indicadores gerados e interpretação | 6,5 | 20% | 1,30 |
| Código documentado e reprodutível | 7,0 | 15% | 1,05 |
| **Soma ponderada (85%)** | | | **5,975** |

A N2 não terá prova oral. A nota final, renormalizando os quatro critérios (85% da rubrica) para a escala de 0 a 10, é **7,0**. Com o ponto extra atribuído na N2, a nota final fica **8,0**.

O ponto que faltou é a integração entre tabelas: uma query com JOIN respondendo uma pergunta de PCP, e uma decisão concreta saindo de um número. É o que faria o trabalho fazer jus à fundamentação que você escreveu.
