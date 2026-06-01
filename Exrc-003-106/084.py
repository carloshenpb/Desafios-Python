#Listas e variáveis
pessoas = []
dados = []
maior = menor = 0
#Coletando lib
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    if len(pessoas) == 1: ## Armazenando o peso da primeira pessoa
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    dados.clear()
    user = ' '
    while user not in 'SsNn':
        user = str(input('Deseja registrar mais pessoas? [S/N] ')).strip()[0]
    if user in 'Nn':
        break
#Exibindo lib
print('=&='*20)
print(f'> Foram registradas {len(pessoas)} pessoas.') ## Quantidade de pessoas registradas
print(f'> O maior peso foi {maior}Kg. As pessoas com esse peso foram: ', end='')
for p in pessoas:## Mais pesados
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'> O menor peso foi {menor}Kg. As pessoas com esse peso foram: ', end='')
for p in pessoas:## Mais leves
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
print('=&='*20)
