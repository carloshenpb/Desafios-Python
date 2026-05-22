km = float(input('Quantos KMs você percorreu como carro?  '))
dia = float(input('Por quantos dias vocês alugou o carro?  '))
ckm = km*0.15
cdia = dia*60
total = ckm+cdia
print('_'*25, '\n 60R$ por dia de aluguel \n 0.15R$ por KM rodado\n', '_'*25)
print('''O valor total a pagar é: {:.2f}R$
O Valor pelos KMs rodados: {:.2f}R$
O Valor pelos dias que ficou com o carro: {:.2f}'''.format(total, ckm, cdia))