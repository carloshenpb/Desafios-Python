# Iniciando o programa
num = int(input('Qual o número que você deseja saber o fatorial? '))
# Fatorial do número escolhido
contador = num
fatorial = 1
print(f'Calculando {num}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
# Exibindo o resultado
print(fatorial)