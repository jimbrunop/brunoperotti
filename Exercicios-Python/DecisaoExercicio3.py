#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Informe M para masculino ou F para feminino")

def valida_sexo(sexo):
    if sexo == 'm' or sexo == 'M':
        print("Sexo masculino")
    elif sexo == 'f' or sexo == 'F':
        print("Sexo feminino")
    else:
        print("Morenona")
valida_sexo(sexo)