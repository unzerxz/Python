from datetime import date

today = date.today()

#acessando o atributo ano 
atual = int(today.strftime("%Y"))

nome = input('Olá, qual seu nome?')
print(f'Prazer {nome}','!')
#atual = int(input('Qual o ano atual?'))
n1 = int(input('Qual seu ano de nascimento?'))
idade = atual - n1
print(f'{nome} sua idade é {idade} anos')
if idade >= 18:
    print('Você ja pode tirar carta, finalmente!!!')
else:
    print('AAAA vc ainda nao pode tirar carta, infelizmente')
