# coding:utf-8

pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': ['Inglês', 'Português']}
print(type(pessoa))

print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][1])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))

pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
print(pessoa)
print(pessoa.pop('idade'))
print(pessoa)
pessoa.update({'idade': 40, 'Sexo': 'M'})
print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)
