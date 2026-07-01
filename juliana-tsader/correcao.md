# Correção N2 — Juliana Tormim Sader
Data: 27/06/2026
Trabalho: Procedimento operacional padrão para extração e análise de dados em banco documental: aplicação a currículos Lattes do PPGEP/UFG

A N1 ficou registrada com nota 9,0 (oral 10,0). A N2 manteve o nível: o trabalho atende o que eu havia pedido para esta etapa (rosto do artigo completo, organização da pasta, MVC e governança de TI na fundamentação, e a consolidação dos indicadores com Qualis e fator de impacto mais a comparação documental × relacional), e a parte prática foi de fato executada sobre o banco documental.

## Conexão e extração de dados (peso 25%)

A conexão está em código (02_carregar_mongodb.py, função conecta), com MongoClient, timeout de seleção e um ping ao servidor para falhar cedo, e o ambiente está caracterizado (Python 3.10, pymongo, MongoDB 7.0, Compass). É boa engenharia de conexão. Duas ressalvas: não há print/captura da conexão (a rubrica pede print além do código), e o dataset (os JSONs do Lattes) e os CSVs de referência de Qualis/IF não acompanham a entrega, o que impede a reexecução real, dá para inspecionar o código, não para rodar. A coleta original via scriptLattes está bem creditada.

Nota do critério: 7,5.

## Qualidade das queries e análises (peso 25%)

São sete indicadores, todos implementados em pandas e pertinentes ao cenário acadêmico: top de artigos por pesquisador, produção anual, orientações em andamento por nível, rede de coautoria, distribuição Qualis e fator de impacto acumulado. O ponto a alinhar é que os pipelines do MongoDB declarados no código (PIPELINE_I3_MONGODB e afins) não são executados, o 03_analisar.py roda só as funções pandas, e os pipelines ficam como constantes ilustrativas. A afirmação de que os indicadores foram "implementados tanto como pipeline MongoDB quanto pandas" é, portanto, só parcialmente verdadeira na execução. E o I5 (rede de coautoria) é metodologicamente frágil: ele casa o pseudônimo no campo de autores, mas a coleção de artigos não carrega esse campo na forma esperada, e o resultado é relatado de modo vago ("núcleo de seis a oito pesquisadores"), sem tabela ou figura.

Nota do critério: 7,0.

## Indicadores gerados e interpretação (peso 20%)

Conjunto coerente e numericamente consistente (a soma do I6 fecha com o total de artigos declarado), com figuras para quase todos os indicadores. A discussão fecha o ciclo dado→informação→conhecimento→decisão de fato: a leitura da rede de coautoria vira uma decisão de gestão concreta (estimular vínculos entre os pesquisadores periféricos e o núcleo central para elevar a produção agregada), e o I7 traz uma analogia boa com throughput ponderado da Engenharia de Produção (qualidade × volume). Os indicadores I1 a I4 ficam mais descritivos, mas o trabalho como um todo entrega a interpretação que essa etapa cobra.

Nota do critério: 8,5.

## Código documentado e reprodutível (peso 15%)

É o ponto mais forte da engenharia do trabalho: quatro scripts numerados, docstrings de módulo, argparse com help, README com tabela de scripts e nota de LGPD, requirements.txt. A anonimização (01_anonimizar.py) é robusta, com pseudônimos determinísticos, remoção de campos sensíveis e mapa fora do repositório, vai além do pedido e é exatamente o cuidado certo para um dado de pessoas reais. Pesa contra: o README está desatualizado (não cita o 04_enriquecer_qualis_if.py, que é justamente o script central da N2), os dados de referência não vêm na entrega, e há um arquivo lixo de 1 byte (codigo/codigo) a remover.

Nota do critério: 8,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Conexão e extração de dados | 7,5 | 25% | 1,875 |
| Qualidade das queries e análises | 7,0 | 25% | 1,75 |
| Indicadores gerados e interpretação | 8,5 | 20% | 1,70 |
| Código documentado e reprodutível | 8,0 | 15% | 1,20 |
| **Soma ponderada (85%)** | | | **6,525** |

A N2 não terá prova oral. A nota final, renormalizando os quatro critérios (85% da rubrica) para a escala de 0 a 10, é **7,7**. Com o ponto extra atribuído na N2, a nota final fica **8,7**.

O caminho para subir, e o trabalho tem fôlego para isso, é fazer os pipelines do Mongo rodarem de verdade (não só constarem como texto), consertar o I5 carregando o campo de autores na coleção, e anexar os CSVs de referência para que a análise seja reproduzível. O I5 e o I7 são onde mora a contribuição do trabalho.
