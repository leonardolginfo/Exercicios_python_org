# Faça um programa para uma loja de tintas. O programa deverá pedir o
# tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
# é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
print()
metros_pintura = float(input('Quantos metros serão pintados? '))
valor_lt = int(80)
cob_lata = int(54)
qtd_lts = metros_pintura/cob_lata
valor_compra = qtd_lts * valor_lt
print(f'Você precisará de {qtd_lts:.2f}')
print(f'Sua compra será de R${valor_compra:.2f}')
