# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

quantidade_turmas = int(input("Informe a quantidade de turmas: "))


def calcula_media_por_turma(quantidade_turmas):
    contador = 0
    lista_alunos = []

    while contador < quantidade_turmas:
        quantidade_alunos = int(input("Informe a quantidade de alunos da turma: "))
        if quantidade_alunos > 40:
            print("Numero de turma excede a quantidade máxima, 40 alunos por turma")
        else:
            lista_alunos.append(quantidade_alunos)
            media_por_turma = 40/lista_alunos[contador]
            print("A media da turma " + str(contador) + " : " + str(media_por_turma))
            contador += 1
calcula_media_por_turma(quantidade_turmas)



