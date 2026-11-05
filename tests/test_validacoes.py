import pandas as pd
from src.validacoes import remover_duplicatas, tem_valores_ausentes


def test_remover_duplicatas():
    dados = pd.DataFrame({
        'matricula': [1, 2, 2, 3],
        'nome': ['Ana', 'Bruno', 'Bruno', 'Carlos']
    })

    resultado = remover_duplicatas(dados, ['matricula'])

    assert len(resultado) == 3
    assert resultado['matricula'].tolist() == [1, 2, 3]


def test_tem_valores_ausentes():
    dados = pd.DataFrame({
        'nome': ['Ana', None, 'Carlos']
    })

    resultado = tem_valores_ausentes(dados)

    assert resultado == True


def test_sem_valores_ausentes():
    dados = pd.DataFrame({
        'nome': ['Ana', 'Bruno', 'Carlos']
    })

    resultado = tem_valores_ausentes(dados)

    assert resultado == False