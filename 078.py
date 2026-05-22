#Lista e variáveis
nums = []
# Digitando os valores
for c in range(0, 5):
    nums.append(int(input(f'Digite um valor para posição {c}: ')))
# Exibindo os valores
print(f'Lista final: {nums}')
## Maior valor
if max(nums) != min(nums):
    print(f'O maior valor digitado foi {max(nums)} nas posições ', end='')
    for i, v in enumerate(nums):
        if v == max(nums):
            print(f'{i}...', end='')
    ## Menor valor
    print(f'\nO menor valor digitado foi {min(nums)} nas posições ', end='')
    for i, v in enumerate(nums):
        if v == min(nums):
            print(f'{i}...', end='')
else:
    print(f'O maior valor que é {max(nums)} e o menor que é {min(nums)} são iguais!')