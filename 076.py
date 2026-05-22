produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.20,
            'Livro', 34.90 )
print('__'*20)
print('TABELA DE PREÇOS'.center(40))
print('__'*20)
# Exibição dos produtos
p = 0
while p < len(produtos):
    if p <= 20:
        print(f'{produtos[p]:.<20}', end='')
        print(f'R${produtos [p+1]:.2f}')
        p += 2
    else:
        break
print('__'*20)
