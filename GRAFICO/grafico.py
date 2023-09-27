import matplotlib.pyplot as plt
anos = ['2016', '2017', '2018', '2019', '2020', '2021', '2022']
maior = [422, 880, 2048, 2799, 319, 1921, 955]
menor = [166, 619, 622, 159, 8, 158, 760]

#criar uma figura e um eixo
fig, ax = plt.subplots()

#plotar os dados com as personalizações
ax.plot(anos, maior, color='red', linestyle='--', marker='o', label='maior bilheteria')
ax.plot(anos, menor, color='blue', linestyle='--', marker='o', label='menor bilheteria')

#adicionar rotulos e titulos
ax.set_xlabel('ano')
ax.set_ylabel('bilheteria (em milhões de US$))')
ax.set_title('crescimento das bilheterias')

#incluir uma legenda
ax.legend()
#mostrar o grafico
plt.show()