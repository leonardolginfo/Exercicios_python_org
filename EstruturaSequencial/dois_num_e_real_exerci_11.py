#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
print()
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite mais uma vez um número inteiro: '))
num3 = float(input('Digite um número real: '))
calc_1 = (num1*2)*(num2/2)
calc_2 = (num1*3)+num3
calc_3 = num3**3
print()
print(f'O produto do dobro de {num1} com metade de {num2} é {calc_1} .')
print()
print(f'A soma do triplo do {num1} com o {num3} é {calc_2} .')
print()
print(f'O valor de {num3} elevado ao cubo é {calc_3}.')
