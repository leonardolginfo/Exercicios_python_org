print(50 * '-')
print('--------------- Cálculo de salário ---------------')
print(50 * '-')
salario_inic = float(input('Qual o valor do seu salário atual? '))

if salario_inic <= 280:
    salario_final = salario_inic + (salario_inic * 20 / 100)
    valor_aumento = salario_final - salario_inic
    print(f'O salário incial era R${salario_inic:.2f}')
    print('Aumento de 20%')
    print(f'O valor de aumento é R${valor_aumento:.2f}')
    print(f'O novo salário é de R${salario_final}')
elif 280 < salario_inic < 700:
    salario_final = salario_inic + (salario_inic * 15 / 100)
    valor_aumento = salario_final - salario_inic
    print(f'O salário incial era R${salario_inic:.2f}')
    print('Aumento de 15%')
    print(f'O valor de aumento é R${valor_aumento:.2f}')
    print(f'O novo salário é de R${salario_final:.2f}')
elif 700 < salario_inic < 1500:
    salario_final = salario_inic + (salario_inic * 10 / 100)
    valor_aumento = salario_final - salario_inic
    print(f'O salário incial era R${salario_inic:.2f}')
    print('Aumento de 10%')
    print(f'O valor de aumento é R${valor_aumento:.2f}')
    print(f'O novo salário é de R${salario_final:.2f}')
else:
    salario_final = salario_inic + (salario_inic * 5 / 100)
    valor_aumento = salario_final - salario_inic
    print(f'O salário incial era R${salario_inic}')
    print('Aumento de 5%')
    print(f'O valor de aumento é R${valor_aumento:.2f}')
    print(f'O novo salário é de R${salario_final:.2f}')
