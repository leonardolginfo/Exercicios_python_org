# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
lado = float(input('Digite o valor de um Lado do quadrado: '))
altura = float(input('Digite o valor da Altura do quadrado: '))
areaquad = lado * altura
dobro = areaquad * 2
print()
print(f'O dobro da área do quadrado é {dobro}')