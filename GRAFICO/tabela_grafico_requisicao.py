#Lucas dos Santos Unzer e Roger Henrique

import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from os import system
from time import sleep

response = requests.get('https://pt.wikipedia.org/wiki/Predefini%C3%A7%C3%A3o:Dados_da_pandemia_de_COVID-19')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    tabelas = pd.read_html(str(table))
    if tabelas:
        dados = tabelas[0]
        print(dados)
    else:
        print('Nenhum DataFrame encontrado na página.')
else:
    print(f'Erro ao acessar a página da web. Código de status: {response.status_code}')

colunas = list(dados.columns)
paises = dados[colunas[0]][10::-1].tolist()
casos = dados[colunas[1]][10::-1].tolist()
mortes = dados[colunas[2]][10::-1].tolist()

cores = ['red', 'orange', 'yellow', 'blue', 'purple']

while True:
    system('cls')
    print("=-" * 25)
    print("                DADOS DISPONÍVEIS")
    print("=-" * 25)
    print("Informe os dados que você deseja gerar o gráfico:")
    print('''
[1] - N° de casos da COVID-19 em cada país
[2] - N° de mortes por COVID-19 em cada país
    ''')
    opcData = int(input("=> ").strip().replace(" ", ""))
    if opcData == 1 or opcData == 2:
        break
    else:
        print("Opção inválida, tente novamente...")
        sleep(1)

while True:
    system('cls')
    print("=-" * 22)
    print("               TIPO DE GRÁFICO")
    print("=-" * 22)
    print("Informe o tipo de gráfico que deseja gerar:")
    print('''
    [1] - Gráfico de Barras
    [2] - Gráfico de Dispersão
    ''')
    opcGrafico = int(input("=> ").strip().replace(" ", ""))
    if opcGrafico == 1 or opcGrafico == 2:
        break
    else:
        print("Opção inválida, tente novamente...")
        sleep(1)

fig = plt.figure(figsize=(17, 7))
plot = fig.add_subplot(111)

def graficoBarras(data1, data2, lateral):
    plt.title('Gráfico de Barras')
    if lateral == 1:
        plt.ylabel('N° de Casos da COVID-19')
    elif lateral == 2:
        plt.ylabel('N° de Mortes pela COVID-19')
    plt.xlabel('Países')
    plt.bar(data1, data2, color=cores)
    plot.set_xticklabels(paises, rotation=20)
    plt.show()

def graficoDispersao(data1, data2, lateral):
    plt.title('Gráfico de Dispersão')
    if lateral == 1:
        plt.ylabel('N° de Casos da COVID-19')
    elif lateral == 2:
        plt.ylabel('N° de Mortes pela COVID-19')
    plt.xlabel('Países')
    plt.scatter(data1, data2)
    plot.set_xticklabels(paises, rotation=20)
    plt.show()
    
match opcGrafico:
    case 1:
        if opcData == 1:
            graficoBarras(paises, casos, 1)
            plt.ylabel('N° de casos da COVID-19')
        elif opcData == 2:
            graficoBarras(paises, mortes, 2)
            plt.ylabel('N° de morte pela COVID-19')
    case 2:
        if opcData == 1:
            graficoDispersao(paises, casos, 1)
        elif opcData == 2:
            graficoDispersao(paises, mortes, 2)
    case _:
        print("Opção inválida, tente novamente...")