import pandas as pd
import random
from faker import Faker

fake = Faker('pt_BR')

random.seed(42)
fake.seed_instance(42)

#Quantidade de registros

QUANTIDADE_ALUNOS = 1000
QUANTIDADE_MATRICULAS = 1500

#Gerando dados dos alunos

alunos = []

for i in range(QUANTIDADE_ALUNOS):

    aluno = {
        'matricula': 10001 + i,
        'nome': fake.name(),
        'data_nascimento': fake.date_of_birth(minimum_age=17, maximum_age=60),
        'email': fake.email()
    }

    alunos.append(aluno)

    df_alunos = pd.DataFrame(alunos)
    
    print(df_alunos.head())

    df_alunos.to_csv('data/raw/alunos.csv', index=False, encoding='utf-8-sig')

#Gerando informações acadêmicas
    
    cursos = [
        'Administração',
        'Psicologia',
        'Enfermagem',
        'Direito',
        'Ciências Contábeis',
        'Sistemas de  Informação',
        'Psicologia',
        'Educação Física',
        'Engenharia Civil',
        'Nutrição',
    ]

turmas = [f'Turma {i:02d}' for i in range(1, 31)]
turnos = ['Manhã', 'Tarde', 'Noite']
modalidades = ['Presencial', 'EAD', "Semipresencial"]
unidades = ['Unidade Centro','Unidade Norte','Unidade Sul',]
informacoes_academicas = []
for matricula in df_alunos['matricula']:
    informacao = {
        'matricula': matricula,
        'curso': random.choice(cursos),
        'turma': random.choice(turmas),
        'turno': random.choice(turnos),
        'modalidade':random.choice(modalidades),
        'unidade':random.choice(unidades),
    }
    informacoes_academicas.append(informacao)
df_academico = pd.DataFrame(informacoes_academicas)

#Salvando informações acadêmicas

df_academico.to_csv(
    'data/raw/informacoes_academicas.csv',
    index=False,
    encoding='utf-8-sig'
)

print(df_academico.head())

#Gerando dados das matrículas

status_matricula = [
    'Ativa',
    'Cancelada',
    'Trancada'
]

periodos = [
    '2025.1',
    '2025.2',
    '2026.1',
    '2026.2'
]

matriculas = []

for i in range(QUANTIDADE_MATRICULAS):

    matricula = {
        'matricula': random.choice(df_alunos['matricula']),
        'data_matricula': fake.date_between(
            start_date='-2y',
            end_date='today'
        ),
        'status': random.choice(status_matricula),
        'periodo': random.choice(periodos)
    }

    matriculas.append(matricula)

#Tranformando em DataFrame

df_matriculas = pd.DataFrame(matriculas)

#Salvando informações das matrículas

df_matriculas.to_csv(
    'data/raw/matriculas.csv',
    index=False,
    encoding='utf-8-sig'
)

print(df_matriculas.head())