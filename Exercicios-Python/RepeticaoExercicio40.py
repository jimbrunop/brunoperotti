# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.


def estatistica_acidentes():
    ficha_cidade = []
    lista_veiculos = []
    lista_acidentes = []
    cidade_contador = 0
    while cidade_contador < 5:
        codigo_cidade = int(input("Informe o código cidade: "))
        numero_veiculos_passeio = int(input("Informe a quantidade de veículos de passeio: "))
        numero_acidentes = int(input("Informe a quantidade de acidentes: "))
        cidade_full_dados = {"codigo_cidade": codigo_cidade, "numero_veiculos_passeio": numero_veiculos_passeio, "numero_acidadentes": numero_acidentes}
        ficha_cidade.append(cidade_full_dados)
        cidade_contador += 1
        lista_veiculos.append(ficha_cidade[cidade_contador - 1]['numero_acidadentes'])
        if ficha_cidade[cidade_contador -1]['numero_veiculos_passeio'] < 2000:
            lista_acidentes.append(ficha_cidade[cidade_contador - 1]['numero_veiculos_passeio'])
        if ficha_cidade[cidade_contador - 1]['numero_acidadentes'] > ficha_cidade[cidade_contador - 2]['numero_acidadentes']:
            mais_acidentes = ficha_cidade[cidade_contador - 1]
        if ficha_cidade[cidade_contador - 1]['numero_acidadentes'] < ficha_cidade[cidade_contador - 2]['numero_acidadentes']:
            menos_acidentes = ficha_cidade[cidade_contador - 1]

    media_veiculos = (sum(lista_veiculos))/cidade_contador
    media_acidentes_dois_mil = (sum(lista_acidentes)/len(lista_acidentes))
    print("dados cidade com mais acidentes " + str(mais_acidentes))
    print("dados cidade com menos acidentes " + str(menos_acidentes))
    print("a média de veículos na listagem é de " + str(media_veiculos))
    print("a média de acidentes de cidades com até 2000 veículos é de " + str(media_acidentes_dois_mil))
estatistica_acidentes()