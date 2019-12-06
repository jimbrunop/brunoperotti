#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

valor_regulamento_maximo = 50
multa_por_kg = 4.00
peso_trazido = float(input("informe o valor em Kg trazidos:"))

if peso_trazido > valor_regulamento_maximo:
    valor_excedido = peso_trazido - valor_regulamento_maximo
    valor_multa_total = valor_excedido * multa_por_kg
    print("a quantidade trazida foi de " + str(peso_trazido) + "Kg, qtdade excedida foi de " + str(valor_excedido) + "Kg, e a multa foi de R$ " + str(valor_multa_total))
else:
    print("ta tudo certo, dentro da quantidade de 50kg")
    