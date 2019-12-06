#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno_estudo = input("Informe M-matutino ou V-Vespertino ou N- Noturno")

def valida_turno(turno_estudo):
    if turno_estudo == 'M':
      print("Bom dia!")
    elif turno_estudo == 'V':
        print("Boa tarde!")
    elif turno_estudo == "N":
        print("Boa noite!")
    else:
        print("turno inválido")
valida_turno(turno_estudo)