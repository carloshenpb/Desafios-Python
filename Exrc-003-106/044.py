#Captando o valor do produto:
valor_produto = float(input('Qual o valor do produto que você está comprando? R$'))

#Definindo a forma de pagamento
forma_de_pagamento = int(input('''Qual a forma de pagamento? 
[1 - A vista no dinheiro com 10% de Desconto]
[2 - A vista no cartão com 5% de desconto]
[3 - 2 vezes no cartão, sem desconto]
[4 - 3 vezes ou mais no cartão, com 20% de juros]
'''))

#A vista no dinheiro:
if forma_de_pagamento == 1:
    desconto = valor_produto - (valor_produto*10/100)
    print(f'O valor a vista no dinheiro é de R${desconto:.2f}')
#A vista no cartão:
if forma_de_pagamento == 2:
    desconto = valor_produto - (valor_produto*5/100)
    print(f'O valor do produto a vista no cartão é de R${desconto:.2f}')
#2 vezes no cartão:
if forma_de_pagamento == 3:
    parcela_sem_juros = valor_produto/2
    print(f'Dividindo em 2 vezes de R${parcela_sem_juros:.2f} no cartão.')
#3 vezes ou mais no cartão, com juros:
if forma_de_pagamento == 4:
    opcao_parcelas = int( input ('Em quantas vezes você deseja dividir?' ))
    parcela_com_juros = (valor_produto + valor_produto*20/100)/opcao_parcelas
    print(f'Dividindo em {opcao_parcelas} as parcelas serão no valor de R${parcela_com_juros:.2f}')

#Para bocós!
else:
    print('OPÇÃO INVÁLIDA!')