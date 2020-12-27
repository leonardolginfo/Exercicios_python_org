# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
print()
altura = float(input('Qual sua altura?'))
sexo = input('Você é do sexo Masculino ou Feminino? Digite M ou F ')

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f'O seu peso ideal é {peso_ideal}')
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {peso_ideal}')
else:
    print('Você não digitou M ou F')
