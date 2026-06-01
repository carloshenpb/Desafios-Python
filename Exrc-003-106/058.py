from random import randint
from time import sleep

# Iniciando o game
print('-=-'*10)
print('JOGO DE ADIVINHAÇÃO')
print('-=-'*10)
 ## Sorteando um número entre 0 e 10
pc = randint(0, 10)
print('.'*9)
sleep(3)
 ## Escolha do usuário
user = int(input('Já escolhi um número entre 0 e 10! Agora é a sua vez, tente adivinhar qual número escolhi: '))

# Tentativas e erros
 ## Caso o usuário acerte de primeira
if user == pc:
    print('Nossa! Você acertou de Primeira! Parabéns!')

 ## Em caso de erro:
palpites = 0
while user != pc:
    if user > pc:
        print('Você errou! O número que escolhi é menor!')
    elif user < pc:
        print('Você errou! O número que escolhi é maior!')
    user = int(input('Tente de novo! '))
    palpites += 1
    
# Fim do game
print('Parabéns você acertou!')
print(f'N° de Tentativas: {palpites}')
