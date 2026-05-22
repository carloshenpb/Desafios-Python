dist = int(input('Qual a distância em KM da viagem que deseja fazer? '))
if dist <= 200:
    valor = dist * 0.5
    print('O valor da passagem será de {:.2f}R$'.format(valor))
else:
    valor = dist * 0.45
    print('O valor da passagem será de {:.2f}R$'.format(valor))
