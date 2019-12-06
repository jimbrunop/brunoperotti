# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67


valor_divida = float(input("Informe o valor da dívida: R$ "))
def calcula_prazos_e_juros(valor_divida):
    valor_parcela_1x = 0
    valor_parcela_3x = (valor_divida*10/100)
    valor_parcela_6x = (valor_divida*15/100)
    valor_parcela_9x = (valor_divida*20/100)
    valor_parcela_12x = (valor_divida*25/100)

    print("Valor Divida " + " Valor dos juros " + "Quantidade de Parcelas " + " Valor Parcela")
    print("R$" +  str((valor_divida + valor_parcela_1x)) + " R$"  + str(valor_parcela_1x) + str(1) + " R$" + str(
        valor_divida))
    print("R$" + str((valor_divida + valor_parcela_3x)) + " R$" + str(valor_parcela_3x) + str(3) + " R$" + str(
        (valor_divida + valor_parcela_3x)/3))
    print("R$" + str((valor_divida + valor_parcela_6x)) + " R$" + str(valor_parcela_6x) + str(6) + " R$" + str(
        (valor_divida + valor_parcela_6x)/6))
    print("R$" + str((valor_divida + valor_parcela_9x)) + " R$" + str(valor_parcela_9x) + str(9) + " R$" + str(
        (valor_divida + valor_parcela_9x)/9))
    print("R$" + str((valor_divida + valor_parcela_12x)) + " R$" + str(valor_parcela_12x) + str(12) + " R$" + str(
        (valor_divida + valor_parcela_12x)/12))


calcula_prazos_e_juros(valor_divida)
