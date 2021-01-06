# -*- coding: utf-8 -*-
# # Desafio 1 v2 da Cod3r
# Calcular a área da circunferência

import math
if __name__=='__main__':
    raio = float(input('Digite o valor do Raio:'))
    circun = math.pi  * raio**2
    print(
        f'O valor da circunferência é PI * Raio ao quadrado resultando \nna área da circunferência com valor igual a: {circun}')

    print('Nome do módulo', __name__)
    print('Nome do pacote', __package__)    
