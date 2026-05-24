# Correção N1 — Geovana Gvas e Maria Eduarda
Data: 16/05/2026
Trabalho: Extração Autônoma de Dados Operacionais — um Procedimento Padrão para o Engenheiro de Produção

## Observação inicial

A pasta tem dois PDFs: uma versão com 13 páginas e outra com 15 ("(2).pdf"). Padronizar mantendo apenas o final (provavelmente o de 15 páginas, mais completo). Versões duplicadas no GitHub geram dúvida sobre qual avaliar.

## Fundamentação teórica (peso 30%)

O resumo do artigo já entrega o eixo conceitual completo, citando o ciclo dado→informação→conhecimento→decisão de forma explícita. A introdução é uma das mais bem articuladas que li, com problema claro (dependência da TI gera gargalo analítico), justificativa, pergunta de pesquisa formulada e estrutura do artigo anunciada. Bom começo.

A seção 2.1 traz Senge (1990) para o pensamento sistêmico — referência primária da "Quinta Disciplina" — e cita os tipos de sistemas SPT, SIG e SAD com base em O'Brien e Laudon. O ciclo dado→informação→conhecimento volta a aparecer com exemplo concreto (tempos de ciclo, volumes de produção, paradas de máquinas como dados brutos virando informação via SIG).

A seção 2.2 articula bem Fowler (Patterns of Enterprise Application Architecture), Bass/Clements/Kazman (Software Architecture in Practice, referência clássica que poucos trabalhos citam) e Martin (Clean Architecture), com o banco de dados situado na camada de infraestrutura.

A seção 2.3 traz o histórico do banco de dados (anos 1960 e 1970 com hierárquico e em rede, Codd em 1970 com o modelo relacional, NoSQL com Sadalage e Fowler) e cita Codd em fonte primária. Polyglot persistence aparece bem amarrado.

O ponto mais forte da fundamentação está em agregação versus composição: vocês definem corretamente "tem um" versus "parte de", citam Fowler/Sadalage e traduzem para SQL com a cláusula `ON DELETE CASCADE` e para NoSQL com documentos embutidos. Esse nível de articulação é o que a rubrica espera.

Três pontos a corrigir:

- A seção 2.1 começa com o título "Sistemas Integrados de Gestão (SIG)" e descreve ERP. Em Laudon, SIG (Sistemas de Informação Gerencial) é uma categoria de sistema que apoia o nível gerencial-médio com relatórios consolidados. Sistemas Integrados de Gestão é o ERP, que é um SPT corporativo. São conceitos distintos e estão sendo tratados como sinônimos.

- A seção 2.3, no parágrafo sobre operações, usa "agregação" como função SQL (soma, média, contagem) e "composição" como JOIN. Logo depois, no parágrafo seguinte, usa os mesmos termos com sentido estrutural (agregação UML/ER e composição UML/ER). São coisas diferentes e o uso ambíguo confunde — agregação na modelagem ER é estrutural (parte/todo), não tem relação com a função SUM ou GROUP BY do SQL.

- As três formas normais são mencionadas em uma frase ("regras para a organização das tabelas e dependências entre atributos"), sem definição. 1FN, 2FN e 3FN precisam aparecer com sua definição própria e exemplo.

Nota do critério: 8,5.

## Qualidade da revisão bibliográfica (peso 20%)

Vinte e duas referências, com presença forte de fontes primárias e clássicas no lugar certo: Codd 1970, Bass/Clements/Kazman, Senge (Quinta Disciplina), Sadalage e Fowler, Date, Elmasri e Navathe, Martin, Stair/Reynolds, O'Brien. A inclusão da ABNT NBR ISO 9001 (2015) como referência normativa para sustentar a definição formal de POP é um diferencial que poucos trabalhos trazem. Yin (Estudo de Caso) e Gil (Como Elaborar Projetos de Pesquisa) ancoram a metodologia.

Dois ajustes a fazer:

- Laudon aparece duas vezes nas referências (uma "LAUDON, K. C.; LAUDON, J. P." e outra "LAUDON, Kenneth C.; LAUDON, Jane P.") — é a mesma obra, padronizar em uma entrada.
- Date também aparece duas vezes (uma em inglês "Addison-Wesley, 2004", outra em português "Elsevier, 2004"). Manter só a edição usada nas citações.

Nota do critério: 8,5.

## Normalização e modelagem de dados (peso 20%)

