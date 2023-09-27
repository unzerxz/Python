from datetime import date
nome = input('Qual e o seu nome?\n> ')
nascimento = int(input('Qual ano você nasceu?\n> '))
hoje = date.today()
atual = int(hoje.strftime('%Y'))
idade = atual - nascimento

if idade >= 18:
    maior = True
elif idade < 0:
    print('Insira um valor válido.')
else:
    maior = False
    
cadastro = {}
cadastro.update({'nome': nome, 'idade': idade, 'maior': maior})
#print(cadastro)

print("Seu nome é", cadastro.get('nome'))
print("Sua idade é", cadastro.get('idade'), "anos")

if cadastro.get('maior') == True:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
