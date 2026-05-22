# Lista
lista_nums = list()
# Digitando vários números
while True:
    lista_nums.append(int(input('Digite um número: ')))
    user = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if user in 'Nn':
        break
#Quantos números foram digitados
print('__'*20)
print(f'> Foram digitados {len(lista_nums)} números')
#Listando os valores em ordem Decrescente
lista_nums.sort(reverse=True)
print(f'> A lista em ordem decrescente fica assim: {lista_nums}')
# Verificando se tem o número 5 na lista
if 5 in lista_nums:
    print(f'> Existem {lista_nums.count(5)} números 5 na lista!')
else:
    print('> O número 5 não foi incluso nesta lista!')
