# Correção N1 — Gustavo Vieira Vale
Data: 17/05/2026
Trabalho: Procedimento Operacional Padrão para Extração e Análise de Dados de Tarefas Administrativas em um Banco de Dados Relacional

## Fundamentação teórica (peso 30%)

A fundamentação cobre os três blocos pedidos, com aplicação consistente ao cenário escolhido (Departamento de Processos em um escritório de médio porte com 60 funcionários e 8 tabelas relacionais). A introdução é bem articulada, com objetivo geral e seis objetivos específicos numerados, e fecha com uma afirmação forte: "a análise do banco de dados deve estar conectada à Melhoria de Processos, pilar fundamental para diferenciar um Engenheiro de Produção de um Engenheiro de Software". A escolha de Dumas et al. (2018) como referência primária de BPM ancora bem esse argumento.

A seção 2.1 (SIG) traz a definição via Laudon e Laudon e a Figura 2 — um diagrama visual do ciclo Dado → Informação → Conhecimento → Decisão. Esse recurso visual ajuda a fixar o conceito central da disciplina. O Quadro do tópico 2.1 traz os quatro estágios com descrição e exemplo aplicado.

A seção 2.5 (Normalização) é onde o trabalho começa a se destacar. As três formas normais aparecem definidas com terminologia técnica correta e, principalmente, com exemplos no próprio banco de tarefas (Tabela 2):
- 1FN com o exemplo do campo de responsável que não pode ter vários nomes
- 2FN com data de abertura dependendo da tarefa e não do funcionário
- 3FN com o nome do setor que não deve ficar na tabela de tarefas e deve estar na tabela de setores

A seção 2.6 traz a Tabela 3 com cardinalidades 1:1, 1:N e N:M, todos com exemplos do próprio banco (Setor/Funcionários, Processo/Atividades, Atividade/Tarefas, Funcionário/Tarefas, Tarefas/Participantes como N:M).

A seção 2.7 (Agregação e Composição) está exemplar: você define a agregação como "tem um" com partes independentes (Funcionário/Tarefa: a tarefa pode ser excluída sem afetar o funcionário) e a composição como dependência de existência (Tarefa/historico_tarefas: o histórico só faz sentido enquanto a tarefa existir). Esse uso correto do par UML aplicado ao próprio cenário é o que a rubrica espera no topo do critério.

Lacunas a corrigir:

- A seção 2.2 (Arquitetura de Software) trata apenas o nível "em camadas" de forma genérica (Interface → Sistema → Regras de Negócio → BD → Consultas). Falta abordar MVC, Clean Architecture (Martin) e arquitetura hexagonal (Cockburn), que são padrões relevantes para o argumento de que o banco é um detalhe de infraestrutura desacoplada.
- A seção 2.3 cobre a evolução do banco em apenas três frases (anos 60, 70 com Codd, 2000+ com NoSQL). Codd inclusive é citado mas não consta na bibliografia. O roteiro pede a evolução em décadas com mais detalhe.
- As propriedades transacionais ACID e BASE não são tratadas, e tampouco a polyglot persistence.

Nota do critério: 8,5.

## Qualidade da revisão bibliográfica (peso 20%)

A bibliografia tem apenas cinco entradas: Laudon e Laudon 2023, Elmasri e Navathe 2018, Silberschatz/Korth/Sudarshan 2019, Dumas et al. 2018, Davenport e Harris 2007. As cinco são adequadas e Dumas et al. é referência primária de Business Process Management — diferencial pertinente ao cenário do trabalho.

Pontos a corrigir:

- Codd (1970) é citado no texto ("modelo relacional proposto por Edgar F. Codd, na década de 1970") mas não consta na lista de referências. Toda citação no texto exige entrada bibliográfica.
- Faltam clássicos relevantes para o tema: Date (BD), Fowler/Sadalage (NoSQL), Martin (Clean Architecture), Cockburn (Hexagonal).
- Formato das citações no texto usa colchetes "[Laudon; Laudon, 2023]" em vez de parênteses "(LAUDON; LAUDON, 2023)" — o padrão ABNT é parênteses com sobrenome em caixa alta.
- A entrada de Davenport e Harris tem um typo: "Harvard Business School Press**x**, 2007".

Nota do critério: 7,0.

## Normalização e modelagem de dados (peso 20%)

Esse é o critério mais bem servido do trabalho. A Tabela 2 (Formas normais) traz cada forma normal com explicação E exemplo no próprio banco de tarefas. A Tabela 3 (Relacionamentos) traz 1:1, 1:N e N:M com exemplos do próprio cenário, incluindo a relação N:M (Tarefas/Participantes).

A Figura 3 é o **Diagrama de Relacionamento do Banco de Dados próprio do cenário**, com as oito tabelas (Setor, Funcionário, Processo, Atividade, Tarefa, Status da Tarefa, Prioridade, Histórico de Tarefas) e as cardinalidades marcadas. Esse diagrama é exatamente o que a rubrica pede.

