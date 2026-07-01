# Correção N1 — Lavínia Mosquem Padilha da Silva e Odilon Ribeiro Pimentel
Data: 17/05/2026
Trabalho: POP para Acesso a Dados em Engenharia de Produção

## Fundamentação teórica (peso 30%)

Os três blocos estão cobertos e bem amarrados. A introdução constrói o argumento central com cuidado: parte da decisão em sistemas complexos (ABEPRO), passa pelos três problemas das camadas intermediárias (filtragem, defasagem temporal e agregação excessiva, com Kimball/Ross e Inmon) e fecha com o gargalo de TI a cada nova pergunta. O banco como fonte primária da verdade operacional, apoiado em Date e Elmasri/Navathe, está bem posicionado.

No SIG, gostei do tratamento da governança de TI. Vocês não pararam na definição: trouxeram o audit trail (Roratto e Dias, 2014, com DOI) e o COBIT 2019 para mostrar integridade, autoria e rastreabilidade, contrastando com a planilha compartilhada. Isso é mais do que a maioria desenvolve nesse ponto. Os dois fluxos (dado bruto → processamento → informação → conhecimento → decisão; e sensor → banco → análise → decisão → ação) materializam o pensamento sistêmico de forma concreta.

Em arquitetura, camadas, MVC com o exemplo das ordens de produção (Model = tabelas, View = tela do operador, Controller = regra de abertura) e a Clean Architecture de Martin estão corretos, com o banco tratado como detalhe de infraestrutura desacoplado. O histórico de bancos está completo: anos 60 com IMS, Codd em 1970, consolidação do SQL nos 80–90, NoSQL nos 2000 e polyglot persistence pós-2010 com Sadalage e Fowler. Relacional sob ACID e NoSQL sob BASE, com documental, colunar e chave-valor exemplificados no contexto de EP.

Nota do critério: 9,0.

## Qualidade da revisão bibliográfica (peso 20%)

Bibliografia ampla (cerca de trinta entradas) e bem distribuída: livros-texto da área (Date, Elmasri/Navathe, Heuser), fontes de SI (Oliveira, Stair/Reynolds, Turban/Sharda/Delen), referência normativa (COBIT 2019 da ISACA), um artigo com DOI (Roratto e Dias) e clássicos para sustentar a argumentação (Schwab, Simon, Davenport e Prusak). Citações em ABNT consistentes no corpo do texto. Critério bem atendido.

Nota do critério: 9,0.

## Normalização e modelagem de dados (peso 20%)

As três formas normais estão definidas corretamente, sem o erro comum de trocar 2FN por 3FN: vocês escrevem que na 2FN todo atributo não-chave depende da chave primária completa e na 3FN nenhum atributo não-chave depende de outro atributo não-chave. Os relacionamentos 1:1 (funcionário/crachá), 1:N (setor/funcionários) e N:M (produto/fornecedor com tabela associativa, citando Heuser) estão certos, e a distinção agregação (fornecedor/pedido) versus composição (ordem de produção/itens, com `ON DELETE CASCADE` no relacional e documento embutido no NoSQL) está bem feita.

O que falta aqui é o trabalho de modelagem do próprio cenário. Os exemplos são os de manual (funcionário/crachá, setor/funcionário) e não há nenhum diagrama, ER ou de classes, do cenário logístico que vocês adotam na metodologia. A teoria está sólida, mas modelagem é justamente desenhar o caso de vocês, não repetir o exemplo do livro. Para a N2 isso é obrigatório.

Nota do critério: 7,0.

## Procedimento de conexão documentado (peso 15%)

O procedimento técnico genérico está descrito (string com servidor, porta, banco, usuário e senha; execução da consulta; carregamento do resultado; encerramento da conexão), com as bibliotecas Python corretas (psycopg2, mysql-connector, pymongo) integradas ao pandas via `read_sql`, e o cuidado de não expor credenciais no código.

Dois pontos a resolver antes da N2. Primeiro, a metodologia adota o Databricks (Spark + Delta Lake) como ambiente, e Databricks não é um dos SGBDs da especificação (PostgreSQL, MySQL, MongoDB, Cassandra). Como o trabalho permite usar o banco real da empresa onde o aluno estagia, isso é defensável, mas precisa estar justificado explicitamente como ambiente corporativo de estágio, dizendo qual motor está por trás (o Delta Lake é tabular, com SQL) e mantendo o vínculo com os SGBDs vistos em aula. Segundo, falta concretude: as cinco etapas estão descritas em texto, sem string de conexão de exemplo, sem o passo a passo na ferramenta gráfica e sem o esboço do código Python. Para N1, planejar já basta; só registre que a execução reprodutível é o que será cobrado na N2.

Nota do critério: 7,0.

## Formatação ENEGEP/SBPO (peso 15%)

Template ENEGEP correto, resumo em itálico, palavras-chave, seções numeradas e referências em ABNT. O nível formal do texto é bom.

Os descontos são objetivos. As seções 4 (Resultados e Discussões) e 5 (Conclusão) estão apenas com o título, totalmente em branco. Na N1 aceito que apareçam como planejamento ou parciais, mas vazias não, escreva ao menos os resultados esperados e um fechamento. Os dois fluxos não estão numerados nem referenciados como figura no texto. E há um deslize de revisão na metodologia: "executada pelo autor", no singular, num trabalho de dupla.

Nota do critério: 7,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 9,0 | 30% | 2,70 |
| Revisão bibliográfica | 9,0 | 20% | 1,80 |
| Normalização e modelagem | 7,0 | 20% | 1,40 |
| Procedimento de conexão | 7,0 | 15% | 1,05 |
| Formatação ENEGEP/SBPO | 7,0 | 15% | 1,05 |
| **Total** | | | **8,0** |

