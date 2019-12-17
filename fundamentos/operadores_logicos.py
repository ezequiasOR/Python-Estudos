# coding:utf-8

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
