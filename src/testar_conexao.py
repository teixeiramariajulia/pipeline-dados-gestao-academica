import psycopg2
from getpass import getpass

senha = getpass("Digite a senha do PostgreSQL: ")

conexao = psycopg2.connect(
    database="gestao-academica",
    user="postgres",
    password=senha,
    host="localhost",
    port=5432,
    options="-c client_encoding=UTF8"
)

print("Conexão com PostgreSQL realizada com sucesso!")

conexao.close()