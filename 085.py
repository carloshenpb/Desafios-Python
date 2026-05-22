# Listas e Variáveis
numeros = [[], []]
# Digitando os valores
for n in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
# Organizando as listas
numeros[0].sort()
numeros[1].sort()
# Exibindo o resultado
print('-_'*20)
print(f'> Lista de números pares: {numeros[0]}')
print(f'> Lista de números ímpares: {numeros[1]}')