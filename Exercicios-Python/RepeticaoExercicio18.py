#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

listagem_numeros = []

def cria_conjunto(quantidade_numeros):
    contador = 1
    while quantidade_numeros >= contador:
        numero = int(input("Informe um numero para o conjunto: "))
        listagem_numeros.append(numero)
        contador += 1

def ordena_maior_menor(listagem_numeros):
    listagem_numeros.sort(key=int, reverse=True)
    print("O maior numero informado é: " + str(listagem_numeros[0]))
    print("O menor numero informado é: " + str(listagem_numeros[-1]))

def calcula_soma(listagem_numeros):
    resultado_soma = listagem_numeros[0] + listagem_numeros[-1]
    print("A soma do maior e o menor número é: " + str(resultado_soma))

quantidade_numeros = int(input("Informe a quantidade de numeros que voce deseja que possua o conjunto: "))

cria_conjunto(quantidade_numeros)
ordena_maior_menor(listagem_numeros)
calcula_soma(listagem_numeros)



