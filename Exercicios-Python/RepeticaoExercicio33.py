#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

programa_inicia = True

def realiza_calculo(programa_inicia):
    listagem_temperaturas = []
    while programa_inicia == True:
        temperatura = float(input("Informe a temperatura em Celsius: "))
        comando_parar = input("Deseja parar a contagem para o resultado: s - sim ou n para n")
        if comando_parar == 'n':
          listagem_temperaturas.append(temperatura)
          listagem_temperaturas.sort(key=int,reverse=True)
          print(listagem_temperaturas)
          continue
        elif comando_parar == 's':
            media_temp = sum(listagem_temperaturas)/listagem_temperaturas.__len__()
            print("A média de temperatura é: " + str(media_temp))
            print("A temperatura informada mais alta é: " + str(listagem_temperaturas[0]) + " e a temperatura mais baixa é : " + str(listagem_temperaturas[-1]))
            programa_inicia = False
        else:
            print("sistema reiniciado")
realiza_calculo(programa_inicia)

