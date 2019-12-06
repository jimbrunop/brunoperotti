#Faça um Programa que leia três números e mostre o maior e o menor deles.

numero_1 = float(input("informe o primeiro numero"))
numero_2 = float(input("informe o segundo numero"))
numero_3 = float(input("informe o terceiro numero"))

def valida_maior(numero_1, numero_2, numero_3):
    if numero_1 > numero_2 and numero_1 > numero_3:
        maior = numero_1
    elif numero_2 > numero_3 and numero_2 > numero_1:
        maior = numero_2
    else:
        maior = numero_3
    return maior


def valida_menor(numero_1, numero_2, numero_3):
    if numero_1 < numero_2 and numero_1 < numero_3:
        menor = numero_1
    elif numero_2 < numero_3 and numero_2 < numero_1:
        menor = numero_2
    else:
        menor = numero_3
    return menor

print(valida_maior(numero_1, numero_2, numero_3))
print(valida_menor(numero_1, numero_2, numero_3))