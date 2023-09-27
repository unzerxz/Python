import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
#instale as bibliotecas bs4,lxml e html5lib
# URL da página da web contendo os dados HTML
    # Altere a url abaixo para a página que contém os dados que deseja utilizar em formato de tabela HTML
url = ('https://pt.wikipedia.org/wiki/Lista_de_jogos_eletrônicos_mais_vendidos')
    # Faça uma solicitação GET para obter o conteúdo HTML da página
response = requests.get(url)
    # Verifique se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
        # Analise o conteúdo HTML com BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
        # Encontre a tabela ou elemento que contém os dados que você deseja extrair
    table = soup.find('table')
        # Use o método read_html do pandas para converter a tabela HTML em um DataFrame
    tabelas = pd.read_html(str(table))
        # Verifique se foram encontrados DataFrames
    if tabelas:
            # Normalmente, o primeiro DataFrame é o que você deseja
        bilheteria = tabelas[0]
            # Agora você tem os dados em um DataFrame que pode ser manipulado
        print(bilheteria.head())
            # Você pode salvar o DataFrame em um arquivo CSV, Excel, etc.
            # df.to_csv('dados_extraidos.csv', index=False)
    else:
            print('Nenhum DataFrame encontrado na página.')
else:
    print(f'Erro ao acessar a página da web. Código de status: {response.status_code}')
    # Cria uma lista com o nome de todas colunas do dataframe
colunas_bil = list(bilheteria.columns)
print(colunas_bil)
    # Selecione as colunas que deseja usar, limitando a quantidade de itens
ranking = bilheteria[colunas_bil[0]][:10].tolist()
ano = bilheteria[colunas_bil[1]][:10].tolist()
filme = bilheteria[colunas_bil[2]][:10].tolist()
dolares = bilheteria[colunas_bil[4]][:10].tolist()

cores = ['red', 'orange', 'yellow', 'blue', 'purple']
cores = ['red', 'orange', 'yellow', 'blue', 'purple']
    # Plota um gráfico comum de linha a partir de duas listas
#plt.plot(ano, dolares)
    # Plota um gráfico de barras 
#plt.bar(dolares, filme, color=cores)
    # Plota um gráfico de dispersão
#plt.scatter(ano, ranking)
    # Plota um histograma
plt.hist(ano)
plt.show()