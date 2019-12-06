# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input("Informe um numero"))

def valida_decimal(numero):
    if round(numero) == numero:
        print("numero inteiro")
    else:
        print("numero decimal")
valida_decimal(numero)