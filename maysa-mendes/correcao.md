# Correção N1 — Maysa Mendes Campos
Data: 17/05/2026
Trabalho: Procedimento para Extração e Análise de Dados por meio de Banco de Dados no Contexto da Engenharia de Produção

## Fundamentação teórica (peso 30%)

Os três blocos aparecem, com definições corretas, mas o tratamento é superficial e ficou faltando parte do que a disciplina pede. No SIG (2.1) você cobre dado/informação/conhecimento e os tipos SPT/SIG/SAD/ERP, o que está certo, mas não desenvolve a governança de TI, que é um dos pontos do bloco (ver Aula-03). Em arquitetura (2.2) você trata camadas, níveis de abstração (físico, lógico, visão) e cita a Clean Architecture, porém sem o MVC e sem o autor de referência da arquitetura limpa (Martin). O MVC está na rubrica e na Aula-04, vale incluir.

O ponto mais frágil é o histórico de bancos. Você menciona Codd e 1970 de passagem em 2.3, mas não há a linha do tempo que a disciplina cobra: anos 60 (arquivos/hierárquico, IMS), 70 (Codd e o modelo relacional), 80–90 (SQL, Oracle, PostgreSQL, MySQL), 2000 (NoSQL) e 2010+ (polyglot persistence). Também falta um comparativo organizado relacional × NoSQL por critério (unidade, esquema, transação ACID × BASE, escala), você descreve características soltas de cada um, sem confrontá-las. A parte de agregação e composição (2.6) está bem feita, com os exemplos de fornecedor/pedido e ordem de produção/itens corretos.

Nota do critério: 7,0.

## Qualidade da revisão bibliográfica (peso 20%)

A base é de livros-texto sólidos da área (Date, Elmasri e Navathe, Silberschatz/Korth/Sudarshan, Heuser) mais Schwab e Davenport/Harris. As referências estão em ABNT e há citação no corpo do texto. Faltou variedade (não há artigo acadêmico nem norma técnica) e há um problema de precisão: a entrada "TOREY, Torey et al." está malformada, provavelmente é Teorey — confira autor, título e ano, porque você cita esse trabalho logo no início da fundamentação. A lista também é curta (cerca de dez entradas) e bastante repetida no texto.

Nota do critério: 6,5.

## Normalização e modelagem de dados (peso 20%)

As três formas normais estão definidas corretamente: 1FN com valor atômico e sem grupos repetitivos, 2FN eliminando dependências parciais em relação à chave primária e 3FN eliminando dependências transitivas entre atributos não-chave. Você não cai no erro de trocar 2FN por 3FN, isso é positivo. Agregação e composição também estão certas e com bons exemplos.

O que enfraquece o critério é a ausência de exemplo e de diagrama. As formas normais e os relacionamentos 1:1, 1:N e N:M aparecem só definidos, sem um caso aplicado, e não há nenhum diagrama (ER ou de classes) do modelo de dados. Modelagem, neste trabalho, é mostrar o modelo desenhado e a normalização rodando sobre ele. Para a N2 isso é obrigatório.

Nota do critério: 6,0.

## Procedimento de conexão documentado (peso 15%)

A metodologia está organizada e separa bem o procedimento relacional (3.1) do não relacional (3.2), cada um com identificação de credenciais, conexão via ferramenta gráfica (DBeaver/pgAdmin, Compass), execução de consultas, conexão via Python (psycopg2, pymongo) e tratamento dos dados em Pandas. A estrutura de passos é clara e reutilizável.

A limitação é o nível de abstração. Os passos são genéricos ("inserir host, porta, usuário e senha", "estabelecer a conexão", "executar consultas SELECT"), sem string de conexão de exemplo, sem código real e sem as queries que você pretende rodar. Também não há escolha e justificativa de um SGBD em função de um cenário, você apresenta os dois caminhos em paralelo, de forma neutra. Para N1 o planejamento já cumpre, mas registre que a N2 cobra o procedimento concreto e reprodutível.

Nota do critério: 7,0.

## Formatação ENEGEP/SBPO (peso 15%)

Template ENEGEP correto, resumo em itálico, palavras-chave, todas as seções na ordem e, diferente de muitos, com Resultados Esperados e Conclusão efetivamente escritos, não só o título. Referências em ABNT. O que falta para subir é o uso de elementos visuais: o trabalho não tem nenhuma figura, tabela ou quadro numerados, e a rubrica de formatação valoriza tabelas e figuras referenciadas no texto. Um quadro comparativo relacional × NoSQL e um diagrama do modelo já resolveriam isso e ainda reforçariam a fundamentação.

Nota do critério: 7,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 7,0 | 30% | 2,10 |
| Revisão bibliográfica | 6,5 | 20% | 1,30 |
| Normalização e modelagem | 6,0 | 20% | 1,20 |
| Procedimento de conexão | 7,0 | 15% | 1,05 |
| Formatação ENEGEP/SBPO | 7,5 | 15% | 1,125 |
| **Total** | | | **6,8** |

## Para a N2

1. Completar o histórico de bancos (linha do tempo dos anos 60 ao polyglot persistence) e montar um quadro comparativo relacional × NoSQL por critério.
2. Incluir o MVC e a governança de TI na fundamentação, com autor de referência para a Clean Architecture.
3. Desenhar o diagrama do modelo de dados e aplicar as três formas normais sobre um exemplo concreto desse modelo.
4. Escolher um SGBD e justificar pela natureza do dado, com string de conexão, código e queries planejadas.
5. Corrigir a referência malformada (Teorey) e ampliar a bibliografia com ao menos um artigo acadêmico.
