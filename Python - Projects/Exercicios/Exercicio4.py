#  Faça um algoritmo que imprima os números no intervalo entre 1 e 100: #

i=0
while(i<100):
    i+=1
    print(i)

print("fim1")

#Evolua o algoritmo no qual imprimimos os números num intervalo pré-definido para um algoritmo que pergunte ao usuário qual o intervalo que o mesmo deseja que seja impresso:

intervaloNum = int(input("informe um número que será o intervalo desejado "))

numeroInicio = 0
while(numeroInicio<100):
    numeroInicio+=intervaloNum
    print(numeroInicio)

print("fim2")



#aça um algoritmo que imprima os números no intervalo entre 1 e 10 em ordem inversa:#

ques3NumeroInicio = 100
while(ques3NumeroInicio > 0):
    ques3NumeroInicio -= 10
    print(ques3NumeroInicio)

print("fim3")


#Faça um algoritmo que imprima os números pares entre 0 e 100:

ques4Inicio = 0
while(ques4Inicio < 100):
    ques4Inicio+=2
    print(ques4Inicio)

print("fim4")


# Faça um algoritmo que imprima os números primos entre 0 e 100: #

primos = []  # Lista vazia de números primos

for numero in range(1, 101):
    contador = 0

    for numeroPrimo in range(1, numero + 1):  # Só precisa saber se o número é dividio por 1 e por ele mesmo.
        if numero % numeroPrimo == 0:
            contador = contador + 1  # Somar a quantidade de divisor

    if contador <= 2:
        primos.append(numero)  # Adiciona lista os numeros primos encontrados na lista
print(primos)

print("fim5")

# Faça um algoritmo que calcule os número primos num intervalo pré-determinado pelo usuário:#

countUser = int(input("Insira um intervalo "))

for numero in range(1, 101):
    countUser = 0

    for numeroPrimo in range(1, numero + 1):  # Só precisa saber se o número é dividio por 1 e por ele mesmo.
        if numero % numeroPrimo == 0:
            contador = countUser + 1  # Somar a quantidade de divisor

    if countUser <= 2:
        primos.append(numero)  # Adiciona lista os numeros primos encontrados na lista
print(primos)

print("fim5")


#Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra. Caso a letra seja o "q" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere "q" seja enviado:#

while(True):
    x = str(input("Estou em looping"))
    if(x=="p"):
        break