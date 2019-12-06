# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

numero = float(input("Informe um numero"))

def valida_par_impar(numero):
    if numero%2 == 0:
        print("Numero par")
    else:
        print("Numero impar")
valida_par_impar(numero)