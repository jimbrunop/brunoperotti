# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#
#                           Até 5 Kg           Acima de 5 Kg
#     Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#     Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#
#     Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

qtdade_kg_morangos_compra = float(input("Informe quantos Kg foram adquiridos de morango: "))
qtdade_kg_maca_compra = float(input("Informe quantos Kg foram adquiridos de maçã: "))


def calcula_preco_morango(qtdade_kg_morangos_compra):
    if qtdade_kg_morangos_compra <= 5.00:
        preco_kg_morango = 2.50
    else:
        preco_kg_morango = 2.20
    return preco_kg_morango

def calcula_preco_maca(qtdade_kg_maca_compra):
    if qtdade_kg_maca_compra <= 5.00:
        preco_kg_maca = 1.80
    else:
        preco_kg_maca = 1.50
    return preco_kg_maca

def calcula_total_kg(qtdade_kg_morangos_compra, qtdade_kg_maca_compra):
    total_kg = qtdade_kg_maca_compra + qtdade_kg_morangos_compra
    return total_kg

def calcula_valor_total (qtdade_kg_morangos_compra, qtdade_kg_maca_compra, preco_kg_morango, preco_kg_maca):
    valor_total_morango = qtdade_kg_morangos_compra * preco_kg_morango
    valor_total_maca = qtdade_kg_maca_compra * preco_kg_maca
    valor_total_compra = valor_total_maca + valor_total_morango
    return valor_total_compra

def calcula_preco_final_desc (valor_total_compra, total_kg):
    desconto = (valor_total_compra * 10) / 100
    valor_a_pagar = valor_total_compra - desconto
    if valor_total_compra >= 25.00 or total_kg >= 8.00:
        print(valor_a_pagar)

    else:
        valor_a_pagar = valor_total_compra
        valor_a_pagar
        print(valor_total_compra)


preco_morango_validado = calcula_preco_morango(qtdade_kg_maca_compra)
preco_maca_validado = calcula_preco_maca(qtdade_kg_maca_compra)
compra_total = calcula_total_kg(qtdade_kg_morangos_compra, qtdade_kg_maca_compra)
valor_total_validado = calcula_valor_total(qtdade_kg_morangos_compra, qtdade_kg_maca_compra, preco_morango_validado, preco_maca_validado)
valor_a_pagar = calcula_preco_final_desc (valor_total_validado, compra_total)

