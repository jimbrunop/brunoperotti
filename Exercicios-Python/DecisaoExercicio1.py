#Faça um Programa que peça dois números e imprima o maior deles. 

primeiro_numero = float(input("Informe o primeiro numero: "))
segundo_numero = float(input("Informe o segundo numero: "))

def valida_numero(primeiro_numero, segundo_numero):
    if primeiro_numero < segundo_numero:
       return print("o segundo numero é o maior: " + segundo_numero)
    elif primeiro_numero == segundo_numero:
        return print("os números são iguais")
    else:
        return print("o primeiro numero é o maior: " + primeiro_numero)
valida_numero(primeiro_numero, segundo_numero)