import pandas as pd

dados = pd.read_excel('Perfil1.xlsx')
dados.set_index("Nome", inplace=True)

num_teste = input("Qual teste deseja salvar?")
teste = 'teste' + num_teste

coluna_teste1 = tuple(dados[teste])

print(coluna_teste1)