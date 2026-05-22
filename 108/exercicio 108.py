import moeda

valor = float(input('Digite o valor em R$: '))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'Diminuindo 15%, temos {moeda.moeda(moeda.diminuir(valor, 15))}')