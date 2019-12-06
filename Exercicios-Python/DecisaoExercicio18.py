#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Informe uma data no formato xx/xx/xxxx")
separa_char = data.split("/")

def valida_data(sepera_char):
    if int(separa_char[0]) < 32 and int(separa_char[1]) < 13 and int(separa_char[2]) < 2020:
        print("Data valida")
    else:
        print("Data inválida")
valida_data(separa_char)
