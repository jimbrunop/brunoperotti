#Escreva um algoritmo que contenha uma função de nome estudo() e que quando executada imprima na saída padrão a frase "Estamos estudando as funções":


def estudo():
    print("Estamos estudando as funções: ")


estudo()

print()

#Escreva um código contendo uma função de nome estudo e defina que a mesma deva receber um número como argumento. Chame este argumento de x. No corpo da função imprima a seguinte frase na tela: "Função invocada com sucesso. O valor passado pelo argumento x é: <valor de x>"

x = int(input("insira o primeiro numero: "))

def estudo(x):
    print("o valor de X é: ", x)


estudo(x)


print()

#screva um algoritmo que receba dois números através da declaração de dois parâmetros cujos nomes serão: x e y. No bloco de instrução faça a soma de ambos valores e imprima o resultado no monitor

y = int(input("insira o segundo numero: "))
def estudo(x,y):
    print("Resultado soma de", x, "e ", y, "é: ", x+y)

estudo(x,y)


print()

#Escreva um algoritmo contendo uma função que necessite de três argumentos. Em seguida, imprima na tela os argumentos em ordem ascendente e, por fim, imprima a média aritmética:

z = int(input("insira o terceiro numero: "))

listaArgs = [x,y,z]

def estudo(x,y,z):
    listaArgs.sort()
    print("a ordem ascendente dos argumentos é", listaArgs)

estudo(x,y,z)

print()

#screva uma função que contenha dois parâmetros. O primeiro deve ser obrigatório e o segundo facultativo:

def dados(nome, idade="idade não informada"):
    nome = input("Digite seu nome:")
    idade2 = input("Digite sua idade ou " + "s" + " para sair:")
    if idade2 == "s":
        print("Nome {}, {}.".format(nome, idade))  # Aplicação do parâmetro facultativo
    else:
        print("Nome {}, {} anos.".format(nome, idade2))

dados("nome")

print()

#Escreva uma função que invocará outra função na qual tenha dois parâmetros definidos. Invoque a primeira função de ``func1()`` e a segunda de ``func2()``. Em seguida, invoque os parâmetros da segunda função de x e y. Some x e y e retorne o resultado. Em func1(), ao receber o resultado, retorne-o também como valor de retorno da função. Por fim, imprima na tela o valor que foi calculado por func2(), retornado para func1() e retornado a quem invocou a função inicialmente:
def func1():
    def func2(x, y):
        a = x + y
        return (a)

    b = func2(10, 10)
    return (b)


resultado = func1()
print(resultado)

print(

)
#Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros. Em seguida, imprima os parâmetros recebidos na tela:

def lista(argsList):
    for v in listaArgs:
        print(v)

listaArgs = []
while True:
    listaArgs.append(input("Digite um valor ou 'S' para sair: "))
    if 'S' in listaArgs:
        listaArgs.remove('S')
        break
    lista(listaArgs)

print()

#Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros que estejam associados a uma chave. Em seguida, imprima na tela o nome da chave e o respectivo valor:






# Considere o trecho de código a seguir.
#
# def func(a, b, c, d)
#     print(a+b+c+d)
# lista = 1,2,3,4
# Invoque a função func(), passando como argumento os valores contidos em lista, com a respectiva ordem, de forma a utilizar o conceito de desempacotamento:

def func(a, b, c, d):
    print(a+b+c+d)
lista = 1,2,3,4

func(*lista)

print()

#Escreva um algoritmo que encontre o maior dentre 3 números. Para facilitar a resolução do exercício utilize funções.

listaArgs = [x,y,z]

def estudo(x,y,z):
    listaArgs.sort()
    print("O maior numero da lista é: ", listaArgs[-1])

estudo(x,y,z)

print()
# Escreva um função que some todos os números contidos numa lista.
# Lista: (1, 2, 3, 4, 5)
# Soma: 15

listaArgs = [x,y,z]

def estudo(x,y,z):
    listaArgs = x+y+z
    print("A soma é : ", listaArgs)

estudo(x,y,z)

print()
# Escreva uma função que multiplique todos os números de uma lista.
# Lista: (1, 2, 3, 4, 5)
# Multiplicação: 120

listaArgs = [x,y,z]

def estudo(x,y,z):
    listaArgs = x*y*z
    print("A multiplicacao é : ", listaArgs)

estudo(x,y,z)

# Escreva uma função que inverta a ordem dos elementos de uma lista manualmente. Não utilize a função interna do Python que faz inverção, crie o algoritmo que faça a inversão.
# Lista: "1234abcd"
# Saída: "dcba4321"

print()

def estudo(x,y,z):
    listaArgs.reverse()
    print("invertido : ", listaArgs)

estudo(x,y,z)



print()

#
# Escreva uma função que calcule o fatorial de um número (um inteiro não negativo). Envie o valor do número que
# será calculado como argumento da função.

def fatorial(x):
    f_texto = "{}! = {}".format(str(x), str(x))
    for f in range(x-1, 0, -1):
        x *= f
        f_texto += " x " + str(f)
    return "{} = {}".format(f_texto, x)

while True:
    x = int(input("Digite o número fatorial desejado ou 0 para encerrar: "))
    if x < 1: break
    resultado = fatorial(x)
    print(resultado)

print()

#Escreva uma função que verifique se um número está num intervalo determinado.

x=int(input('digite um numero que esteja no intervalo determinado:'))
def intervalo(x):
    if x>= 2 and x <=9:
        print('esta no intervalo determinado!')
    else:
        print('não esta no intervalo determinado!')
intervalo(x)


print()
#
# Escreva uma função que aceite Strings e calcule a quantidade de letras em mauisculas e minúsculas que a String possui.

a = input('Digite uma palavra com caracteres minusculas e maiusculas: ')
mm = 0
mn = 0


def contador(mm, mn, a):
    for v in list(a):
        letra = ord(v)
        if (letra >= 65 and letra <= 90):
            mm += 1
        elif (letra >= 97 and letra <= 122):
            mn += 1

    print('Valor de letras Maiusculas: ', mm,
          '\nValor de letras Minusculas:', mn,
          '\nPalavra digitada:', a)


contador(mm, mn, a)

