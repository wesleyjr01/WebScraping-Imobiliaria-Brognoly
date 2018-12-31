import mysql.connector

senha = 'senha'
configuracao = {
    'user': 'root',
    'password': senha,
    'host': '127.0.0.1',
    'database': 'agenda'
}

con = mysql.connector.connect(**configuracao)
cursor = con.cursor()

# building the update command to be used with a dictionary
query_stmt = (
    "SELECT nome, telefone, celular FROM contatos WHERE nome like 'M%'"
)

cursor.execute(query_stmt)

for (nome, telefone, celular) in cursor:
    print(f"Nome: {nome}, telefone: {telefone}, celular: {celular}")
cursor.close()
con.close()