As Tabelas 5 a 12 detalham cada uma das oito entidades com todos os campos e descrição. Esse nível de modelagem completa do cenário é diferencial real.

A seção 2.7 (Agregação e Composição) aplica o par UML ao próprio cenário, distinguindo Funcionário/Tarefa (agregação, parte autônoma) e Tarefa/historico_tarefas (composição, dependência forte).

Nota do critério: 9,5.

## Procedimento de conexão documentado (peso 15%)

Outro critério muito bem servido. As Etapas 3 a 9 trazem **18 códigos Python reais e executáveis**, cobrindo:

- Conexão (Código 1: `sqlite3.connect`; Código 2: teste de conexão via `pd.read_sql_query`)
- Validação da estrutura (Código 3: `SELECT name FROM sqlite_master`; Código 4: `PRAGMA table_info`)
- Exploração (Códigos 5-9: `COUNT`, `SELECT * LIMIT 10`, distribuição por status com JOIN, distribuição por prioridade com JOIN, contagem de campos nulos)
- Extração consolidada (Códigos 10-13: volume de tarefas por setor com JOIN triplo entre tarefas/funcionarios/setores; backlog por setor; tempo médio de execução por processo com JOIN entre tarefas/atividades/processos; produtividade por funcionário)
- Cálculo de indicadores (Código 14: taxa de atraso com CASE WHEN; Tabela 16 com seis indicadores e fórmulas)
- Tratamento (Códigos 15-16: criação de DataFrame, conversão de datas, criação de coluna calculada)
- Visualização (Código 17: gráfico de barras com matplotlib; Código 18: modelo de interpretação estruturada)
- Plano de Ação 5W2H (Tabela 18) consolidando as recomendações de melhoria por prioridade

A escolha de SQLite simplifica a execução e está justificada como adequada ao contexto acadêmico ("alternativa simples e adequada... para se tratar de uma alternativa simples e adequada"). Vale comentar, porém, que SQLite é um banco em arquivo único, sem servidor — adequado para o exercício, mas afasta do cenário industrial real (servido) que o roteiro do trabalho privilegia (PostgreSQL, MySQL, MongoDB, Cassandra). Considerar para a N2 migrar pelo menos um exemplo para PostgreSQL ou MySQL.

Nota do critério: 9,5.

## Formatação ENEGEP/SBPO (peso 15%)

O trabalho está bem cuidado na formatação interna: sumário detalhado, glossário com 10 termos (Tabela 1) ajudando o leitor não-técnico, resumo em português e Abstract em inglês com palavras-chave em ambas as línguas, tabelas e códigos numerados com legenda, referências bibliográficas listadas.

Pontos críticos a corrigir:

- **Template não é ENEGEP/SBPO**. O artigo usa cabeçalho "Engenharia de Produção FCT UFG" em formato de trabalho acadêmico genérico. O ENEGEP exige cabeçalho próprio do encontro (logo, edição, local e data) e bordas/fontes específicas.
- **Seção 4 (Aplicação e Resultados) está vazia** — só o título aparece, sem conteúdo nenhum.
- **Seção 5 (Considerações Finais) está vazia** — só o título.

Como o trabalho descreve um procedimento de extração e os dez passos já estão exaustivamente documentados na seção 3.4, faltou pelo menos uma página de "Resultados esperados" (descrevendo os indicadores que se pretende gerar e como serão analisados) e uma página de "Considerações Finais" amarrando o trabalho e apontando o que virá na N2.

Outros pequenos ajustes:
- A Figura 1 (resumo visual) na página 4 não tem fonte explicitada.
- A Tabela 1 (glossário) aparece antes mesmo da seção 1.3 ser declarada.

Nota do critério: 6,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 8,5 | 30% | 2,55 |
| Revisão bibliográfica | 7,0 | 20% | 1,40 |
| Normalização e modelagem | 9,5 | 20% | 1,90 |
| Procedimento de conexão | 9,5 | 15% | 1,425 |
| Formatação ENEGEP/SBPO | 6,5 | 15% | 0,975 |
| **Total** | | | **8,3** |

## Para a N2

Quatro frentes a endereçar:

1. Migrar o artigo para o template ENEGEP/SBPO oficial e preencher as seções 4 (Aplicação e Resultados) e 5 (Considerações Finais), atualmente vazias.
2. Ampliar a bibliografia: incluir Codd 1970 (que já está citado no texto sem entrada), Date para BD, Fowler/Sadalage para NoSQL, Martin para Clean Architecture, Cockburn para Hexagonal. Corrigir o formato das citações de colchetes para parênteses, padrão ABNT.
3. Desenvolver a arquitetura de software com MVC, Clean Architecture e Hexagonal (não apenas camadas), e expandir o histórico do banco de dados com mais detalhe sobre cada década (60, 70, 80-90, 2000, 2010+). Incluir uma seção sobre ACID, BASE e polyglot persistence.
4. Manter SQLite como cenário acadêmico se preferir, mas incluir pelo menos um exemplo equivalente em PostgreSQL ou MySQL na execução prática, para alinhar com os SGBDs servidos que o roteiro do trabalho privilegia.

