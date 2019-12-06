#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

numero_1 = int(input("Informe um numero: "))
numero_2 = int(input("Informe um segundo numero: "))
lista_numeros = []

def valida_intervalo(numero_1, numero_2):
    while numero_1 <= numero_2:
        lista_numeros.append(numero_1)
        numero_1 += 1
    print("numeros dentro do intervalo: " + str(lista_numeros))
valida_intervalo(numero_1,numero_2)