Os relacionamentos 1:1, 1:N e N:M estão definidos com exemplos (funcionário/crachá, setor/funcionários, produtos/fornecedores) e a discussão de agregação versus composição estrutural está bem feita, conforme já comentado em fundamentação. A tradução em SQL com `ON DELETE CASCADE` e em NoSQL com documentos embutidos é exatamente o que se espera.

Lacunas:

- As três formas normais não são definidas (já comentado).
- A confusão terminológica entre "agregação SQL" (SUM, AVG) e "agregação UML/ER" no início de 2.3 enfraquece a seção.
- Não há diagrama ER ou de classes do modelo de dados que será usado na N2. Os exemplos de cardinalidade são genéricos (funcionário/crachá, setor/funcionários) e não vinculados ao dataset que vocês vão analisar. Como na N2 vão receber o dataset do docente, esse diagrama precisa ser construído sobre as tabelas reais.

Nota do critério: 7,5.

## Procedimento de conexão documentado (peso 15%)

A Figura 1 (fluxograma de escolha de SGBD) é um elemento original e útil — orienta a decisão entre relacional ou NoSQL com base em estrutura, volume contínuo, complexidade de relacionamentos e necessidade de indicadores. Termina em "Iniciar conexão", articulando bem com o procedimento. O Quadro 1, que pareia PostgreSQL, MySQL, MongoDB e Cassandra com exemplos de uso na produção industrial, sustenta o fluxograma.

A Figura 2 (fluxograma metodológico do POP) detalha as cinco fases com decisões e refinamentos, fechando em "Artigo concluído (N2)". Boa síntese visual do procedimento.

A seção 3 descreve as cinco fases em texto e cita as bibliotecas Python (psycopg2 para PostgreSQL, mysql-connector para MySQL, pymongo para MongoDB), o uso de pandas para análise, Jupyter Notebook como ambiente e Git/GitHub para versionamento.

O que falta para fechar com nota cheia: o trecho de código Python real executando a Fase 1 (string de conexão, `psycopg2.connect`, cursor, primeiro SELECT) e o tratamento de erro de conexão. Sem isso, o procedimento fica claro no nível conceitual mas pendente no nível de reprodução técnica. Esse adensamento será cobrado na N2.

Nota do critério: 8,0.

## Formatação ENEGEP/SBPO (peso 15%)

Template oficial, cabeçalho, resumo (em itálico, como o template pede), palavras-chave, seções numeradas, Quadro e Figuras numerados com fonte indicada, referências em ABNT.

Pontos a corrigir:

- Não há seção 4 (Resultados) nem seção 5 (Conclusão / Considerações Finais). O artigo termina abruptamente após a metodologia e vai direto para as referências. Mesmo na N1, a especificação do trabalho pede que essas seções apareçam parciais ou como planejamento. Recomendo encerrar com pelo menos um "4. Resultados esperados" (descrevendo os indicadores que se pretende gerar na N2) e uma "5. Considerações finais" amarrando o que foi discutido teoricamente.
- Duplicação de referências Laudon e Date (já comentado em bibliografia).

Nota do critério: 7,0.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 8,5 | 30% | 2,55 |
| Revisão bibliográfica | 8,5 | 20% | 1,70 |
| Normalização e modelagem | 7,5 | 20% | 1,50 |
| Procedimento de conexão | 8,0 | 15% | 1,20 |
| Formatação ENEGEP/SBPO | 7,0 | 15% | 1,05 |
| **Total** | | | **8,0** |

## Para a N2

Cinco frentes:

1. Corrigir os títulos da seção 2.1: separar Sistemas de Informação Gerencial (categoria de sistema, Laudon) do ERP (Sistema Integrado de Gestão).
2. Eliminar a ambiguidade do uso de "agregação" e "composição" na seção 2.3: deixar claro que esses termos se referem a relacionamentos estruturais (UML/ER), não a funções SQL.
3. Definir explicitamente 1FN, 2FN e 3FN com exemplos do dataset que será analisado.
4. Construir o diagrama ER do dataset fornecido pelo docente, marcando agregação versus composição visualmente.
5. Adensar a Fase 1 com código Python real (string de conexão, `psycopg2.connect`, cursor, primeiro SELECT) e adicionar as seções 4 (Resultados Esperados) e 5 (Considerações Finais).

## Prova oral

Nota: 8,5

As cinco corretas: SIG frente a ERP e seus níveis de decisão, funções SQL frente a relacionamento UML, as formas normais com violação em ordens de produção, a conexão com psycopg2 e a polyglot persistence. A conexão ficou descrita em texto, faltou o código literal que a pergunta pedia.