## Prova oral

Nota: 9,0

As cinco corretas: MVC, hexagonal e Clean Architecture bem distinguidas, histórico dos bancos, ACID e BASE no seu cenário, as limitações concretas do SQLite (lock de escrita, volume, arquitetura cliente-servidor) e a especificidade do engenheiro de produção com o 5W2H.

# Correção N2 — Gustavo Vieira Vale
Data: 27/06/2026
Trabalho: Procedimento Operacional Padrão para Extração e Análise de Dados de Tarefas Administrativas em um Banco de Dados Relacional

Considero resolvidos os pontos que você levantou na revisão da N1 (o padrão SBPO com a logo da UFG no lugar da logo do evento, e o escopo teórico da N1), então não repenalizo formatação por template aqui. A N2 executa o POP de ponta a ponta e está num nível alto.

## Conexão e extração de dados (peso 25%)

A conexão está documentada com código (Código 1, p. 17, e a célula 4 do notebook), com busca robusta do arquivo, PRAGMA foreign_keys = ON e o output real registrando a versão do SQLite e "Conexão realizada com sucesso". É reprodutível, com período parametrizado e queries usando :data_inicio/:data_fim. Mantenho a observação da N1, que você assume: segue tudo em SQLite, sem o exemplo equivalente em PostgreSQL ou MySQL que sugeri (a frente 4 não foi cumprida, só citada como possibilidade). Um detalhe operacional: o arquivo .sqlite não parece ter sido entregue na pasta, o que impede a reprodução literal por terceiros.

Nota do critério: 8,0.

## Qualidade das queries e análises (peso 25%)

Aqui o trabalho brilha. O notebook traz uma camada de validação de dados que está acima do roteiro: PRAGMA integrity_check, foreign_key_check e checagens de coerência cronológica e de nulos por status (célula 10). E o SQL é avançado de verdade, window function para participação percentual (célula 17), CTE recursiva gerando o calendário mensal para a série de aberturas e conclusões (célula 29), CASE WHEN duplo para a taxa de atraso, e comparação do tempo real contra o tempo padrão (célula 23). Uma observação para alinhar: a taxa de atraso do PDF (Código 14) só conta data_conclusao > data_prazo, enquanto a versão completa e correta, que também pega as pendentes com prazo vencido, está só no notebook (célula 21). Quem reproduzir pelo PDF não chega aos 62,50%.

Nota do critério: 9,0.

## Indicadores gerados e interpretação (peso 20%)

Seis indicadores, todos com tabela e gráfico, mais o painel-resumo: volume por setor, backlog, taxa de atraso (com a média entre setores marcada no gráfico), tempo médio contra o padrão, produtividade e retrabalho, além da evolução mensal mostrando saldo negativo nos três meses. A interpretação é madura e tecnicamente honesta, você trata indicador alto como sinal para investigação, não como prova de ineficiência, declara as premissas e fecha no plano de ação 5W2H amarrado a evidência específica (redistribuir o backlog de Operações, redesenhar o fluxo de Suporte de Sistemas). É o ciclo dado→decisão fechado com critério.

Nota do critério: 9,0.

## Código documentado e reprodutível (peso 15%)

Notebook bem comentado, com docstrings nas funções utilitárias, células markdown por etapa e as fórmulas dos indicadores declaradas antes do cálculo, "para que o resultado seja auditável". Gera 21 artefatos e encerra a conexão ao final. Pesa contra: não há requirements.txt nem README na entrega, o arquivo .sqlite não acompanha, e a produtividade por funcionário (Figura 8) exibe nomes individuais com sufixo numérico; mesmo com a ressalva de que não é avaliação de desempenho, é um ranking nominal que merece atenção de LGPD, ainda que os dados sejam modificados.

Nota do critério: 7,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Conexão e extração de dados | 8,0 | 25% | 2,00 |
| Qualidade das queries e análises | 9,0 | 25% | 2,25 |
| Indicadores gerados e interpretação | 9,0 | 20% | 1,80 |
| Código documentado e reprodutível | 7,5 | 15% | 1,125 |
| **Soma ponderada (85%)** | | | **7,175** |

A N2 não terá prova oral. A nota final, renormalizando os quatro critérios (85% da rubrica) para a escala de 0 a 10, é **8,4**. Com o ponto extra atribuído na N2, a nota final fica **9,4**.
