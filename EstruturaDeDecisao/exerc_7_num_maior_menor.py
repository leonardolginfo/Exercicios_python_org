# Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

maior = num1

if num1 < num2 > num3:
    maior = num2

if num1 < num3 > num1:
    maior = num3
print(f'O maior número é {maior}')

menor = num1
if num1 > num2 < num3:
    menor = num2
if num1 > num3 < num2:
    menor = num3
print(f'O menor número é {menor}')