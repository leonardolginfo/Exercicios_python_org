# Faça um Programa que leia três números e mostre o maior deles.
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2:
    if num1 > num3:
        print(f'O maior número é primeiro {num1}')
    else:
        print(f'O maior número é terceiro {num3}')
elif num2 > num3:
     print(f'O maior número é o segundo {num2}')
else:
     print(f'O maior número é o terceiro {num3}')
