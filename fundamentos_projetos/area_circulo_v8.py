#!/usr/bin/python3
from math import pi


def circulo(raio):
    print('Área do círculo = %.2f' % (pi * raio ** 2))


if __name__ == '__main__':
    raio = float(input('Informe o raio: '))
    circulo(raio)
