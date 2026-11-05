import pandas as pd

#Extrair os dados dos arquivos CSV

df_alunos = pd.read_csv('data/raw/alunos.csv')
df_academico = pd.read_csv('data/raw/informacoes_academicas.csv')
df_matriculas = pd.read_csv('data/raw/matriculas.csv')

#Vizualizando os dados extraídos

print("DADOS DOS ALUNOS")
print(df_alunos.head())

print("\nINFORMACOES ACADÊMICAS")
print(df_academico.head())

print("\nDADOS DAS MATRÍCULAS")
print(df_matriculas.head())

#Verificando a quantidadede registros

print("\nQUANTIDADE DE REGISTROS")
print("Alunos:", df_alunos.shape)
print("Informações acadêmicas:", df_academico.shape)
print("Matrículas:", df_matriculas.shape)