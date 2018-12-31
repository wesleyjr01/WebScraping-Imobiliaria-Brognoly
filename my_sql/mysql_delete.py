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

# building the delete command to be used with a dictionary
delete_stmt = (
    "DELETE from contatos WHERE id = 7"
)

cursor.execute(delete_stmt)
con.commit()
cursor.close()
con.close()
