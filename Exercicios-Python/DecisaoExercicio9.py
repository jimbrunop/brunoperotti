#Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero_1 = float(input("Informe o primeiro numero"))
numero_2 = float(input("Informe o segundo numero"))
numero_3 = float(input("Informe o terceiro numero"))
listagem_numeros = []

def insere_valores_listagem (numero_1, numero_2, numero_3):
    listagem_numeros.append(numero_1)
    listagem_numeros.append(numero_2)
    listagem_numeros.append(numero_3)
insere_valores_listagem(numero_1, numero_2, numero_3)

listagem_numeros.sort(key=float, reverse=True)
print(listagem_numeros)
