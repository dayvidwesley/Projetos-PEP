# Correção N1 — Gabriel Campos e Rafael Campos
Data: 16/05/2026
Trabalho: Procedimento Operacional Padrão para Conexão com Bancos de Dados PostgreSQL e MongoDB

## Fundamentação teórica (peso 30%)

A fundamentação é extensa e organizada em seis subseções, cobrindo todos os blocos pedidos com autores de referência: Laudon e Stair para SIG, Sommerville e Pressman/Maxim para arquitetura, Fowler para padrões em camadas, Freeman e Robson para MVC, Martin para Clean Architecture, e em banco de dados a base é forte com Codd em fonte primária (1970), Elmasri e Navathe, Silberschatz/Korth/Sudarshan, Date, Connolly e Begg, Sadalage e Fowler, Banker e Chodorow. Inclui ainda o teorema CAP de Brewer (2012), Slack para administração da produção e Kagermann para Indústria 4.0.

O histórico do banco de dados (2.3) está completo, desde os modelos hierárquicos dos anos 60 (IMS), passando por Codd em 1970, consolidação do SQL entre 80 e 90, ascensão do NoSQL nos anos 2000 e polyglot persistence a partir de 2010. A discussão de ACID em 2.4 traz Connolly e Begg, e a contraposição BASE com Brewer (referência primária do teorema CAP) é um diferencial conceitual importante.

A seção 2.6 (agregações e composições) está muito bem feita: vocês trazem Booch, Rumbaugh e Jacobson como referência primária de UML, distinguem corretamente "tem um" de "parte de", citam o `ON DELETE CASCADE` como implementação concreta da composição em SQL e a referência por ObjectId em NoSQL. Esse nível de articulação é o que a rubrica espera no topo do critério.

O que pesa contra: o ciclo dado→informação→conhecimento→decisão aparece muito tímido em 2.1 (uma única menção a Stair/Reynolds sobre conhecimento) e sem exemplo concreto. A classificação dos sistemas em SPT/SIG/SAD/SAE não aparece. E a fundamentação, embora rica, fica descolada de um cenário próprio — o trabalho é genérico, sem aplicação a uma empresa ou caso real, o que vai limitar a Normalização e a Conexão.

Nota do critério: 9,0.

## Qualidade da revisão bibliográfica (peso 20%)

Vinte e sete referências, com os clássicos da área no lugar certo: Codd 1970 em fonte primária, Booch/Rumbaugh/Jacobson, Brewer 2012 para CAP, Elmasri/Navathe, Silberschatz/Korth/Sudarshan, Date, Connolly/Begg, Coronel/Morris, Sadalage/Fowler, Sommerville, Pressman/Maxim, Martin, McKinney para pandas, Chiavenato para administração, Slack para operações, Kagermann para Indústria 4.0. Documentação oficial do PostgreSQL, MongoDB e psycopg também aparece. ABNT consistente.

Esse é o critério mais forte do trabalho.

Nota do critério: 9,5.

## Normalização e modelagem de dados (peso 20%)

As três formas normais estão definidas com terminologia técnica adequada — e a 2FN merece destaque: vocês citam explicitamente "chaves compostas" e "dependências parciais", o que é o conceito correto. Os relacionamentos 1:1, 1:N e N:M aparecem com exemplos. Agregação e composição estão bem distinguidas, com a tradução em SQL (FK + JOIN) e NoSQL (referência por ObjectId), e a menção ao `ON DELETE CASCADE` para composição é ponto a favor.

O que pesa contra é a ausência de aplicação ao próprio caso: a 2FN não tem exemplo, a 3FN tem um exemplo genérico ("informações de fornecedores em tabelas de produtos"), e não há diagrama ER. Como o trabalho de vocês é um POP genérico de instalação e conexão (sem cenário específico de empresa), essa fragilidade na aplicação é estrutural. Na N2, com a base de dados fornecida, vocês precisam construir o diagrama do próprio modelo.

Nota do critério: 8,0.

