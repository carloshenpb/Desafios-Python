preco = float(input('Qual o preço do produto? R$:  '))
desconto = preco-(preco*5/100)
print('O novo preço com 5% de desconto é R${:.2f}'.format(desconto))