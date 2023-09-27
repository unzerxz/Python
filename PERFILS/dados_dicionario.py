import pandas as pd

dados = pd.read_excel('Pasta1.xlsx')
dados.set_index('Nome', inplace=True)

num_teste = input("Qual teste deseja salvar?")
teste = 'teste' + num_teste
dicionario = {}

for indice, linha in dados.iterrows():
    chave = indice
    valor = linha[teste]
    dicionario[chave] = valor

print(dicionario)