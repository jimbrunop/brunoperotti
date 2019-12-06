# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

numero_maximo = 20
numero_minimo = 1
listagem = []

while numero_minimo != numero_maximo:
    print(numero_minimo)
    listagem.append(numero_minimo)
    numero_minimo += 1
else:
    print (listagem)