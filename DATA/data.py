import requests
from datetime import datetime, time

url = 'https://worldtimeapi.org/api/ip'

try:
    response = requests.get(url)
    data = response.json()

    dia = data["datetime"][9:10]
    mes = data["datetime"][6:7]
    ano = data["datetime"][:4]
    zona = data["timezone"]
    endereco_ip = data["client_ip"]
    
    print("Data:" dia, "/", mes, "/", ano)
    print("Zona: ", data["timezone"])
    print("Endereço IP: ", endereco_ip)
    
except Exception as erro:
    print('Ocorreu um erro:', erro)
