# coding:utf-8
# Primeiros Exemplos

print('Hello, World!')

# Tipos Básicos

print(True)
print(False)
print(1.2 + 1)
print('Aqui eu escrevo o que eu quero!')
print("Aqui também")
print('Você é ' + 3 * 'muito ' + 'legal!')  # + aqui é uma concatenação
# print(3 + '6') -> ambiquidade
print([1, 2, 3])
print({'nome': 'Ezequias', 'idade': 19})
print(None)

# Variáveis

a = 10
b = 5.2

print(a + b)

a = 'Agora sou uma string'
print(a)

# Comentários

# Comentários de uma linha

"""
Comentários de
multiplas linhaa
"""

# Minhas variáveis
salario = 3450.45
despesas = 2456.2

"""
Calculando quanto
vai sobrar no
final do mês
"""
print(salario - despesas)

# print('Fim')
print('Fim de verdade')  # Comentário aqui tbm vale!

# Operadores Aritméticos
print(2 + 3)
print(4 - 7)
print(2 * 5.2)
print(9.4 / 3)
print(9.4 // 3)
print(2 ** 10)
print(10 % 3)

a = 15
b = a
print(a + b)

# Percentual de despesas
percentual = (despesas / salario) * 100.0
print(percentual)

# Operadores Relacionais
print(3 > 4)
print(4 >= 3)
print(1 < 2)
print(3 <= 1)
print(3 != 2)
print(3 == 3)
print(2 == '2')

# Operadores de Atribuição
e = 3
e = e + 7
print(e)
e += 5
print(e)
e -= 3
print(e)
e *= 2
print(e)
e /= 4
print(e)
e %= 4
print(e)
e **= 8
print(e)
e //= 255
print(e)

# Operadores Lógicos
print(True or False)
print(7 != 3 and 2 > 3)

print('Tabela verdade do AND')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('Tabela verdade do OR')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('Tabela verdade do XOR')   # ou exclusivo
print(True != True)
print(True != False)
print(False != True)
print(False != False)

print('Operador de Negação (unário)')
print(not True)
print(not False)

# Desafio operadores lógicos
# Os trabalhos
trabalho_terca = True
trabalho_quinta = False

'''
-Confirmando os 2: TV 50' + Sorvete
-Confirmando apenas 1: TV 32' + Sorvete
-Nenhum confirmado: Fica em casa
'''
tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
mais_saudavel = not sorvete

print('Tv50={} Tv32={} Sorvete={} Saudável={}'
   .format(tv_50, tv_32, sorvete, mais_saudavel))

# Operadores Ternários
esta_chovendo = True
print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo])
print('Hoje estou com as roupas ' + ('molhadas.' if esta_chovendo else 'secas.'))

# Operador de Membro
lista = [1, 2, 3, 'Ana', 'Carla']
print(2 in lista)
print('Ana' not in lista)

# Operador de Identidade
x = 3
y = x
z = 3
print(x is y)
print(y is z)
print(x is not z)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_a is not lista_c)

# Builtins
print(type(1))
print(__builtins__.type('Fala Galera!  '))
__builtins__.print(10 / 3)