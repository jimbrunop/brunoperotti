# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#
#     Álcool:
#     até 20 litros, desconto de 3% por litro
#     acima de 20 litros, desconto de 5% por litro
#     Gasolina:
#     até 20 litros, desconto de 4% por litro
#     acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros_vendidos = float(input("Informe quantos litros foram inseridos: "))
tipo_combustivel = input("Informe o tipo de combustivel, g - gasolina ou a - alcool")
preco_litro_gasolina = 2.50
preco_litro_alcool = 1.90

def calcula_valor_abastecimento (litros_vendidos, tipo_combustivel, preco_litro_gasolina, preco_litro_alcool):
    if tipo_combustivel == 'g' or tipo_combustivel == 'G':
        valor_abastecido = (litros_vendidos * preco_litro_gasolina)
        if litros_vendidos <= 20.00:
            valor_com_desconto = valor_abastecido - (valor_abastecido * 4) / 100
            print(
                "Foram abastecidos: " + str(litros_vendidos) + "com valor de R$: " + str(valor_abastecido) + "Aplicando deesconto: R$" + str(valor_com_desconto))
        else:
            print(
                "Foram abastecidos: " + str(litros_vendidos) + "com valor de R$: " + str(valor_abastecido))
    elif tipo_combustivel == 'a' or tipo_combustivel == 'A':
        valor_abastecido = (litros_vendidos * preco_litro_alcool)
        if litros_vendidos <= 20.00:
            valor_com_desconto = valor_abastecido - (valor_abastecido * 3)/100
            print("Foram abastecidos: " + str(litros_vendidos) + "com valor de: R$ " + str(valor_abastecido) + "Aplicando deesconto: R$" + str(valor_com_desconto))
        else:
            print("Foram abastecidos: " + str(litros_vendidos) + "com valor de: R$" + str(valor_abastecido))

    else:
        print("Tipo combustivel inválido")
calcula_valor_abastecimento (litros_vendidos, tipo_combustivel, preco_litro_gasolina, preco_litro_alcool)