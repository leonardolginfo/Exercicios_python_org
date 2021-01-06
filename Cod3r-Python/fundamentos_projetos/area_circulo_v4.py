from math import pi
import sys
import errno


def circulo(raio):
    print('Área do círculo', pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)
