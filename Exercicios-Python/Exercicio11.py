#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    #
    # o produto do dobro do primeiro com metade do segundo .
    # a soma do triplo do primeiro com o terceiro.
    # o terceiro elevado ao cubo.

valor_int_1 = int(input("Informe o primeiro numero (inteiro)"))
valor_int_2 = int(input("Informe o segundo numero (inteiro)"))
valor_float_3 = float(input("Informe o terceiro numero (real)"))

questao_a = (2 * valor_int_1) * (valor_int_2 / 2)
questao_b = float((3 * valor_int_1)) + (valor_float_3)
questao_c = (valor_float_3 ** 3)


print("o produto do dobro do primeiro com metade do segundo " + str(questao_a))
print("a soma do triplo do primeiro com o terceiro " + str(questao_b))
print(" terceiro elevado ao cubo" + str(questao_c))