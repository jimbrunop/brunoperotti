# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00


quantidade_itens = int(input("Quantidade de pães comprados: "))

def calcula_valor_total(quantidade_itens):
    valor_unitario = 0.18
    valor_total = valor_unitario * quantidade_itens
    print("O valor total dos pães é de: R$" + str(valor_total))
calcula_valor_total(quantidade_itens)