# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.


listagem_numeros = []

def cria_conjunto(quantidade_numeros):
    contador = 1
    while quantidade_numeros >= contador:
        numero = int(input("Informe um numero para o conjunto: "))
        if numero > 0 and numero <= 1000:
            listagem_numeros.append(numero)
            contador += 1
        else:
            print("Informe um numero válido, maior que 0 e menor que 1000")

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

