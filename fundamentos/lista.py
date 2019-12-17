# coding:utf-8

lista = []
print(type(lista))
print(len(lista))
lista.append(1)
lista.append(5)
print(lista)
print(len(lista))

nova_lista = [1, 5, 'Ana', 'Bia']
print(nova_lista)
nova_lista.remove(5)    # remove o item 5 e não o indice 5
print(nova_lista)
nova_lista.reverse()
print(nova_lista)

lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
print(lista.index('Guilherme'))
print(lista[2])
print(1 in lista)
print('Rebeca' in lista)
print('Pedro' not in lista)
print(lista[-1])
print(lista[-5])

lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista[1:3])
print(lista[1:-1])
print(lista[1:])
print(lista[:-1])
print(lista[:])
print(lista[::2])
print(lista[::-1])
del lista[2]
print(lista)
del lista[1:]
print(lista)
