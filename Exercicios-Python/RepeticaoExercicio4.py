# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pais_a_nr_hab = 80000
pais_a_taxa_anual_crescimento = 3.0
pais_b_nr_hab = 200000
pais_b_taxa_anual_crescimento = 1.5
anos = 0


def calcula_anos(pais_a_nr_hab, pais_a_taxa_anual_crescimento, pais_b_nr_hab, pais_b_taxa_anual_crescimento,anos):
    while pais_a_nr_hab <= pais_b_nr_hab:
        pais_a_nr_hab = pais_a_nr_hab + ((pais_a_nr_hab*pais_a_taxa_anual_crescimento)/100)
        pais_b_nr_hab = pais_b_nr_hab + ((pais_b_nr_hab * pais_b_taxa_anual_crescimento) / 100)
        anos += 1
    else:
        return anos

total_anos = calcula_anos(pais_a_nr_hab, pais_a_taxa_anual_crescimento, pais_b_nr_hab, pais_b_taxa_anual_crescimento, anos)

print("Será igualada a quantidade de habitantes de ambas as cidades após: " + str(total_anos) + " anos")