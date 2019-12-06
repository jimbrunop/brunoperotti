# Faça um programa que leia 5 números e informe a soma e a média dos números.


index = 0
listagem_de_numero = []
soma = 0

def calcula_soma_e_media (index, soma):
    while index < 5:
        index += 1
        num = int(input("Informe o proximo numero: "))
        listagem_de_numero.append(num)
    for index in listagem_de_numero:
        soma += index
    media = soma / 5
    print("a soma dos valores é: " + str(soma))
    print("a media dos valores é: " + str(media))
calcula_soma_e_media(index,soma)