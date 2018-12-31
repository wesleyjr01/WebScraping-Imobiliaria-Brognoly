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
update_stmt = (
    "UPDATE contatos SET nome = %(cont_name)s, telefone = %(tel)s, celular = %(cel)s WHERE id = 2"
)

# Creating a dictionary with data to be insert
data = {
    'cont_name': 'Itachi',
    'tel': '(61)2312-5653',
    'cel': '(61)93874-5853'
}

cursor.execute(update_stmt, data)
con.commit()
cursor.close()
con.close()
