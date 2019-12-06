# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


def valida_numero():
    numero = float(input("informe um numero de 0 a 10: "))
    while (numero > 10) or (numero < 0):
        numero = float(input("informe um numero de 0 a 10: "))
    else:
        print("o valor bateu")
valida_numero()
