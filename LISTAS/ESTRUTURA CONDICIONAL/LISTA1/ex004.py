nome = input('Qual seu nome ?? ')
ano = int(input(f'Prazer {nome}, qual seu ano de nascimento?? '))
idade = (2023 - ano)

if idade >= 18:
    {
        print('PARABENS, VC É MAIORZINHO')
    }
else: 
    {
        print('QUE PENA, AINDA É BEBE')
    }