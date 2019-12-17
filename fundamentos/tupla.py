# coding:utf-8

tupla = tuple()
tupla = ()
print(type(tupla))
tupla = ('um',)      # tupla de um único elemento tem que colocar uma vírgula no final
print(type(tupla))
print(tupla[0])
cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.count('azul'))
print(len(cores))
