# coding:utf-8

nome = 'Saulo Pedro'
print(nome)
print(nome[0])
# nome[0] = 'P'  String é imutável
# print('marca d'água')
print("Dias D'Avila")
print('Dias D\'Avila')
print('Texto entre apostrófos pode ter "aspas"')
print('''Texto com múltiplas
... linhas''')

nome = 'Ana Paula'
print(nome[-3])
print(nome[4:])   # Começa a partir do indice 4
print(nome[-5:])
print(nome[:3])   # O indice final não entra
print(nome[2:5])

numeros = '1234567890'
print(numeros)
print(numeros[::])
print(numeros[::2])     # de dois em dois
print(numeros[1::2])    # de dois em dois começando do indice 1
print(numeros[::-1])    # inverter uma string: indo do começo até o final com passo negativo
print(numeros[::-2])

print(nome[::-1])

frase = 'Python é uma linguagem excelente'
print('py' not in frase)
print('ing' in frase)
print(len(frase))
print(frase.lower())
frase = frase.upper()
print(frase)
print(frase.split())

a = '123'
b = ' de Oliveira 4'
print(a + b)
print(a.__add__(b))
