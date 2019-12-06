# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome_usuario = input("Informe o nome de usuário: ")
senha_usuario = input("Informe a senha de usuário: ")

def valida_senha_login(nome_usuario, senha_usuario):
    while nome_usuario == senha_usuario:
        print("Login e senha nao podem ser iguais")
        nome_usuario = input("Informe o nome de usuário: ")
        senha_usuario = input("Informe a senha de usuário: ")
    else:
        print("usuario cadastrado")
valida_senha_login(nome_usuario,senha_usuario)