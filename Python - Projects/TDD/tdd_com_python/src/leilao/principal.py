from src.leilao.dominio import Usuario, Lance, Leilao

user_01 = Usuario('usuario01', carteira=500.00)
user_02 = Usuario('usuario02', carteira=500.00)
user_03 = Usuario('usuario03', carteira=500.00)

lance_user_01 = Lance(usuario=user_01, valor=100.00)
lance_user_02 = Lance(usuario=user_02, valor=150.00)
lance_user_03 = Lance(usuario=user_02, valor=200.00)

leilao = Leilao('Playstation5')

leilao.lances.append(lance_user_02)
leilao.lances.append(lance_user_01)
leilao.lances.append(lance_user_03)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

print(f'O menor lance foi de {leilao.menor_lance} e o maior lance foi de {leilao.maior_lance}')
