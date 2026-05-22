#lista
numeros = list()
#Adicionando vários números
while True:
    num = int(input('Digite um número: '))
#Verificando se o número já foi digitado
    while num in numeros:
        print('Erro! Número já digitado!', end=' ')
        num = int(input('Digite outro número: '))
    if num not in numeros:
        print('Valor adicionado com sucesso....')
    numeros.append(num)
#Perguntando se o user quer continuar
    user = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if user in 'Nn':
        break
#Exibindo a lista em ordem crescente
numeros.sort()
print('=-'*20)
print(f'A lista final ficou assim: {numeros}')
