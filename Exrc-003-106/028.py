"""from random import choice
num = int(input('''Irei escolher um número de 0 a 5 para você adivinhar!
Escolhendo.....
PRONTO! AGORA É SUA VEZ! TENTE ADIVINHAR!:'''))

lista = [0, 1, 2, 3, 4, 5]
sorte = choice(lista)

if num == sorte:
    print('PARABÉNS VOCÊ ACERTOU! O número que escolhi foi:{}'.format(sorte))
else:
    print('QUE PENA, VOCÊ ERROU! O número que escolhi foi: {}'.format(sorte))"""

#Solução do Guanabara:

from random import randint
from time import sleep
computador = randint(0, 5) # Sortea um número de 0 a 5.

print('-=-'*20)
print('Irei pensar em número de 0 a 5, tente adivinhar!')
print('-=-'*20)
print('PENSANDO.....')
sleep(3)
jogador = int(input('PRONTO! Sua vez! Tente adivinhar qual número escolhi:'))
sleep(3)
if jogador == computador:
    print('VOCÊ GANHOU! PARABÉNS! O número é {}'.format(computador))
else:
    print('VOCÊ PERDEU! O número certo é {}'.format(computador))