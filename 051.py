term_1 = int(input('Digite o 1° termo da sua PA: '))
raz = int(input('Digite a razão da sua PA: '))
print('Os 10 primeiros termos dessa PA são: ')
#Calculando os 10  primeiros termos da PA:
for c in range(1, 11):
    an = term_1 + (c-1) * raz
    print(an, end=' -> ')
print('ACABOU !')
