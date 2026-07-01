# Correção N1 — Guilherme Alves e Vinycius Cirilo
Data: 16/05/2026
Trabalho: Procedimento Operacional Padrão para extração e análise de dados diretamente em bancos de dados relacionais e documentais em contextos de Engenharia de Produção

## Fundamentação teórica (peso 30%)

A fundamentação é muito sólida e articulada. A introdução abre com uma argumentação afiada: três limitações concretas do dado intermediado (filtrado, atrasado, agregado) que justificam o acesso direto ao banco como competência analítica do engenheiro. Esse tipo de problematização funciona melhor do que listas genéricas de Indústria 4.0.

A seção 2.1 traz Laudon para a definição de SIG, situa ERP/MES/WMS/BI como materializações, articula o pensamento sistêmico (sistemas abertos com retroalimentação) e fecha com o ciclo dado→informação→conhecimento→decisão ancorado em Davenport e Prusak (referência primária do livro "Working Knowledge"). A menção à governança de TI também aparece, o que poucos trabalhos da turma fazem.

A seção 2.2 articula bem camadas, MVC, hexagonal (Cockburn como referência primária) e Clean Architecture (Martin), e amarra o argumento de que o acesso analítico direto ao BD é arquiteturalmente legítimo porque opera na camada de infraestrutura sem violar as superiores.

A seção 2.3 traz o histórico do banco de dados completo: 1960 com IMS hierárquico, Codd em 1970 em fonte primária, 1980-1990 com Oracle/DB2/PostgreSQL/MySQL e SQL como padrão, ACID detalhada (todas as quatro propriedades), 2000s com o movimento NoSQL e suas quatro famílias (documentais, colunas, chave-valor, grafos), 2010+ com polyglot persistence (Fowler e Sadalage primária). É a apresentação histórica mais completa que se pode pedir nesse nível.

A seção 2.4 (Tabela 1) compara relacional e documental em sete aspectos (incluindo ACID vs BASE, escalabilidade vertical vs horizontal, padrão de linguagem) e fecha com a observação crucial de que "a escolha entre os dois paradigmas raramente é binária".

Nota do critério: 9,5.

## Qualidade da revisão bibliográfica (peso 20%)

Oito referências, com presença de fontes primárias no lugar certo: Codd 1970 ("A Relational Model of Data for Large Shared Data Banks"), Cockburn 2005 (origem da arquitetura hexagonal), Davenport e Prusak 1998 ("Working Knowledge"), Fowler e Sadalage 2012 ("NoSQL Distilled"), Martin 2017 (Clean Architecture), Elmasri e Navathe 2018 (clássico de BD), Laudon e Laudon 2014. ABNT consistente.

Dois pontos a observar:

- O número de referências é modesto (8), o que limita a triangulação argumentativa. Vale ampliar com pelo menos Date para BD e Sommerville ou Bass/Clements/Kazman para arquitetura.
- A entrada "MARTINS, D. W. P. Material didático da disciplina" cita o próprio professor. Não é problema acadêmico em si, mas em um artigo ENEGEP a referência precisaria estar publicamente disponível. Substituir por citações diretas aos autores que o material referencia.

Nota do critério: 8,0.

## Normalização e modelagem de dados (peso 20%)

Esse é o ponto mais forte do trabalho. As três formas normais aparecem definidas com terminologia técnica correta e exemplos do contexto industrial:

- 1FN com o exemplo do campo "componentes" contendo "rolamento; eixo; mola" e a necessidade de decompô-lo.
- **2FN com o exemplo da tabela "itens_ordem" com chave composta `(ordem_id, item_id)` e o nome do produto dependendo apenas de item_id**. Esse é tecnicamente o conceito correto — a 2FN ataca dependência parcial em chaves compostas — e o exemplo é claro.
- 3FN com a tabela "funcionários" e o campo nome_setor dependendo de setor_id (dependência transitiva).

A Tabela 2 sintetiza as cardinalidades 1:1, 1:N e N:M com exemplos em Engenharia de Produção (Funcionário/Crachá, Setor/Funcionários, Produto/Fornecedor) e a implementação concreta (FK UNIQUE, FK simples, tabela associativa).

A seção 2.6 (agregação e composição) está exemplar: definição UML, exemplos no contexto industrial (Fornecedor/Pedido como agregação, Ordem de Produção/Itens como composição), tradução em SQL com `ON DELETE CASCADE` e em MongoDB com documento embutido versus referência por ObjectId. O fechamento — "a distinção não é meramente teórica: ela orienta decisões concretas de modelagem que afetam o desempenho das consultas, a complexidade das regras de integridade e a robustez do procedimento de extração" — articula perfeitamente teoria e prática.

