idade_mulheres = 0
idade_homens = 0
idade_total = 0
quantidade_mulheres = 0
quantidade_homens = 0


for i in range(10):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    sexo = input(f"Digite o sexo da {i+1}ª pessoa (M para masculino, F para feminino): ").upper()
    
    idade_total += idade
    
    if sexo == 'M':
        idade_homens += idade
        quantidade_homens += 1
    elif sexo == 'F':
        idade_mulheres += idade
        quantidade_mulheres += 1
    else:
        print("Sexo inválido. Use M ou F.")
        continue


if quantidade_mulheres > 0:
    media_idade_mulheres = idade_mulheres / quantidade_mulheres
else:
    media_idade_mulheres = 0

if quantidade_homens > 0:
    media_idade_homens = idade_homens / quantidade_homens
else:
    media_idade_homens = 0

if quantidade_mulheres + quantidade_homens > 0:
    media_idade_total = idade_total / (quantidade_mulheres + quantidade_homens)
else:
    media_idade_total = 0


print(f"Idade média das mulheres: {media_idade_mulheres:.2f}")
print(f"Idade média dos homens: {media_idade_homens:.2f}")
print(f"Idade média do grupo: {media_idade_total:.2f}")