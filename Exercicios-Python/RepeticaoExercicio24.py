# Faça um programa que calcule o mostre a média aritmética de N notas.

quantidade_notas = int(input("informe a quantidade de notas do aluno: "))

def calcula_media(quantidade_notas):
    contador = 0
    listagem_notas = []
    while contador < quantidade_notas:
        nota_aluno = float(input("informe a nota: "))
        if nota_aluno >= 0.0 and nota_aluno <= 10.0:
            contador += 1
            listagem_notas.append(nota_aluno)
        else:
            print("nota precisa ser um valor válido entre 0 e 10")

    somatoria = sum(listagem_notas)
    media = somatoria/quantidade_notas
    print("relação de notas: " + str(listagem_notas) + " e a média do aluno fdi: " + str(media))
calcula_media(quantidade_notas)