# lista
nums = list()
# Digitando 5 valores
maior = menor = num = 0
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0: # Insere o primeiro número da lista
        maior = menor = num
        nums.append(num)
    if c > 0: # Insere os próximos 4 números da lista
        if num > maior: ## Insere um número na ultima posisção no caso dele ser maior do que os que já estão na lista
            maior = num
            nums.append(num)
        elif num < menor:## Insere um número na primeira posição no caso dele ser o menor do que os que já estão na lista
            menor = num
            nums.insert(0,num)
        else: ## Insere os números que não são nem o MAIOR da lista e nem o MENOR entre eles.
            for i, v in enumerate(nums):
                if v >= num:
                    nums.insert(i, num)
                    break
print('=-'*20)
print(f' Está foi a lista: {nums}')
