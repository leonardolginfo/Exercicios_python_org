# Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

# n1>n2>n3 -
# n1>n3>n2 -
# n2>n1>n3
# n2>n3>n1
# n3>n1>n2
# n3>n2>n1

if num1 > num2 > num3:
    maior = num1
    meio = num2
    menor = num3
if num1 > num3 > num2:
    maior = num1
    meio = num3
    menor = num2
if num2 > num1 > num3:
    maior = num2
    meio  = num1
    menor = num3
if num2 > num3 > num1:
    maior = num2
    meio = num3
    menor = num1
if num3 > num1 > num2:
    maior = num3
    meio = num1
    menor = num2
if num3 > num2 > num1:
    maior = num3
    meio = num2
    menor = num1

print(maior, meio, menor)