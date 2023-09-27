
maior_valor = float('-inf')  
menor_valor = float('inf')   


for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    

    if valor > maior_valor:
        maior_valor = valor
    
   
    if valor < menor_valor:
        menor_valor = valor


soma = 0
for i in range(10):
    soma += valor

media = soma / 10


print(f"O maior valor é: {maior_valor}")
print(f"O menor valor é: {menor_valor}")
print(f"A média dos valores é: {media}")