# Faça um programa que leia 5 números e informe o maior número.

index = 1
listagem_de_numero = []


def valida_maior_numero(index):
    while index <= 5:
        num = int(input("Informe o proximo numero: "))
        listagem_de_numero.append(num)
        index += 1
    listagem_de_numero.sort(key=int)
    print("O maior numero inserido foi: " + str(listagem_de_numero[-1]))
valida_maior_numero(index)