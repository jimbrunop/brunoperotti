#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco_prod_1 = float(input("Insira o valor do produto 1 R$: "))
preco_prod_2 = float(input("Insira o valor do produto 2 R$: "))
preco_prod_3 = float(input("Insira o valor do produto 3 R$: "))


def valida_menor_preco(preco_prod_1, preco_prod_2, preco_prod_3):
    if preco_prod_1 < preco_prod_2 and preco_prod_1 < preco_prod_3:
        menor_preco = preco_prod_1
    elif preco_prod_2 < preco_prod_1 and preco_prod_2 < preco_prod_3:
        menor_preco = preco_prod_2
    else:
        menor_preco = preco_prod_3
    return menor_preco

print("o valor mais baixo é R$: " + str(valida_menor_preco(preco_prod_1, preco_prod_2, preco_prod_3)))
