# Faça um Programa que verifique se uma letra digitada
# é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
print()
sexo = input('Digite uma letra em caixa alta para ientificar o sexo: ')
if sexo == 'F':
    print(f'{sexo} - Feminino')
elif sexo == 'M':
    print(f'{sexo} - Masculino')
else:
    print('Sexo Inválido')