Falta apenas o diagrama ER próprio, mas como o dataset será fornecido pelo professor na N2, esse diagrama será construído lá.

Nota do critério: 9,5.

## Procedimento de conexão documentado (peso 15%)

Outro ponto muito bem servido. A Tabela 3 lista as ferramentas com versões específicas (PostgreSQL 16, MongoDB 7) e a função de cada uma no procedimento. As Figuras 1 e 2 trazem código Python real e executável:

- Figura 1: `psycopg2.connect` com os cinco parâmetros (host, port, dbname, user, password), uma query SQL completa com `COUNT(*)`, `AVG(tempo_ciclo)`, `GROUP BY linha`, `ORDER BY tempo_medio DESC`, leitura por `pd.read_sql` e fechamento explícito da conexão.
- Figura 2: `MongoClient`, pipeline com `$match`, `$group`, `$sort`, conversão para DataFrame e fechamento. O pipeline é funcionalmente equivalente à query SQL — o que vocês destacam acertadamente como propriedade importante para o engenheiro analítico.

A Tabela 4 organiza o POP em cinco etapas (Conectar, Explorar, Extrair, Analisar, Interpretar) com evidências esperadas para a N2.

A seção 3.4 (Considerações sobre segurança e governança) traz três princípios concretos: usuário read-only com permissão SELECT/find, credenciais fora do código versionado (variáveis de ambiente ou cofres de segredos), e anonimização de dados pessoais por LGPD. Esse nível de cuidado com governança eleva o critério.

O que falta para a nota cheia é apenas a execução real — o procedimento ainda não foi rodado sobre um dataset, mas isso é exatamente o escopo da N2.

Nota do critério: 9,5.

## Formatação ENEGEP/SBPO (peso 15%)

O trabalho está bem cuidado no nível de formatação acadêmica geral: resumo em itálico, palavras-chave, seções numeradas, tabelas e figuras numeradas com fonte indicada, referências em ABNT, blocos de código bem destacados.

Porém, o template usado **não é o template ENEGEP/SBPO oficial**. O cabeçalho do artigo é "FACULDADE DE CIÊNCIAS E TECNOLOGIA – CÂMPUS APARECIDA DE GOIÂNIA" com numeração de páginas "N de 9", em formato de trabalho acadêmico genérico. O template ENEGEP exige o cabeçalho próprio do encontro (logo, edição, local e data), bordas e fontes específicas. Como o trabalho será apresentado em formato ENEGEP no encontro, é importante migrar para o template oficial na próxima versão.

Outros pequenos ajustes:

- "Elaborada pelo autor" aparece no singular nas Tabelas 2 e 3, embora a autoria seja em dupla. Padronizar para "pelos autores".
- Não há seção 4 de Resultados separada (vai direto para "4. Considerações Finais"). Como na N1 essa seção pode aparecer parcial ou como planejamento, e a Tabela 4 já lista as evidências esperadas, considerem nomear como "4. Resultados Esperados" e mover as Considerações Finais para a seção 5.

Nota do critério: 7,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 9,5 | 30% | 2,85 |
| Revisão bibliográfica | 8,0 | 20% | 1,60 |
| Normalização e modelagem | 9,5 | 20% | 1,90 |
| Procedimento de conexão | 9,5 | 15% | 1,425 |
| Formatação ENEGEP/SBPO | 7,0 | 15% | 1,05 |
| **Total** | | | **8,8** |

## Para a N2

Quatro frentes:

1. Migrar o artigo para o template ENEGEP/SBPO oficial (cabeçalho do encontro, fontes e bordas conforme exigência) e reorganizar a numeração para incluir uma seção 4 de Resultados Esperados separada das Considerações Finais.
2. Ampliar a bibliografia com pelo menos Date (BD), Sommerville ou Bass/Clements/Kazman (arquitetura), e substituir a citação ao material didático por referências diretas aos autores que ele baseia.
3. Executar o procedimento sobre o dataset fornecido: gerar a captura de tela da conexão estabelecida, construir o diagrama do modelo de dados (ER no PostgreSQL e diagrama de coleções no MongoDB), e produzir os indicadores propostos com pandas/matplotlib.
4. Adicionar um exemplo prático do carregamento das credenciais via `os.environ` ou `python-dotenv`, materializando a recomendação de governança da seção 3.4.

## Prova oral

Nota: 9,5