## Procedimento de conexão documentado (peso 15%)

A documentação dos procedimentos de instalação e conexão está muito bem feita. Dezoito figuras com prints reais cobrem o download do PostgreSQL, a instalação com criação da senha do usuário `postgres`, a porta 5432, o cadastro do servidor no pgAdmin com todos os parâmetros (host, port, maintenance database, username, password), a instalação do Python com "Add Python to PATH", o `pip install psycopg2`, o `pip install pandas`, depois MongoDB com download, instalação como serviço, MongoDB Compass com a URI `mongodb://localhost:27017/`, e os comandos `pip install pymongo` e `pandas`. Alguém com pouca experiência consegue reproduzir o procedimento sem dúvidas. Esse é exatamente o sentido de um POP.

Ressalvas: o procedimento documenta até a "porta de entrada" — instalação e cadastro do servidor. Falta o passo seguinte, que é o código Python efetivamente executando a conexão e uma query: `psycopg2.connect(host=..., port=5432, ...)` retornando um cursor e rodando um `SELECT`, ou `MongoClient("mongodb://localhost:27017")` listando uma coleção. Sem esse fechamento, o procedimento mostra que vocês conseguem instalar e configurar, mas não que extraem dados ainda. Esse adensamento será cobrado na N2.

Outro ponto a observar: a Figura 9 (prompt de comando) reaparece como Figura 16, e a instalação do psycopg2 também é mostrada duas vezes (Figura 10 e Figura 17 são quase idênticas). Convém revisar a numeração e remover repetições.

Nota do critério: 9,0.

## Formatação ENEGEP/SBPO (peso 15%)

Template oficial, cabeçalho, resumo, palavras-chave, seções numeradas, dezoito figuras numeradas com fonte indicada, referências em ABNT bem cuidadas. A base formal está atendida.

Pontos a ajustar:

- O resumo no início do artigo aparece sem o itálico padrão ENEGEP.
- A "Fonte: Elaborado pelo autor" aparece no singular em várias figuras, embora a autoria seja em dupla. Padronizar para "pelos autores".
- Figuras repetidas (9/16 e 10/17, como comentado acima) inflam o trabalho desnecessariamente.
- Falta seção 4 de Resultados Esperados separada das Considerações Finais. As "Considerações finais" foram numeradas como seção 4 mas funcionam como conclusão.
- O artigo não tem nenhum quadro ou tabela. Uma tabela comparativa entre PostgreSQL e MongoDB (esquema, transações, escala, casos de uso) faria muito bem ao texto e está dentro do padrão ENEGEP.

Nota do critério: 7,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 9,0 | 30% | 2,70 |
| Revisão bibliográfica | 9,5 | 20% | 1,90 |
| Normalização e modelagem | 8,0 | 20% | 1,60 |
| Procedimento de conexão | 9,0 | 15% | 1,35 |
| Formatação ENEGEP/SBPO | 7,5 | 15% | 1,125 |
| **Total** | | | **8,7** |

## Para a N2

Quatro frentes a endereçar:

1. Adensar o procedimento com o código Python efetivamente conectando e rodando uma query simples em cada SGBD (psycopg2 e pymongo).
2. Construir o diagrama ER da base de dados fornecida e aplicar 1FN/2FN/3FN com exemplos desse modelo, marcando também agregação e composição visualmente.
3. Adicionar uma seção 4 de Resultados Esperados (ou pelo menos um quadro de indicadores planejados) antes das Considerações Finais.
4. Limpar a numeração de figuras repetidas, padronizar "pelos autores" e incluir ao menos um quadro comparativo PostgreSQL × MongoDB.

## Prova oral

Nota: 9,0

Respostas corretas: ciclo ilustrado com SQL, o teorema CAP justificando o BASE, o nome_produto violando a 2FN, CASCADE frente a RESTRICT e SET NULL, e a diferença entre MVC e Clean Architecture.

