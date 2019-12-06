#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

quantidade_turma = int(input("Informe a quantidade de pessoas da amostragem: "))

def valida_idade(quantidade_turma):
    contador_pessoas = 0
    lista_idades = []
    while contador_pessoas < quantidade_turma:
        idade_pessoa = int(input("informe a idade da pessoa: "))
        contador_pessoas += 1
        lista_idades.append(idade_pessoa)
    somatoria_idades = sum(lista_idades)
    media = somatoria_idades/contador_pessoas
    if media >= 0.0 and media <= 25.0:
        print("Trata-se de uma turma Jovem")
    elif media >= 26.0 and media <= 60.0:
        print("Trata-se de uma turma Adulta")
    else:
        print("Trata-se de uma turma Idosa")
valida_idade(quantidade_turma)