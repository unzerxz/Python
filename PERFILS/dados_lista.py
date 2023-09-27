import pandas as pd

dados = pd.read_excel('Pasta1.xlsx')

minha_coluna = []

for indice, linha in dados.iterrows():
    valor = linha['Nome']
    minha_coluna.append(valor)
    
print(minha_coluna)
    