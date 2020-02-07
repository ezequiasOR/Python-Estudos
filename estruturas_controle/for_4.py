# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim')

# Função sortear_dado - numeros entre 1 e 6
# For com range 1 a 6
# Se for impar continue
# Se o numero for par e for igual ao valor sorteado
# pela funcao dado imprimir 'ACERTOU' e depois chamar o break
# Se não acertar chama o else... print('Não acertou o número!')

from random import randint


def sortear_dado():
    return randint(1, 6)


numero_sorteado = sortear_dado()

for i in range(1, 7):
    if i % 2 != 0:
        continue
    elif i == numero_sorteado:
        print('ACERTOU!', i)
        break
else:
    print('Não acertou o número!')
