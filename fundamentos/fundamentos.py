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
