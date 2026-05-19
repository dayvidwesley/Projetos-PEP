# Correção N1 — Any Júlia e Natália Paiva
Data: 16/05/2026
Trabalho: Procedimento Operacional Padrão para Extração e Análise de Indicadores de Desempenho Comercial via PostgreSQL e Power BI — Estudo de Caso na Rural Data (Nettão)

## Observações iniciais

A entrega está em `.docx` na raiz da pasta `any-julia/`, fora de uma subpasta `N1/`. Padronizar movendo para `any-julia/N1/` e idealmente exportando em PDF para a versão final do artigo (formato ENEGEP).

A pasta `natalia-paiva/` está vazia. Como o trabalho é em dupla, faz sentido unificar as duas pastas em `any-julia-e-natalia-paiva/`.

Meu nome aparece como "Prof. Dayvid W. P. Martins" no cabeçalho, com o prefixo correto. Isso é compatível com o papel de orientador, mas o template ENEGEP normalmente reserva o cabeçalho para autores. Considerem mover para uma seção de agradecimentos ou rodapé, ou retirar.

## Fundamentação teórica (peso 30%)

A fundamentação é ambiciosa e cobre os três blocos esperados com muita profundidade.

Em 2.1, vocês trazem o ciclo dado→informação→conhecimento com um exemplo do próprio caso: "R$ 84.500 de faturamento em outubro" como dado, "92% da meta orçada" como informação, "intensificar campanhas de retenção no segmento suinocultura" como conhecimento orientando decisão. Esse nível de concretude é o que dá força ao texto. Os níveis operacional, tático e estratégico aparecem situados na realidade da Rural Data.

Em 2.2, o histórico do banco de dados está completo (60-70-2000-2010+, com Codd em 1970 citado primariamente e PostgreSQL desde 1996 contextualizado), e o gancho com polyglot persistence amarra bem na escolha do PostgreSQL como espinha dorsal transacional.

O ganho real do trabalho está nas seções 2.4 a 2.7. A discussão de modelagem dimensional (Kimball e Ross), esquema estrela, ETL/ELT, KPIs (Parmenter) e os quatro componentes do Power BI (Power Query, Modelo, DAX, Visualização) traz profundidade conceitual real. A ponte entre Clean Architecture e o desacoplamento das camadas do Power BI é uma articulação bem feita e sustenta a tese de que o POP é robusto à mudança de fonte.

Dois pontos a corrigir:

- Na seção 2.4, a ilustração da 2FN ("todos os atributos da assinatura dependem do identificador único") usa chave simples. A 2FN só faz sentido em chave composta, porque ela ataca dependência parcial em chaves compostas. Reformular com uma tabela de chave composta (talvez uma associativa cliente x fazenda x período).
- Não há discussão de agregação vs composição, que é parte explícita do roteiro do trabalho. Vale incluir uma subseção curta antes da modelagem dimensional, com exemplo do próprio caso (Cliente/Fazendas como agregação, Assinatura/Logs como composição, por exemplo).

Nota do critério: 9,0.

## Qualidade da revisão bibliográfica (peso 20%)

Bibliografia muito rica, com autores certos no lugar certo: Codd em 1970 como referência primária, Davenport e Prusak para conhecimento, Date e Elmasri/Navathe para BD, Kimball e Ross para modelagem dimensional, Sharda/Delen/Turban para BI, Parmenter para KPIs, Martin para Clean Architecture, Microsoft e Supabase como documentação oficial. Quinze referências, ABNT consistente, mistura coerente de livros consagrados, artigos clássicos e documentação técnica.

Nota do critério: 9,5.

## Normalização e modelagem de dados (peso 20%)

As três formas normais aparecem definidas (com a ressalva sobre a 2FN já feita), os relacionamentos 1:N estão bem identificados no próprio caso (Cliente/Assinaturas, Assinatura/Logs, Cliente/Fazendas, Assinatura/Faturamento). A discussão de modelagem dimensional (fato x dimensão, esquema estrela, calendário como dimensão de tempo) acrescenta valor real, demonstrando entendimento de que o modelo analítico não é o mesmo modelo transacional.

Dois pontos a aprofundar:

- Não há diagrama. Nem ER do PostgreSQL nem esquema estrela do Power BI. Como o texto cita seis tabelas e quatro relacionamentos, a falta visual fica sentida. Esse diagrama vai ser exigido na N2.
- Faltou tratar agregação vs composição (já comentado em fundamentação).
- Os relacionamentos descritos são todos 1:N. Vale pensar se algum no caso real é N:M (Cliente/Plano, talvez, considerando histórico de mudanças de plano), e como o esquema lida com isso.

Nota do critério: 8,0.

## Procedimento de conexão documentado (peso 15%)

Aqui o trabalho está muito bem posicionado. A Etapa 2 do POP descreve com clareza a conexão direta ao PostgreSQL hospedado no Supabase via conector nativo do Power BI, com governança de acesso (credencial de leitura, papel restrito). O Quadro 1 mapeia as seis tabelas relevantes com tipo (fato/dimensão) e papel no modelo, o Quadro 2 sintetiza o POP em uma referência de uma página, e o Quadro 3 detalha oito indicadores com fonte e cálculo conceitual. O conjunto é reprodutível.

O que falta para fechar com nota cheia: um exemplo concreto da string de conexão Supabase (host, porta, banco, sslmode) e idealmente um print do Power BI Desktop conectado, ou um trecho M do Power Query mostrando o "Source = PostgreSQL.Database(...)". Esses elementos vão ser preenchidos na N2.

Nota do critério: 9,0.

## Formatação ENEGEP/SBPO (peso 15%)

Template oficial, cabeçalho, resumo, palavras-chave, seções numeradas, quadros numerados (1 a 3) com fonte indicada e citados no corpo do texto, referências em ABNT bem cuidadas. A forma está bem feita.

Pontos a ajustar:

- Padronizar o cabeçalho conforme o template ENEGEP (verificar a posição do orientador, conforme observação inicial).
- A estrutura termina em "4. Considerações Finais", sem uma seção 4 dedicada a Resultados. Os Quadros 1, 2 e 3 cumprem parte do papel de "resultados planejados", mas formalmente o ENEGEP espera seções separadas para Resultados e Conclusão. Considerem dividir.

Nota do critério: 8,5.

## Nota final

| Critério | Nota | Peso | Ponderado |
|---|---|---|---|
| Fundamentação teórica | 9,0 | 30% | 2,70 |
| Revisão bibliográfica | 9,5 | 20% | 1,90 |
| Normalização e modelagem | 8,0 | 20% | 1,60 |
| Procedimento de conexão | 9,0 | 15% | 1,35 |
| Formatação ENEGEP/SBPO | 8,5 | 15% | 1,275 |
| **Total** | | | **8,8** |

## Para a N2

Quatro frentes a endereçar:

1. Construir os dois diagramas que estão pedindo lugar no texto: o ER das seis tabelas no PostgreSQL e o esquema estrela do modelo no Power BI, identificando fato x dimensão e marcando agregação vs composição.
2. Incluir uma subseção sobre agregação e composição com exemplos do próprio caso.
3. Reformular o exemplo da 2FN usando uma tabela com chave composta.
4. Adensar a conexão: string de exemplo, print do Power BI conectado, snippet M do Power Query.
