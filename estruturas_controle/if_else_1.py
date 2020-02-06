#!/usr/bin/python3
# Conceitos   Notas
# A           De 10,0 à 9,1
# A-          De 9,0 à 8,1
# B           De 8,0 à 7,1
# B-          De 7,0 à 6,1
# C           De 6,0 à 5,1
# C-          De 5,0 à 4,1
# D           De 4,0 à 3,1
# D-          De 3,0 à 2,1
# E           De 2,0 à 1,1
# E-          De 1,0 à 0,0

# *Para notas maiores que 10 e monores que 0, será impresso "Nota Inválida"


def nota_conceito(nota):
    if 9.1 <= nota <= 10.0:
        return 'A'
    elif 8.1 <= nota <= 9.0:
        return 'A-'
    elif 7.1 <= nota <= 8.0:
        return 'B'
    elif 6.1 <= nota <= 7.0:
        return 'B-'
    elif 5.1 <= nota <= 6.0:
        return 'C'
    elif 4.1 <= nota <= 5.0:
        return 'C-'
    elif 3.1 <= nota <= 4.0:
        return 'D'
    elif 2.1 <= nota <= 3.0:
        return 'D-'
    elif 1.1 <= nota <= 2.0:
        return 'E'
    elif 0.0 <= nota <= 1.0:
        return 'E-'
    else:
        return 'Nota Inválida'


if __name__ == '__main__':
    nota = float(input('Nota do aluno: '))
    conceito = nota_conceito(nota)
    print(conceito)
