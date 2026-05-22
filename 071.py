print('=$='*20)
print('CAIXA ELETRÔNICO'.center(60))
print('=$='*20)
#Variáveis
saque = int(input('Digite o valor do saque: R$'))
total = saque
cedula = 50
totalced = 0
#Loop
print('Sacando...........')
while True:
    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break
print('=$='*20)