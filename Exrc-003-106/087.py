#Listas e variáveis
matriz = [[0, 0 , 0], [0, 0, 0], [0, 0, 0]]
somapares = somacol2 =  maior = 0
# Digitando os números da matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para posição [{l}, {c}]:  '))
        if matriz[l][c] % 2 == 0: ## Somando os valores pares
            somapares += matriz[l][c]
        if c ==  2: ## Somando os valores da 3° coluna
            somacol2 += matriz [l][c]
# Exibindo os resultados
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if c == 0: # Procurando o maior número da 2° coluna
            maior = matriz[1][c]
        elif matriz[1][c] > maior:
            maior = matriz[1][c]

    print()
print('=-'*30)
print(f'> A soma dos valores pares digitados foi: {somapares}')
print(f'> A soma do valores da 3° coluna foi: {somacol2}')
print(f'> O maior valor da 2° linha foi: {maior}')