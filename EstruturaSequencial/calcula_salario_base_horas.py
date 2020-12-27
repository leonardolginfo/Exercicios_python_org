# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print()
valorhora = float(input('Qual o valor da hora trabalhada? '))
qtd_horas_trabalhadas = float(input('Quantas horas trabalhou esse mês? '))
salario = valorhora * qtd_horas_trabalhadas

print()
print(f'O valor que você receberá será de R${salario}')
