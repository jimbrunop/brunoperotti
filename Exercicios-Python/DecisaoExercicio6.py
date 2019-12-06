#Faça um Programa que leia três números e mostre o maior deles.

numero_1 = float(input("informe o primeiro numero"))
numero_2 = float(input("informe o segundo numero"))
numero_3 = float(input("informe o terceiro numero"))

def valida_maior_numero(numero_1, numero_2, numero_3):
    if numero_1 > numero_2 and numero_1 > numero_3:
        print("o maior numero digitado foi " + str(numero_1))
    elif numero_2 > numero_1 and numero_2 > numero_3:
        print("o maior numero digitado foi " + str(numero_2))
    else:
        print("o maior numero digitado foi " + str(numero_3))
valida_maior_numero(numero_1, numero_2, numero_3)