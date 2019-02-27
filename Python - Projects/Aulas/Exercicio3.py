#Faça um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero.#

numer1 = int(input("Digite um numero"))

if(numer1>0):
    print("Este número é positivo")
elif(numer1<0):
    print("Este número é negativo")
else:
    if(numer1==0):
        print("o número é igual a zero")

print()
#Faça um algoritmo que leia um número e mostre se o mesmo é par ou ímpar.

if(numer1%2==0):
    print("número par")
else:
    print("numero impar")

# Faça um algoritmo que leia dois números e imprima o maior.#

numer2 = int(input("digite um segundo número"))

if(numer1>numer2):
    print("O numero %d é maior que o numero %d " %(numer1, numer2))

print()

#Faça um algoritmo que peça a idade de uma pessoa e imprima na tela se a mesma já é maior de idade ou então, se a mesma é de menor.#
idade1 = int(input("Digite sua idade"))
maiorDeIdade = 18

if(idade1>=maiorDeIdade):
    print("Você tem %d anos, logo é maior de idade " %(idade1))
else:
    print("Você tem %d anos, logo, é menor de idade " %(idade1))

print()

#Faça um algoritmo que peça a idade do usuário e a idade da sua mãe. Em seguida, imprima na tela com quantos anos sua mãe o teve.#
idadeMae = int(input("Digite agora a idade de sua mãe"))

idadeNascimento = idadeMae - idade1
print("a idade de sua mae é %d , a sua é %d, neste caso você nasceu quando sua mãe tinha %d anos" %(idadeMae,idade1,idadeNascimento))

#Faça um algoritmo que imprima 50 vezes o caractere "-" na tela (sem a utilização de laços de repetição)#
print()
if(True):
    print("--------------------------------------------------------------------------------------------------------------")

print()

#Faça um algoritmo que peça dois números. Primeiro, imprima o maior e, em seguida, o menor.#

if(numer1>numer2):
    print(numer1)
elif(numer2>numer1):
    print(numer2)
else:
    if(numer1==numer2):
        print("os números são iguais")

print()

