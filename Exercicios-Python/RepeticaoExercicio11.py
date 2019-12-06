# Altere o programa anterior para mostrar no final a soma dos números.

numero_1 = int(input("Informe um numero: "))
numero_2 = int(input("Informe um segundo numero: "))
lista_numeros = []

def valida_intervalo(numero_1, numero_2):
    while numero_1 <= numero_2:
        lista_numeros.append(numero_1)
        numero_1 += 1
valida_intervalo(numero_1,numero_2)

def soma_listagem(lista_numeros):
    soma = 0
    for index in lista_numeros:
        soma += index
    print("A soma dos numeros da listagem é: " + str(soma))
soma_listagem(lista_numeros)