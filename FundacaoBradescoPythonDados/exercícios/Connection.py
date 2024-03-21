import sqlite3

# Conectacom o banco de dados ou cria um banco no caso de um banco não existente
con = sqlite3.connect("primeiro_banco.bd")
# Busca Resultados de conexão
cur = con.cursor()
# Cria uma tabela em um banco de dados
cur.execute("CREATE TABLE contato(nome, endereco, telefone)")

# Verifica se a tabela já existe
tabela_existe = cur.fetchone()
# Caso a tabela não existe, irá criá-la
if not tabela_existe:
    cur.execute("CREATE TABLE contato(nome, endereco, telefone)")
    print("Tabela 'contato' criada com sucesso!")
else:
    print("A tabela 'contato' já existe.")
# Consulta a tabela
res = cur.execute("SELECT name FROM sqlite_master")
# Busca a linha consultada
print(res.fetchone())
('contato',)
con.commit()
con.close()
