#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
print()
valor = float(input('Digite um número. '))
if valor > 0:
    print(f'O número {valor} digitado é POSITIVO.')
elif valor < 0:
    print(f'O número {valor} digitado é NEGATIVO.')
else:
    print(f'O valor digitado é igual 0')