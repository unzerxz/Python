import requests
url = 'https://worldtimeapi.org/api/ip'
try:
    response = requests.get(url)
    data = response.json()
    dia = data["datetime"][8:10]
    mes = data["datetime"][6:7]
    zona = data["timezone"]
    endereco_ip = data["client_ip"]
    ano = int(data["datetime"][:4])

    nome = input('Qual e o seu nome?\n> ')

    nascimento = int(input('Qual ano você nasceu?\n> '))

    idade = ano - nascimento

    if idade >= 18:
        maior = True
    elif idade < 0:

     print('Insira um valor válido.')

    else: 

        maior = False

    cadastro = {}
    cadastro.update({'nome': nome, 'idade': idade, 'maior': maior})

    print("Seu nome é", cadastro.get('nome'))
    print("Sua idade é", cadastro.get('idade'), "anos")

    if cadastro.get('maior') == True:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")
        print("Data:", dia, "/", mes, "/", ano)
        print("Zona: ", data["timezone"])
        print("Endereço IP: ", endereco_ip)

except Exception as erro:
        print('Ocorreu um erro:', erro)