# Correção N2 — Gabriel Campos e Rafael Campos
Data: 27/06/2026
Trabalho: Procedimento Operacional Padrão para Conexão com Bancos de Dados PostgreSQL e MongoDB

A N2 de vocês explora de verdade os dois bancos fornecidos e endereça a frente central que apontei na N1, a modelagem do cenário real. O artigo cresceu para 52 páginas, e as seções 6 e 7 (indicadores ERP e MES) e a 8 (Considerações Finais) estão cheias e robustas.

## Conexão e extração de dados (peso 25%)

A conexão está bem documentada nos dois SGBDs, com prints reais: pgAdmin no Postgres remoto (Figuras 19-20, p. 25-26) e mongosh/Compass no Mongo (Figura 22, p. 28). Gostei especialmente da exploração por catálogo, vocês consultam information_schema.columns filtrando o schema erp (Figura 21) e usam getCollectionNames/findOne/countDocuments no Mongo. É a etapa "Explorar" feita com método. A ressalva: tudo foi feito por ferramenta gráfica, e o texto da p. 34 chama isso de "conexão programática estabelecida na seção 4.1", o que não confere, porque não há código psycopg2 ou pymongo em lugar nenhum. A N1 pedia esse código.

Nota do critério: 8,0.

## Qualidade das queries e análises (peso 25%)

Ponto mais forte do trabalho. São 13 indicadores, 7 consultas SQL no ERP e 6 pipelines no MES. No SQL há JOINs triplos de verdade (faturamento por cliente cruzando pedido_venda, cliente e item_pedido, Figura 27; custo por fornecedor, Figura 28; aderência plano × previsão, Figura 30; DRE reconstruída por grupo, Figura 31). No Mongo, o uso de $unwind sobre o array embutido de paradas (Figura 33) é o trecho tecnicamente mais bonito, porque ataca a natureza documental do dado, e vocês ainda validam o resultado cruzando a soma do tempo parado entre os Indicadores 8 e 9. As poucas queries triviais (status que retornou um único valor) foram honestamente justificadas como limite da base, não erro de vocês.

Nota do critério: 8,5.

## Indicadores gerados e interpretação (peso 20%)

Os 13 indicadores estão sintetizados nas Tabelas 2 e 3, e a Tabela 2 traz uma coluna de "Implicação Gerencial" que é exatamente o fechamento que cobro: estoque de segurança fixo em 50% que precisa ser refinado por lead time e criticidade, Pareto de clientes apontando retenção, corretiva mais cara justificando ampliar a preventiva, paradas de setup pedindo SMED. Decisão concreta em cima de cada número. O que segura a nota é a forma: todos os indicadores são tabelas e saídas de console, não há um gráfico sequer, e a rubrica da N2 pede tabelas e gráficos. Um Pareto e uma curva ABC plotados dariam muito mais força à leitura.

Nota do critério: 7,5.

## Código documentado e reprodutível (peso 15%)

O SQL e os pipelines estão todos visíveis como texto/print e são reproduzíveis manualmente. Mas não há script Python, requirements ou README na pasta N2, só o PDF (o N2.md está vazio). As bibliotecas que a metodologia declara (psycopg2, pymongo, pandas) não chegam a aparecer em código, pandas nunca é usado. A Figura 16 ainda repete a Figura 9, resíduo da N1 que não foi limpo. Reproduzir o trabalho hoje exige refazer tudo nas ferramentas gráficas, na mão.

Nota do critério: 6,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Conexão e extração de dados | 8,0 | 25% | 2,00 |
| Qualidade das queries e análises | 8,5 | 25% | 2,125 |
| Indicadores gerados e interpretação | 7,5 | 20% | 1,50 |
| Código documentado e reprodutível | 6,5 | 15% | 0,975 |
| **Soma ponderada (85%)** | | | **6,60** |

A N2 não terá prova oral. A nota final, renormalizando os quatro critérios (85% da rubrica) para a escala de 0 a 10, é **7,8**. Com o ponto extra atribuído na N2, a nota final fica **8,8**.
