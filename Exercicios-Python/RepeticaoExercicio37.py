# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

sistema_ativo = True

def questiona_dados_cliente(sistema_ativo):
    ficha_aluno = []
    listagem_gorduritos = []
    listagem_alturas = []
    contador_aluno = 0
    while sistema_ativo == True:
        codigo_aluno = int(input("informe seu codigo: "))
        if codigo_aluno == 0:
            sistema_ativo = False
        else:
            peso_aluno = float(input("informe o seu peso em kg: "))
            altura_aluno = float(input("informe a sua altura em cm: "))
            cliente_full_dados = {"codigo_aluno":codigo_aluno, "altura_aluno":altura_aluno, "peso_aluno":peso_aluno}
            ficha_aluno.append(cliente_full_dados)
            listagem_gorduritos.append(peso_aluno)
            listagem_alturas.append(altura_aluno)
            contador_aluno += 1
        if ficha_aluno[contador_aluno - 1]['altura_aluno'] > ficha_aluno[contador_aluno - 2]['altura_aluno']:
            mais_alto = ficha_aluno[contador_aluno - 1]
        if ficha_aluno[contador_aluno - 1]['peso_aluno'] > ficha_aluno[contador_aluno - 2]['peso_aluno']:
            mais_gordo = ficha_aluno[contador_aluno - 1]
    #     if ficha_aluno[contador_aluno - 1]['peso_aluno'] < ficha_aluno[contador_aluno - 2]['peso_aluno']:
    #         mais_magro = ficha_aluno[contador_aluno - 1]
    #     if ficha_aluno[contador_aluno - 1]['altura_aluno'] < ficha_aluno[contador_aluno - 2]['altura_aluno']:
    #         mais_baixo = ficha_aluno[contador_aluno - 1]
    # print("O aluno mais alto é: " + str(mais_magro))
    # print("O aluno mais alto é: " + str(mais_baixo))
    print("O aluno mais alto é: " + str(mais_alto))
    print("O aluno mais gordo é: " + str(mais_gordo))

    print("A média de gorduritos da turma é de: " + str((sum(listagem_gorduritos)) / contador_aluno))
    print("A média de altura da turma é de: " + str((sum(listagem_alturas)) / contador_aluno))
questiona_dados_cliente(sistema_ativo)
