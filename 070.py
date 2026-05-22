print('='*40)
print('Varejão do César'.center(40))
print('='*40)
#Variáveis
total = menor_preco = nome_menor_preco = maior_mil = 0
#loop
while True:
#Iniciando a compra
    nomeprodut = str(input('Digite o nome do produto que irá por no carrinho: '))
    preco = float(input('Digite o preço do produto: R$'))
#Calculando o valor final da compra
    total += preco
#Quantidade de produtos acima de R$1000
    if preco > 1000:
        maior_mil += 1
#Produto mais barato
    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        nome_menor_preco = nomeprodut
#Continuando ou não a compra
    user = ' '
    while user not in 'SsNn':
        user = str(input('Deseja continuar comprando? [S/N] ')).strip()[0]
    if user in 'Nn':
        break
print('='*40)
print('COMPRA ENCERRADA !'.center(40))
print(f'''>Valor final da compra: R${total:.2f}
>Produtos acima de R$1000: {maior_mil}
>Produto de menor preço: {nome_menor_preco.upper()} (que  saiu por R${menor_preco})''')
print('='*40)