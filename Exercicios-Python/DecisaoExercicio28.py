# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#
#                           Até 5 Kg           Acima de 5 Kg
#     File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#     Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#     Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#
#     Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


tipo_carne = input("Informe o tipo da carne: f - file duplo, a - alcatra ou p - picanha")
quantidade_solicitada = float(input("Informe a quantidade desejada em Kg: "))
forma_pgto = input("Qual seria forma de pagto? 1 - Cartão tabajara ou 2 - outra forma")

def verifica_valor_tipo_carne(tipo_carne, quantidade_solicitada):
    if tipo_carne == 'f':
        if quantidade_solicitada <= 4.90:
            valor_kg = 4.90
        else:
            valor_kg = 5.80
    elif tipo_carne == 'a':
        if quantidade_solicitada <= 4.90:
            valor_kg = 5.90
        else:
            valor_kg = 6.80
    elif tipo_carne == 'p':
        if quantidade_solicitada <= 4.90:
            valor_kg = 5.90
        else:
            valor_kg = 6.80
    else:
        print("Tipo de carne inexistente - vai ganhar languiça de morenona")
    return valor_kg

def calcula_valor_compra_sem_desconto(valor_kg, quantidade_solicitada):
    total_bruto = valor_kg * quantidade_solicitada
    return total_bruto

def calcula_valor_compra_com_desconto(forma_pgto, total_bruto):
    if forma_pgto == '1':
        total_a_pagar = total_bruto - ((total_bruto*5)/100)
    else:
        total_a_pagar = total_bruto
    return total_a_pagar

def valida_tipo_carne_para_impressao (tipo_carne):
    if tipo_carne == 'f':
        carne = "file duplo"
    elif tipo_carne == 'a':
        carne = "alcatra"
    elif tipo_carne == 'p':
        carne = "picanha"
    else:
        print("carne invalida")
    return carne

def valida_tipo_carne_para_impressao (forma_pgto):
    if forma_pgto == "1":
        forma_pgto_cliente = "Cartão Tabajara"
    else:
        forma_pgto_cliente = "Outros"
    return forma_pgto_cliente

valor_kg = verifica_valor_tipo_carne(tipo_carne,quantidade_solicitada)
valor_total_sem_desconto = calcula_valor_compra_sem_desconto(valor_kg,quantidade_solicitada)
valor_total_com_desconto = calcula_valor_compra_com_desconto(forma_pgto,valor_total_sem_desconto)
valida_tipo_carne_para_impressao(tipo_carne)
tipo_pagamento = valida_tipo_carne_para_impressao(forma_pgto)


print("------------------------")
print("Quantidade: " + str(quantidade_solicitada))
print("Tipo carne: " + str(tipo_carne))
print("Preço total: R$" + str(valor_total_sem_desconto))
print("Tipo de pagamento: " + str(tipo_pagamento))
print("Valor de desconto: R$" + str(valor_total_com_desconto))
print("------------------------")