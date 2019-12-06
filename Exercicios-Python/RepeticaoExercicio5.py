# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.


pais_a_nr_hab = float(input("Informe a quantidade de habitantes do país A: "))
pais_a_taxa_anual_crescimento = float(input("Informe a taxa anual de crescimento do país A em %: "))
pais_b_nr_hab = float(input("Informe a quantidade de habitantes do país B: "))
pais_b_taxa_anual_crescimento = float(input("Informe a taxa anual de crescimento do país B em %: "))
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