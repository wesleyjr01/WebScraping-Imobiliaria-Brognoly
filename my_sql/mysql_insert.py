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

# building the insert command to be used with a dictionary
insert_stmt = (
    "INSERT INTO contatos (nome, telefone, celular) "
    "VALUES (%(cont_name)s, %(tel)s, %(cel)s)"
)

# Creating a dictionary with data to be insert
data = {
    'cont_name': 'Bela Adormecida3',
    'tel': '(61)2212-5652',
    'cel': '(61)98874-5852'
}

cursor.execute(insert_stmt, data)
con.commit()
cursor.close()
con.close()
