from random import choice
from time import sleep

print('--=--'*4)
print('[[[[ JOKENPÔ ]]]]')
print('--=--'*4)

#Escolha do Computador:
pedra = str('''  
   ██████
 ██████████
████████████
████████████
 ██████████
   ██████''')

papel = str('''
████████████
██        ██
██        ██
██        ██
██        ██
██        ██
████████████
''')

tesoura = str(''' 
     ██     ██
      ██   ██
       ██ ██
        ███
       ██ ██
      ██   ██
     ██     ██
      ██   ██
       ██ ██
        ███
''')

pedra_papel_tesoura = [pedra, papel, tesoura]
computador = choice(pedra_papel_tesoura)

#Escolha do jogador:
print('VAMOS JOGAR?')
print('JOOKENNN..................')
sleep(3)
jogador = str(input('........PÔ!  ').upper())
#Definido o vencedor:
#Caso 1: Jogador jogou pedra!
if jogador == 'PEDRA':
    print('''   VOCÊ JOGOU PEDRA!
    ██████
  ██████████
 ████████████
 ████████████
  ██████████
    ██████''')

    if computador == pedra:
        print('''EU JOGUEI PEDRA TAMBÉM! EMPATAMOS!
           ██████
         ██████████
        ████████████
        ████████████
         ██████████
           ██████
        ''')
    elif computador == papel:
        print('''EU JOGUEI PAPEL! EU GANHEI!
        ████████████
        ██        ██
        ██        ██
        ██        ██
        ██        ██
        ██        ██
        ████████████
        ''')
    elif computador == tesoura:
        print(''' EU JOGUEI TESOURA! VOCÊ GANHOU!
             ██     ██
              ██   ██
               ██ ██
                ███
               ██ ██
              ██   ██
             ██     ██
              ██   ██
               ██ ██
                ███
        ''')

#Caso 2: Jogador jogou papel!
if jogador == 'PAPEL':
    print('''VOCÊ JOGOU PAPEL!
    ████████████
    ██        ██
    ██        ██
    ██        ██
    ██        ██
    ██        ██
    ████████████
''')
    if computador == pedra:
        print('''EU JOGUEI PEDRA! VOCÊ GANHOU!
           ██████
         ██████████
        ████████████
        ████████████
         ██████████
           ██████
''')
    elif computador == papel:
        print('''EU JOGUEI PAPEL TAMBÉM! EMPATAMOS!
        ████████████
        ██        ██
        ██        ██
        ██        ██
        ██        ██
        ██        ██
        ████████████
''')
    elif computador == tesoura:
        print('''EU JOGUEI TESOURA! EU GANHEI!
             ██     ██
              ██   ██
               ██ ██
                ███
               ██ ██
              ██   ██
             ██     ██
              ██   ██
               ██ ██
                ███
''')

#Caso 2: Jogador jogou tesoura!
if jogador == 'TESOURA':
    print('''VOCÊ JOGOU TESOURA!
         ██     ██
          ██   ██
           ██ ██
            ███
           ██ ██
          ██   ██
         ██     ██
          ██   ██
           ██ ██
            ███
''')
    if computador == pedra:
        print('''EU JOGUEI PEDRA! EU GANHEI!
           ██████
         ██████████
        ████████████
        ████████████
         ██████████
           ██████
''')
    elif computador == papel:
        print('''EU JOGUEI PAPEL! VOCÊ GANHOU!
        ████████████
        ██        ██
        ██        ██
        ██        ██
        ██        ██
        ██        ██
        ████████████
''')
    elif computador == tesoura:
        print('''EU JOGUEI TESOURA TAMBÉM! EMPATAMOS!
             ██     ██
              ██   ██
               ██ ██
                ███
               ██ ██
              ██   ██
             ██     ██
              ██   ██
               ██ ██
                ███
''')
