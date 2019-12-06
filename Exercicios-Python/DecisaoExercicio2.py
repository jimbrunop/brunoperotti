#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input("informe um numero"))

def valida_positivo_negativo(valor):
    if valor >= 0:
        print("Valor positivo")
    else:
        print("Valor negativo")
valida_positivo_negativo(valor)