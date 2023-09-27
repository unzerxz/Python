
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


subtracao = float(input("Digite o resultado da subtração ({} - {}): ".format(numero1, numero2)))
multiplicacao = float(input("Digite o resultado da multiplicação ({} * {}): ".format(numero1, numero2)))
divisao = float(input("Digite o resultado da divisão ({} / {}): ".format(numero1, numero2)))


resultado_subtracao = numero1 - numero2
resultado_multiplicacao = numero1 * numero2
resultado_divisao = numero1 / numero2


if subtracao == resultado_subtracao:
    {
    print("Resposta correta para a subtração!")
    }
else:
    print("Resposta incorreta para a subtração. O valor correto é:", resultado_subtracao)

if multiplicacao == resultado_multiplicacao:
    print("Resposta correta para a multiplicação!")
else:
    print("Resposta incorreta para a multiplicação. O valor correto é:", resultado_multiplicacao)

if divisao == resultado_divisao:
    print("Resposta correta para a divisão!")
else:
    print("Resposta incorreta para a divisão. O valor correto é:", resultado_divisao)