# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

ultimo_numero = 50
index = 1
listagem_numero = []

def executa_numeros_impares(index, ultimo_numero):
    while index <= ultimo_numero:
        listagem_numero.append(index)
        index += 2
    print(listagem_numero)
executa_numeros_impares(index, ultimo_numero)