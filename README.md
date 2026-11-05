# Pipeline de Dados para Gestão Acadêmica

## Sobre o projeto

Este projeto tem como objetivo desenvolver um pipeline de dados para gestão acadêmica, utilizando Python, Pandas e PostgreSQL.

O pipeline realiza a geração de dados fictícios, extração, transformação, limpeza e carregamento dos dados em um banco de dados relacional, permitindo consultas e análises por meio de SQL.

O projeto foi desenvolvido como parte dos meus estudos em Engenharia de Dados, com foco na aplicação prática dos conceitos de ETL (Extract, Transform, Load).

## Tecnologias utilizadas

- Python
- Pandas
- PostgreSQL
- SQL
- SQLAlchemy
- Psycopg2
- Faker
- Pytest
- Git e GitHub

## Estrutura do projeto

```text
Pipeline Gestão Acadêmica/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── sql/
│   ├── 01_criar_tabelas.sql
│   └── 02_analises.sql
│
├── src/
│   ├── gerar_dados.py
│   ├── extrair_dados.py
│   ├── transformar_dados.py
│   ├── testar_conexao.py
│   ├── carregar_dados.py
│   └── validacoes.py
│
├── tests/
│   └── test_validacoes.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Etapas do pipeline

### 1. Geração de dados

Utilização da biblioteca Faker para criar dados acadêmicos fictícios, incluindo:

- Alunos;
- Informações acadêmicas;
- Matrículas.

Foram gerados 1.000 alunos e 1.500 registros de matrículas.

### 2. Extração

Leitura dos arquivos CSV utilizando Pandas.

### 3. Transformação e limpeza

Tratamento dos dados, incluindo:

- Verificação de valores ausentes;
- Identificação de registros duplicados;
- Conversão de tipos de dados;
- Remoção de matrículas duplicadas, considerando aluno e período acadêmico.

Para registros duplicados, foi mantida a matrícula com a data de registro mais recente.

Após o tratamento, foram obtidos 1.258 registros de matrículas.

### 4. Carregamento

Conexão com PostgreSQL utilizando SQLAlchemy e Psycopg2 para armazenar os dados tratados em tabelas relacionais.

### 5. Análises SQL

Desenvolvimento de consultas SQL para analisar:

- Quantidade de alunos por curso;
- Total de alunos;
- Matrículas por situação;
- Matrículas por período;
- Matrículas por curso;
- Matrículas por curso e situação;
- Relação de alunos, cursos e matrículas.

## Testes

Foram implementados testes automatizados utilizando Pytest para validar:

- Remoção de registros duplicados;
- Identificação de valores ausentes;
- Verificação de dados sem valores ausentes.

Os testes foram executados com sucesso.

## Como executar o projeto

### Pré-requisitos

- Python instalado;
- PostgreSQL instalado e configurado;
- Git instalado.

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Criar o ambiente virtual

No terminal, dentro da pasta do projeto:

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Gerar os dados

```bash
python .\src\gerar_dados.py
```

### 6. Extrair e transformar os dados

```bash
python .\src\extrair_dados.py
```

```bash
python .\src\transformar_dados.py
```

### 7. Configurar o banco de dados

Crie o banco de dados PostgreSQL com o nome:

`gestao-academica`

Execute o script `sql/01_criar_tabelas.sql` no banco de dados para criar as tabelas.

### 8. Testar a conexão

```bash
python .\src\testar_conexao.py
```

### 9. Carregar os dados

```bash
python .\src\carregar_dados.py
```

Atenção: a carga utiliza inserção de dados (`append`). Execute em tabelas vazias na primeira carga. Não execute novamente sem preparar as tabelas para evitar conflitos de chaves primárias.

### 10. Executar os testes

```bash
python -m pytest -v
```

## Resultados

O projeto foi desenvolvido e testado com dados fictícios, apresentando os seguintes resultados:

- 1.000 alunos cadastrados;
- 1.000 registros de informações acadêmicas;
- 1.258 matrículas após o tratamento;
- 3 testes automatizados aprovados.

## Próximas melhorias

- Implementação de Docker para facilitar a configuração e execução do ambiente;
- Ampliação dos testes automatizados;
- Aprimoramento das validações de qualidade dos dados.

## Autora

Projeto desenvolvido como parte dos meus estudos em Engenharia de Dados.