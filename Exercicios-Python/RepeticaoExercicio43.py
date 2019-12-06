# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

sistema_ativo = True

def calcula_conta_lanche(sistema_ativo):
    lista_pedido = []
    lista_valores_totais = []
    preco_cod_100 = 1.20
    preco_cod_101 = 1.30
    preco_cod_102 = 1.50
    preco_cod_103 = 1.20
    preco_cod_104 = 1.30
    preco_cod_105 = 1.00


    print("Especificação   Código  Preço")
    print("Cachorro Quente 100     R$ 1,20")
    print("Bauru Simples   101     R$ 1,30")
    print("Bauru com ovo   102     R$ 1,50")
    print("Hambúrguer      103     R$ 1,20")
    print("Cheeseburguer   104     R$ 1,30")
    print("Refrigerante    105     R$ 1,00")

    while sistema_ativo == True:
        cod_produto = int(input("Informe o cod do produto ou 0 para finalizar a compra :"))
        if cod_produto == 0:
            sistema_ativo = False
        else:
            quantidade = int(input("Informe a quantidade dos itens: "))
            if cod_produto == 100:
                valor_total_por_item = preco_cod_100 * quantidade
            if cod_produto == 101:
                valor_total_por_item = preco_cod_101 * quantidade
            if cod_produto == 102:
                valor_total_por_item = preco_cod_102 * quantidade
            if cod_produto == 103:
                valor_total_por_item = preco_cod_103 * quantidade
            if cod_produto == 104:
                valor_total_por_item = preco_cod_104 * quantidade
            if cod_produto == 105:
                valor_total_por_item = preco_cod_105 * quantidade
            pedido = {'cod item': cod_produto, 'quantidade': quantidade, 'valor item': valor_total_por_item}
            lista_pedido.append(pedido)
            lista_valores_totais.append(pedido['valor item'])
    print(*lista_pedido, sep="\n")
    print("Valor total do pedido: R$" + str(sum(lista_valores_totais)))
calcula_conta_lanche(sistema_ativo)