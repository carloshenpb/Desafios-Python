import moeda

valor = float(input('Digite um valor: R$ '))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, f = True)}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, f = False)}')
print(f'Ao aumentar 10%, temos {moeda.aumentar(valor, taxa=10, f=True)}')
print(f'Ao diminuir 15%, temos {moeda.diminuir(valor, taxa=15, f=True)}')