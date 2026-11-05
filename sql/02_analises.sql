-- 1. Quantidade de alunos por curso

SELECT
    curso,
    COUNT(*) AS quantidade_alunos
FROM informacoes_academicas
GROUP BY curso
ORDER BY quantidade_alunos DESC;


-- 2. Total de alunos

SELECT
    COUNT(*) AS total_alunos
FROM alunos;


-- 3. Quantidade de matrículas por situação

SELECT
    status,
    COUNT(*) AS quantidade
FROM matriculas
GROUP BY status
ORDER BY quantidade DESC;


-- 4. Quantidade de matrículas por período

SELECT
    periodo,
    COUNT(*) AS quantidade_matriculas
FROM matriculas
GROUP BY periodo
ORDER BY quantidade_matriculas DESC;

-- 5. Quantidade de matrículas por curso

SELECT
    a.curso,
    COUNT(*) AS total_matriculas
FROM matriculas AS m
INNER JOIN informacoes_academicas AS a
    ON m.matricula = a.matricula
GROUP BY a.curso
ORDER BY total_matriculas DESC;

-- 6. Quantidade de matrículas por curso e situação

SELECT
    a.curso,
    m.status,
    COUNT(*) AS quantidade_matriculas
FROM matriculas AS m
INNER JOIN informacoes_academicas AS a
    ON m.matricula = a.matricula
GROUP BY a.curso, m.status
ORDER BY a.curso, quantidade_matriculas DESC;


-- 7. Lista de alunos, cursos e situação das matrículas

SELECT
    al.nome,
    a.curso,
    m.periodo,
    m.status
FROM matriculas AS m
INNER JOIN alunos AS al
    ON m.matricula = al.matricula
INNER JOIN informacoes_academicas AS a
    ON m.matricula = a.matricula
ORDER BY a.curso, al.nome;