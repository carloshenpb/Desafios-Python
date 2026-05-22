# Listas
lista_principal = []
lista_pares = []
lista_impares = []
# Digitando os valores
while True:
    num = int(input('Digite um número: '))
    lista_principal.append(num) # Adicionando a lista principal
    if num % 2 == 0: # Adiconando os números pares em uma lista especifica
        lista_pares.append(num)
    else: # Adiconando os números impares em uma lista especifica
        lista_impares.append(num)
    user = ' '
    while user not in 'SsNn':
        user = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if user in 'Nn':
        break
print('=='*20)
print(f'Lista completa dos valores digitados: {lista_principal}')
print(f'Lista dos números pares: {lista_pares}')
print(f'Lista dos números ímpares: {lista_impares}')
