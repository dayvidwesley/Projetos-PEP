# Prova oral N1 — Any Júlia e Natália Paiva

Perguntas para a explanação de 5 minutos. Respostas orais, sem consultar o artigo no momento.

1. Vocês ilustram a 2FN com "todos os atributos dependem do identificador único da assinatura". Com chave simples isso é automático. Reformulem com uma tabela de chave composta: o que é dependência parcial e como eliminá-la?
   
  Considerando o contexto do trabalho, poderiamos reformular para chave composta utilizando uma tabela analítica chamada assinatura_periodo, formada pela combinação de assinatura_id e AnoMes, utilizada para armazenar métricas mensais das assinaturas. Se nessa tabela fossem armazenados atributos como nome do cliente, plano contratado ou estado da fazenda, esses atributos dependeriam apenas de assinatura_id, e não da chave completa (assinatura_id, AnoMes). Assim, isso caracterizaria uma dependência parcial, já que uma chave composta e um atributo depende apenas de uma parte dessa chave, e não dela inteira. Para eliminar esse problema, os atributos devem permanecer em suas tabelas de origem, como assinaturas e fazendas, enquanto a tabela associativa deve conter apenas informações que dependam efetivamente da combinação completa da chave, como faturamento mensal ou quantidade de eventos no período. 

2. O trabalho não trata agregação versus composição. Definam as duas e dê um exemplo de cada: uma relação em que a parte sobrevive sem o todo, outra em que a parte deixa de existir se o todo é removido.

  Na agregação, a relação é fraca: a parte tem vida própria e sobrevive mesmo que o todo desapareça. No nosso modelo, a relação entre assinaturas e fazendas se encaixa aqui. As duas estão ligadas por assinatura_id, mas a fazenda existe como unidade operacional independente — ela tem estado, rebanho, faturamento próprio. Se a assinatura for cancelada, a fazenda continua existindo como entidade de negócio. Já na composição, a relação é forte: a parte só faz sentido enquanto o todo existe. O exemplo claro aqui é assinaturas e logs_assinaturas. Um log de assinatura — registro de contratação, mudança de plano, cancelamento — só tem propósito enquanto a assinatura à qual ele se refere existe. Se a assinatura é removida, os logs perdem qualquer utilidade operacional ou analítica, porque o objeto que eles descreviam não existe mais.

3. Vocês mantêm o PostgreSQL normalizado e o modelo no Power BI em esquema estrela. Por que as duas modelagens convivem? O que cada uma otimiza?

6. Vocês definem ETL e ELT. Em que cenário a ELT é mais adequada e por que data warehouses modernos tendem a empurrar a transformação para depois do load?

7. Vocês mapeiam as camadas do Power BI na Clean Architecture. O que significa, em dependência entre camadas, dizer que a lógica analítica (DAX) é independente da origem dos dados?
