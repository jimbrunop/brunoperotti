#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.


def questiona_dados_cliente():
    ficha_aluno = []
    contador_aluno = 0
    while contador_aluno < 10:
        codigo_aluno = int(input("Informe o coódigo do aluno: "))
        altura_aluno = float(input("informe a sua altura em cm: "))
        cliente_full_dados = {"codigo_aluno":codigo_aluno, "altura_aluno":altura_aluno}
        ficha_aluno.append(cliente_full_dados)
        contador_aluno += 1
        if ficha_aluno[contador_aluno - 1]['altura_aluno'] > ficha_aluno[contador_aluno - 2]['altura_aluno']:
            mais_alto = ficha_aluno[contador_aluno - 1]
        if ficha_aluno[contador_aluno - 1]['altura_aluno'] < ficha_aluno[contador_aluno - 2]['altura_aluno']:
            mais_baixo = ficha_aluno[contador_aluno - 1]
    print("O aluno mais alto é: " + str(mais_alto))
    print("O aluno mais baixo é: " + str(mais_baixo))
questiona_dados_cliente()

