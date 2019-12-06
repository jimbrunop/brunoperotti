# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

total_eleitores = int(input("Informe a quantidade de eleitores: "))

def valida_eleito(total_eleitores):
    candidato_01 = 0
    candidato_02 = 0
    candidato_03 = 0
    contador = 0
    while contador < total_eleitores:
        voto = int(input("Informe 1 para o candidato 1, 2 para o candidato 2 ou 3 para o condidato 3: "))
        if voto == 1:
            candidato_01 += 1
            contador += 1
        elif voto == 2:
            candidato_02 += 1
            contador += 1
        elif voto == 3:
            candidato_03 += 1
            contador += 1
        else:
            print("Cod candidato inexistente ")

    print("Quantidade de votos Candidado 1: " + str(candidato_01))
    print("Quantidade de votos Candidado 2: " + str(candidato_02))
    print("Quantidade de votos Candidado 3: " + str(candidato_03))
valida_eleito(total_eleitores)
