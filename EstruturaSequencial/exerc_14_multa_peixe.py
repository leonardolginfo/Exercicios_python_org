# programa calcula multa e excesso de peso
print()
peso_pescado = float(input('Quantos quilos pescados? '))
limite_peso = int(50)

if peso_pescado > limite_peso:
    excesso = peso_pescado - limite_peso
    multa = excesso * 4
    print(f'\nVocê pescou kg{excesso} além do limite permitido que é de kg{limite_peso}.')
    print(f'Deverá pagar uma multa no valor de R${multa}')
else:
    print(f'Você não ultrapassou o limite de KG{limite_peso}, fique feliz :)')