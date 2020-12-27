# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
print()
valor_hora = float(input('Qual o valor da sua hora trabalhada? '))
qtd_horas = float(input('Quantas horas você rtabalhou neste mês? '))
sal_bruto = valor_hora * qtd_horas
ir   = int(11)
inss = int(8)
sindicato = int(5)
salario_liquido = sal_bruto - (((sal_bruto * ir)/100) + ((sal_bruto * inss)/100) + ((sal_bruto * sindicato)/100))
print(f'O valor do seu salário líquido é {salario_liquido}')