import mysql.connector
from mysql.connector import errorcode

senha = 'senha'
configuracao = {
    'user': 'root',
    'password': senha,
    'host': '127.0.0.1',
    'database': 'agenda'
}

try:
    # con = mysql.connector.connect(user='root', password='D134732592889', host='127.0.0.1', database='agenda')
    con = mysql.connector.connect(**configuracao)
    print('connected!')
except mysql.connector.Error as erro:
    if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuario ou senha invalidos.')
    elif erro.errno == errorcode.ER_BAD_DB_ERROR:
        print('Banco de dados não existe')
    else:
        print(erro)
else:
    con.close()