As cinco corretas e densas: BASE com o teorema CAP, a quebra da equivalência entre GROUP BY e $group quando há junções profundas, CASCADE frente a RESTRICT e SET NULL, a integração orientada a eventos entre os bancos e a diferença entre variável de ambiente e cofre de segredos.

# Correção N2 — Guilherme Alves e Vinycius Cirilo
Data: 27/06/2026
Trabalho: Procedimento Operacional Padrão para extração e análise de dados diretamente em bancos de dados relacionais e documentais em contextos de Engenharia de Produção

Esse é um trabalho muito bem executado. A migração para o template ENEGEP foi feita, as seções 4 e 5 estão completas, e o que mais me agrada é que dá para confiar na execução: os números do indicadores_resumo.json e dos CSVs batem exatamente com as tabelas do PDF, o que prova que o pipeline rodou de verdade sobre os dois bancos.

## Conexão e extração de dados (peso 25%)

A conexão está modularizada em conexao.py, com engine_postgres() (SQLAlchemy sobre psycopg2) e cliente_mongo() (pymongo), credenciais por variável de ambiente, com env.example e README documentando. O run_pop.py orquestra as cinco etapas e imprime o log de conexão dos dois bancos. É reprodutível de ponta a ponta, e o cuidado com governança de credenciais que cobrei na N1 está atendido. A única coisa que falta para o topo é o print de tela da conexão: a rubrica pede print, e vocês substituíram por log textual. É evidência mais fraca que uma captura, embora aqui o conjunto compense.

Nota do critério: 8,5.

## Qualidade das queries e análises (peso 25%)

SQL e pipelines de alto nível. No ERP, o faturamento por produto tem quatro JOINs com cálculo de margem e desconto; há CTE no previsão × real, agregação temporal com to_char, LEFT JOIN com COALESCE na aderência do plano. No MES, o $unwind sobre o array embutido de paradas materializa na prática o conceito de composição da N1, e os pipelines de OEE e refugo estão corretos. Só um deslize real: na query de compras por fornecedor o WHERE tem "... OR c.status IS NOT NULL", que anula os filtros anteriores e torna o critério trivial (e esse indicador acaba nem aparecendo no artigo). Fora isso, as queries exercitam de propósito os conceitos que cobrei, é bom de ver.

Nota do critério: 8,5.

## Indicadores gerados e interpretação (peso 20%)

Cobertura completa e madura: OEE global e por máquina decomposto em D×P×Q, MTBF/MTTR, Pareto das paradas pelas Seis Grandes Perdas, refugo/FPY, curva ABC, MAPE da previsão e um indicador cross-database de aderência (plano no Postgres × peças boas no Mongo). A interpretação fecha em decisão concreta em cada um: TPM e SMED na Montagem 01 e no Torno CNC 02 (identificado como gargalo pelo OEE de 72,9%), atacar as paradas organizacionais e não as quebras (conclusão que vocês sustentam cruzando MTBF alto com o Pareto), recalibrar a previsão pelo viés positivo do MAPE, proteger a disponibilidade dos itens classe A. Esse cruzamento MTBF × Pareto para concluir que a perda é organizacional é análise de gente que entendeu o dado.

Nota do critério: 9,0.

## Código documentado e reprodutível (peso 15%)

Critério muito bem servido. Pacote pop/ separado por etapa, docstrings ligando cada função à etapa do POP e ao conceito da N1, requirements.txt e README completos, env.example, e dois caminhos de execução (notebook didático e CLI). As saídas são determinísticas e conferem com o artigo. Deslizes menores: o README cita arquivos (construir_notebook.py, gerar_artigo.py) que não estão na pasta entregue e usa nomes de diretório diferentes dos reais, e o cabeçalho interno das páginas ainda diz "XLV ENEGEP Natal 2025" enquanto a capa traz "XLVI São Paulo 2026". Não comprometem a execução.

Nota do critério: 9,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Conexão e extração de dados | 8,5 | 25% | 2,125 |
| Qualidade das queries e análises | 8,5 | 25% | 2,125 |
| Indicadores gerados e interpretação | 9,0 | 20% | 1,80 |
| Código documentado e reprodutível | 9,0 | 15% | 1,35 |
| **Soma ponderada (85%)** | | | **7,40** |

A N2 não terá prova oral. A nota final, renormalizando os quatro critérios (85% da rubrica) para a escala de 0 a 10, é **8,7**. Com o ponto extra atribuído na N2, a nota final fica **9,7**.

Faltou só o diagrama do modelo de dados (a exploração ficou textual) e a ampliação da bibliografia que pedi na N1, que não veio. São os dois pontos que ficaram de fora, mas o trabalho prático está num nível alto.
