# Projetos PEP -- Praticas em Engenharia de Producao (2026/1)

Repositorio da disciplina **Praticas em Engenharia de Producao** do curso de Engenharia de Producao da **Universidade Federal de Goias (UFG)** -- Faculdade de Ciencias e Tecnologia, Campus Aparecida de Goiania.

**Professor:** Dayvid W P Martins

---

## Objetivo

Este repositorio centraliza os trabalhos dos alunos da disciplina no semestre 2026/1. O trabalho consiste na elaboracao de um **Procedimento Operacional Padrao (POP)** no formato de artigo cientifico (normas ENEGEP/SBPO), documentando o procedimento de **acesso, extracao e analise de dados** diretamente de um banco de dados real.

O objetivo e que o aluno demonstre **autonomia analitica**: saber ir direto a fonte dos dados para tomar decisoes fundamentadas, completando o ciclo **dado -> informacao -> conhecimento -> decisao**.

## Estrutura do Trabalho

O trabalho e dividido em duas entregas, cada uma valendo uma nota:

### N1 -- Construcao Teorica
- Artigo com fundamentacao teorica completa (SIG, arquitetura de software, bancos de dados)
- Historico, normalizacao (1FN-3FN), relacionamentos (1:1, 1:N, N:M), agregacoes e composicoes
- Procedimento de conexao ao BD escolhido
- Explanacao oral de 5 min ao professor

### N2 -- Parte Pratica
- Execucao real do POP descrito na N1
- Conexao a BD real + queries e analises
- Resultados, indicadores e conclusao
- Codigo documentado e reprodutivel
- Explanacao oral de 5 min ao professor

## Estrutura do Repositorio

Cada aluno possui **sua propria pasta** dentro deste repositorio. Nao e permitido alterar a pasta de outros colegas.

```
/
├── README.md
├── aluno-nome-sobrenome/
│   ├── artigo/          # Artigo no formato ENEGEP/SBPO
│   ├── codigo/          # Scripts de conexao e queries
│   ├── dados/           # Dados anonimizados (se aplicavel)
│   └── apresentacao/    # Registro da explanacao oral
├── aluno-outro-nome/
│   └── ...
└── ...
```

## Como Comecar

1. Crie uma conta no [GitHub](https://github.com) (caso ainda nao tenha)
2. Solicite acesso ao repositorio ao professor
3. Crie sua pasta com seu nome no formato `nome-sobrenome`
4. Comite todas as entregas: artigo, codigo, dados (anonimizados) e registro da explanacao oral

## Bancos de Dados Aceitos

| SGBD | Ferramenta Grafica | Biblioteca Python |
|------|-------------------|-------------------|
| PostgreSQL | pgAdmin, DBeaver | psycopg2 |
| MySQL | MySQL Workbench, DBeaver | mysql-connector |
| MongoDB | MongoDB Compass | pymongo |
| Cassandra | DataStax Studio | cassandra-driver |

## Fonte dos Dados

- **Opcao A:** BD da empresa onde o aluno trabalha/estagia (respeitando sigilo e LGPD)
- **Opcao B:** Dataset estruturado disponibilizado pelo professor

## Criterios de Avaliacao

### N1 -- Teorica
| Criterio | Peso |
|----------|------|
| Fundamentacao teorica (SIG + Arq + BD) | 30% |
| Qualidade da revisao bibliografica | 20% |
| Normalizacao e modelagem de dados | 20% |
| Procedimento de conexao documentado | 15% |
| Formatacao ENEGEP/SBPO | 15% |

### N2 -- Pratica
| Criterio | Peso |
|----------|------|
| Conexao e extracao de dados | 25% |
| Qualidade das queries e analises | 25% |
| Indicadores gerados e interpretacao | 20% |
| Codigo documentado e reprodutivel | 15% |
| Apresentacao oral | 15% |

## Dicas

1. **Comece pela N1** -- uma boa fundamentacao teorica facilita toda a parte pratica
2. **Escolha bem o BD** -- se a empresa tem ERP com PostgreSQL ou MySQL, use dados reais (com autorizacao); caso contrario, use o dataset do professor
3. **Documente tudo** -- o POP e um procedimento; outra pessoa deve conseguir reproduzir seguindo seu artigo
4. **Conecte teoria e pratica** -- ao mostrar uma query, explique qual conceito teorico ela aplica
5. **Respeite a LGPD** -- se usar dados reais, anonimize dados pessoais antes de inclui-los no artigo

---

**UFG -- Faculdade de Ciencias e Tecnologia | Engenharia de Producao | 2026/1**
