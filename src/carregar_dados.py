import pandas as pd
from pathlib import Path

# Localizar a pasta principal do projeto
pasta_projeto = Path(__file__).resolve().parent.parent

# Ler os arquivos tratados
df_alunos = pd.read_csv(
    pasta_projeto / "data" / "processed" / "alunos_tratados.csv"
)

df_academico = pd.read_csv(
    pasta_projeto / "data" / "processed" / "informacoes_academicas_tratadas.csv"
)

df_matriculas = pd.read_csv(
    pasta_projeto / "data" / "processed" / "matriculas_tratadas.csv"
)

print("Arquivos tratados carregados com sucesso!")

from sqlalchemy import create_engine, URL
from getpass import getpass

# Solicitar a senha do PostgreSQL
senha = getpass("Digite a senha do PostgreSQL: ")

# Criar a conexão
url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password=senha,
    host="localhost",
    port=5432,
    database="gestao-academica"
)

engine = create_engine(url)

# Enviar os dados para o PostgreSQL
with engine.begin() as conexao:
    df_alunos.to_sql(
        "alunos", conexao, if_exists="append", index=False
    )

    df_academico.to_sql(
        "informacoes_academicas", conexao, if_exists="append", index=False
    )

    df_matriculas.to_sql(
        "matriculas", conexao, if_exists="append", index=False
    )

print("Dados carregados no PostgreSQL com sucesso!")