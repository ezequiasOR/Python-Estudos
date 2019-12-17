# coding:utf-8

from string import Template

nome, idade = 'Ana', 30
print('Nome: %s Idade: %d' % (nome, idade))  # menos recomendado; %s => String, %d => int, %f => float, %r => boolean
print('Nome: {0} Idade: {1}'.format(nome, idade))  # pode ou não usar os indices, python < 3.6
print(f'Nome: {nome} Idade: {idade}')  # python >= 3.6

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))
