def remover_duplicatas(df, colunas):
    return df.drop_duplicates(subset=colunas)

def tem_valores_ausentes(df):
    return df.isnull().values.any()