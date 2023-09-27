import pandas as pd

dados = pd.read_excel('perfis_lp.xlsx')

print(dados)

indice = int(input('Qual teste deseja mostrar? Digite uma linha: '))

print(dados.loc[[indice]])