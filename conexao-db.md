# 🔌 Como conectar aos bancos (ERP + MES)

Ambiente didático hospedado na nuvem. Os dois bancos estão **no ar 24/7** e exigem
usuário e senha. Use um cliente gráfico (mais fácil) ou o terminal.

## Credenciais (resumo)

| Banco | Tipo | Host | Porta | Usuário | Senha | Base |
|---|---|---|---|---|---|---|
| **ERP** | PostgreSQL | `pep-postgresql.arch7.dev` | `5432` | `erp` | `Fg669s8OGBgxTqL1C6gHv6FX7EJR` | `erp` |
| **MES** | MongoDB | `pep-mongo.arch7.dev` | `27018` | `mes` | `UT1EF3jReDHpf547q5P8BWivqLsx` | `mes` |

> ⚠️ Credenciais de uso em aula — não publique em repositórios públicos.
> No MongoDB a autenticação é no banco **`admin`** (`authSource=admin`) e a porta é **27018**.

---

## 1. PostgreSQL — ERP

**String de conexão:**
```
postgresql://erp:Fg669s8OGBgxTqL1C6gHv6FX7EJR@pep-postgresql.arch7.dev:5432/erp
```

### Opção A — DBeaver (recomendado) · https://dbeaver.io
1. **Database → New Database Connection → PostgreSQL**
2. Preencha:
   - Host: `pep-postgresql.arch7.dev` · Port: `5432`
   - Database: `erp` · Username: `erp` · Password: *(acima)*
3. **Test Connection → Finish**. As tabelas estão no schema **`erp`**.

### Opção B — terminal (psql)
```bash
psql "postgresql://erp:Fg669s8OGBgxTqL1C6gHv6FX7EJR@pep-postgresql.arch7.dev:5432/erp"
```

**Primeiro teste (deve retornar 19):**
```sql
SELECT count(*) FROM information_schema.tables WHERE table_schema = 'erp';
```

---

## 2. MongoDB — MES

**String de conexão:**
```
mongodb://mes:UT1EF3jReDHpf547q5P8BWivqLsx@pep-mongo.arch7.dev:27018/?authSource=admin
```

### Opção A — MongoDB Compass (recomendado) · https://www.mongodb.com/products/compass
1. Cole a string de conexão acima no campo **URI** e clique **Connect**.
2. Abra o banco **`mes`** para ver as 6 coleções.

### Opção B — terminal (mongosh)
```bash
mongosh "mongodb://mes:UT1EF3jReDHpf547q5P8BWivqLsx@pep-mongo.arch7.dev:27018/?authSource=admin"
```

**Primeiro teste (deve retornar 6 coleções):**
```js
use mes
db.getCollectionNames()
```

---

## 3. Interfaces web (navegador) — *em ativação*

Quando os endereços web estiverem publicados, será possível usar o banco **sem instalar
nada**, direto no navegador:

| Banco | URL | Login |
|---|---|---|
| ERP (Adminer) | `https://pep-postgresql.arch7.dev` | System **PostgreSQL**, Server `pep-postgres`, User/DB `erp` + senha |
| MES (Mongo Express) | `https://pep-mongo.arch7.dev` | usuário `aluno` + senha da turma |

> Enquanto isso, use os clientes da seção 1 e 2 (já funcionam).

---

## Problemas comuns
- **Mongo "Authentication failed":** confirme `authSource=admin` na URI e a porta **27018** (não 27017).
- **Postgres "could not connect":** confirme a porta **5432** e que a senha foi copiada inteira (sem espaços).
- **"Não vejo as tabelas" (Postgres):** elas ficam no schema **`erp`** — expanda esse schema na árvore do cliente.
