import pandas as pd

#Lendo os arquivos originais

df_alunos = pd.read_csv('data/raw/alunos.csv')
df_academico = pd.read_csv('data/raw/informacoes_academicas.csv')
df_matriculas = pd.read_csv('data/raw/matriculas.csv')

#Verificando dados ausentes

print("DADOS AUSENTES - ALUNOS")
print(df_alunos.isnull().sum())

print("\nDADOS AUSENTES - INFORMAÇÕES ACADÊMICAS")
print(df_academico.isnull().sum())

print("\nDADOS AUSENTES - MATRÍCULAS")
print(df_matriculas.isnull().sum())

#Verificando matrículas duplicadas

print("\nVERIFICANDO MATRÍCULAS DUPLICADAS")

duplicadas = df_matriculas.duplicated(
    subset=['matricula', 'periodo']
).sum()

print("Matrículas duplicadas:", duplicadas)

#Visualizando os registros duplicados

print("\nREGISTROS DUPLICADOS")

print(
    df_matriculas[
        df_matriculas.duplicated(
            subset=['matricula', 'periodo'],
            keep=False
        )
    ].sort_values(['matricula', 'periodo']).head(10)
)

#Removendo matrículas duplicadas

df_matriculas['data_matricula'] = pd.to_datetime(
    df_matriculas['data_matricula']
)

df_matriculas = df_matriculas.sort_values(
    'data_matricula',
    ascending=False
)

df_matriculas = df_matriculas.drop_duplicates(
    subset=['matricula', 'periodo'],
    keep='first'
)

#Conferindo as duplicidades após a limpeza

duplicadas_apos_limpeza = df_matriculas.duplicated(
    subset=['matricula', 'periodo']
).sum()

print("\nDUPLICIDADES PÓS A LIMPEZA:")
print(duplicadas_apos_limpeza)

print("\nQUANTIDADE DE MATRÍCULAS APÓS A LIMPEZA:")
print(df_matriculas.shape)

#Salvando os dados tratados

df_matriculas.to_csv(
    'data/processed/matriculas_tratadas.csv',
    index=False,
    encoding='utf-8-sig'
)

print("\nDados tratados salvos com sucesso!")

#Tratando os dados dos alunos

df_alunos['data_nascimento'] = pd.to_datetime(
    df_alunos['data_nascimento']
)

#Verificando matrículas repetidas

duplicados_alunos = df_alunos['matricula'].duplicated().sum()

print("\nDUPLICIDADES NA TABELA DE ALUNOS:")
print(duplicados_alunos)

#Salvando os dados dos alunos tratados

df_alunos.to_csv(
    'data/processed/alunos_tratados.csv',
    index=False,
    encoding= 'utf-8-sig'
)

print("\nDados dos alunos salvos com sucesso!")

#Verificando matrículas repetidas nas informações acadêmicas

duplicados_academico = df_academico['matricula'].duplicated().sum()

print("\nDUPLICIDADES NAS INFORMAÇÕES ACADÊMICAS:")
print(duplicados_academico)

#Salvando as informações acadêmicas tratadas

df_academico.to_csv(
    'data/processed/informacoes_academicas_tratadas.csv',
    index=False,
    encoding='utf-8-sig'
)

print("\nInformações acadêmicas salvas com sucesso!")