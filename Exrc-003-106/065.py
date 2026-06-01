num = int(input('Digite um número: '))
user = str(input('Deseja continuar digitando? [S/N]')).strip().upper()[0]
soma = num
cont = 1
num_max = num_men = num
while user in 'Ss':
    num = int(input('Digite um número: '))
    if num > num_max:
        num_max = num
    elif num < num_men:
        num_men = num
    soma += num
    cont += 1
    user = str(input('Deseja continuar digitando? [S/N]')).strip().upper()[0]
print('O maior número digitado foi {} e o menor foi {} '.format(num_max, num_men))
media = soma/cont
print(f'Você digitou {cont} números e a media dos valores digitado é de {media}')