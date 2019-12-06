# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho_m_quadrados_informado = float(input("Informe em m² a área a ser pintada: "))
quantidade_litros_tonel = tamanho_m_quadrados_informado / 3

if tamanho_m_quadrados_informado % 54 == 0:
	latas = tamanho_m_quadrados_informado / 54
else:
	latas = int(tamanho_m_quadrados_informado / 54) + 1

preco = latas * 80

print ('quantidade de latas' + str(latas))
print ('R$' + str(preco))
