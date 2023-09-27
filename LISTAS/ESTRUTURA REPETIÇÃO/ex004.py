while True:
    nome = input("Digite seu nome: ")
    codigo = input("Digite seu código pessoal: ")

    if nome == codigo:
        print("Erro: O código não pode ser igual ao nome. Por favor, tente novamente.")
    else:
        break

print("Nome:", nome)
print("Código pessoal:", codigo)