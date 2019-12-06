#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("informe uma letra")

def valida_vogal(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print ('é vogal')
    else:
        print ('é consoante')
valida_vogal(letra)