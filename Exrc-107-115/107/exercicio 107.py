import moeda

valor = float(input('Digite o valor em R$: '))
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'A metade de R${valor} é R${moeda.metade(valor)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(valor, 10)}')
print(f'Diminuindo 15%, temos R${moeda.diminuir(valor, 15)}')