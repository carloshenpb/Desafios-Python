from random import  choice
a1 = input('Digite o nome da 1 pessoa:  ')
a2 = input('Digite o nome da 2 pessoa:  ')
a3 = input('Digite o nome da 3 pessoa:  ')
a4 = input('Digite o nome da 4 pessoa:  ')
a5 = input('Digite o nome da 5 pessoa:  ')
lista = [a1, a2, a3 ,a4]
sorteado = choice(lista)
print('O sortudo é {} ! Parabens!'.format(sorteado))