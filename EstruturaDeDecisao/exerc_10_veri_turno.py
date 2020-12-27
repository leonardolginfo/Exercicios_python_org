# Faça um Programa que pergunte em que turno você estuda. Peça para digitar
# M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print('Olá" Em que turno você estuda? ')
print('Digite M para Matutino')
print('Digite V para Vespertino')
print('Digite N para Noturno')
turno = input('Digite aqui: ')

if turno == 'M':
    print('\nBom dia!!!')
elif turno == 'V':
    print('\nBoa tarde!!!')
elif turno == 'N':
    print('\nBoa noite!!!')
else:
    print('\nEntrada Inválida!')