# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

index = 0
lista_numeros = []

def pede_numero(index):
    qtdade_par = 0
    qtdade_impar = 0
    while index < 10:
        numero = int(input("Informe um numero inteiro: "))
        lista_numeros.append(numero)
        index += 1
        if numero % 2 == 0:
            qtdade_par += 1
        else:
            qtdade_impar += 1
    print(lista_numeros)
    print("quantidade pares: " + str(qtdade_par))
    print("quantidade impares: " + str(qtdade_impar))
pede_numero(index)