## Para a N2

1. Desenhar o diagrama de dados do cenário real (ER no relacional e/ou de coleções), com as entidades efetivamente usadas, e aplicar 1FN/2FN/3FN sobre esse modelo, não sobre exemplos de manual.
2. Justificar o Databricks como ambiente corporativo de estágio e deixar explícita a relação com os SGBDs da disciplina.
3. Executar a conexão e as queries, com string de exemplo, passo a passo na ferramenta gráfica, código Python e prints.
4. Preencher as seções 4 (Resultados) e 5 (Conclusão) e numerar os fluxos como figuras, referenciando-os no texto.

## Prova oral

Nota: 9,5

As cinco corretas e densas: composição com o exemplo da ordem e seus itens, o audit trail, a 2FN com itens de pedido, o Databricks como lakehouse e o lugar do NoSQL no fluxo do sensor.

# Correção N2 — Lavínia Mosquem Padilha da Silva e Odilon Ribeiro Pimentel
Data: 27/06/2026
Trabalho: POP para Acesso a Dados em Engenharia de Produção

A N2 de vocês tem um mérito e tanto: foi executada sobre um cenário corporativo real, com dado de verdade da operação de frota. As seções 4 e 5 foram preenchidas, o Databricks foi justificado como ambiente de estágio e há diagrama do cenário próprio. O que segura a nota é a baixa sofisticação do SQL e o fato de o miolo analítico não estar entregue.

## Conexão e extração de dados (peso 25%)

A conexão e a extração estão evidenciadas com prints reais do Databricks (p. 10-11): a navegação Catalog → lakehouse → schema logistica, o notebook no cluster, a célula %sql com a query escrita e o resultado tabular renderizado. Mil linhas extraídas, o que comprova execução de verdade. A ressalva: não há string de conexão nem código Python, o trabalho assume que o leitor já tem acesso ao workspace, e o único Python do artigo é o exemplo genérico de psycopg2 herdado da N1, que sequer corresponde ao Databricks. O text.cmd entregue está vazio.

Nota do critério: 7,5.

## Qualidade das queries e análises (peso 25%)

Aqui está a maior fragilidade. São duas queries, e ambas são SELECT * filtrado: a primeira puxa o relatório de viagem de maio com um filtro de regional e unidade mais uma formatação de data e um cast, a segunda é uma projeção da tabela de apoio de filiais. Não há JOIN, GROUP BY nem agregação no SQL. Toda a inteligência analítica (lead time, ociosidade, quebras, a estimativa de retorno) foi feita no Power BI, em DAX/M, que não foi entregue nem mostrado. Aqui é preciso separar duas coisas: o SQL em si é trivial, mas a análise existe e é boa, só foi feita no Power BI em vez de no banco. Como o critério avalia "queries e análises", não dá para tratar como se a análise não tivesse acontecido; o desconto é por ela ter ficado fora do SQL, não por inexistir. Há ainda uma inconsistência entre as duas extrações (a regional aparece como "RG-SE/CO" numa e "RG-SUDOESTE" na outra) e um erro de aspas no nome qualificado da segunda query no arquivo, corrigido só no print.

Nota do critério: 6,5.

## Indicadores gerados e interpretação (peso 20%)

É o ponto alto. Os dois painéis (previsibilidade de retorno e utilização de frota) respondem perguntas operacionais concretas, e o fechamento do ciclo é muito bem feito: vocês ligam o dado bruto de status de viagem à informação de disponibilidade de frota e à decisão diária de quantas saídas programar, com a estimativa concreta de 39 veículos previstos para retorno, separando bem o painel operacional do histórico tático (renegociação de contrato de frota, manutenção). A modelagem dimensional em estrela com a fato Diarias_D-1 mostra entendimento acima do esperado. A ressalva: os indicadores só existem como imagem no PDF; as planilhas entregues são o output bruto das queries, não os indicadores calculados, então não há como conferir os números na fonte.

Nota do critério: 8,5.

## Código documentado e reprodutível (peso 15%)

O SQL está num arquivo à parte, legível, com cabeçalho por query. Mas não há requirements, README, notebook exportado nem o DAX/M do Power BI, que é onde mora o trabalho de fato. O pipeline de transformação (Power Query, relacionamentos, medidas, painéis) está só descrito em texto e mostrado em prints, não reproduzível a partir do que foi entregue. O text.cmd está vazio e a numeração de figuras está bagunçada (três "Figura 4" diferentes).

Nota do critério: 6,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Conexão e extração de dados | 7,5 | 25% | 1,875 |
| Qualidade das queries e análises | 6,5 | 25% | 1,625 |
| Indicadores gerados e interpretação | 8,5 | 20% | 1,70 |
| Código documentado e reprodutível | 6,0 | 15% | 0,90 |
| **Soma ponderada (85%)** | | | **6,10** |

A N2 não terá prova oral. A nota final, renormalizando os quatro critérios (85% da rubrica) para a escala de 0 a 10, é **7,2**. Com o ponto extra atribuído na N2, a nota final fica **8,2**.

O trabalho de vocês tem um cenário e uma leitura de negócio maduros; o que falta é levar parte da análise para o SQL (um GROUP BY que já entregue a contagem por status, por exemplo, em vez de trazer mil linhas e agregar no BI) e versionar as medidas do Power BI. O que faltou foi pelo menos uma query com agregação no próprio SQL e a entrega das medidas DAX do Power BI.
