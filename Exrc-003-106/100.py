from random import randint
from time import sleep

def sorteio(lista):
    v = randint(1,10)
    print(f'Sorteando {v} valores......')
    for c in range(0, v):
        valor = randint(1, 10)
        lista.append(valor)
    for n in lista:
        print(f'{n}', end=' ')
        sleep(0.5)
    print()

def somaPar(lista):
    soma = 0
    print(f'Somando os valores pares de {lista}....')
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'O resultado da soma foi {soma}')

# Programa Principal
numeros = []
sorteio(numeros)
somaPar(numeros)
