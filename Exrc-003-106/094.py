pessoas = list()
pessoa = dict()
somaid = media = 0
while True: # Registro de pessoas
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro o sexo só pode ser M(masculino) e F(feminino).')
    pessoa['idade'] = int(input('Idade: '))
    somaid += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        user = str(input('Deseja registrar mais alguém? [S/N]: ')).upper().strip()[0]
        if user in 'SN':
            break
        print('Erro! Digite apenas S(sim) ou N(não)!')
    if user == 'N':
        break
print('=-'*20)# Exibindo os resultados
print(f'Foram registradas {len(pessoas)} pessoas.')
print('--'*20)
media = somaid/len(pessoas)
print(f'> A média de idade do grupo foi de {media:.1f}')
print('> As mulheres do registradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}]', end=' ')
print()
print('> As pessoas que estão acima da média de idade são: ')
for p in pessoas:
    if p['idade'] >= media:
        print(f' - {p["nome"]} com {p["idade"]} anos.')