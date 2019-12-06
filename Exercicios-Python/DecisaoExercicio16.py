# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#
#     Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#     Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#     Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#     Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

valor_a = int(input('Informe o valor de A: '))

if (valor_a == 0):
    print('Não é uma equação de segundo grau')
else:
    valor_b = int(input('Valor de B: '))
    valor_c = int(input('Valor de C: '))
    delta = valor_b * valor_b - (4 * valor_a * valor_c)

    if delta < 0:
        print('Delta menor que 0. Raízes imaginárias. Tchau')
    elif delta == 0:
        raiz = -valor_c / (2 * valor_a)
        print('Delta=0 , raiz = ', raiz)
    else:
        valor_raiz_1 = (-valor_b + math.sqrt(delta)) / (2 * valor_a)
        valor_raiz_2 = (-valor_b - math.sqrt(delta)) / (2 * valor_a)
        print('Raizes: ', valor_raiz_1, ' e ', valor_raiz_2)