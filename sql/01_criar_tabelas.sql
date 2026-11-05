CREATE TABLE alunos (
matricula INTEGER PRIMARY KEY,
nome VARCHAR(150),
data_nascimento DATE,
email VARCHAR(255)
);

CREATE TABLE informacoes_academicas (
matricula INTEGER PRIMARY KEY,
curso VARCHAR(100),
turma VARCHAR(50),
turno VARCHAR(30),
modalidade VARCHAR(50),
unidade VARCHAR(100),

FOREIGN KEY (matricula) REFERENCES alunos(matricula)
);

CREATE TABLE matriculas (
matricula INTEGER,
data_matricula DATE,
status VARCHAR(20),
periodo VARCHAR(10),

PRIMARY KEY (matricula, periodo),
FOREIGN KEY (matricula) REFERENCES alunos(matricula)
);