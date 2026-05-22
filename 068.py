from random import randint
print('='*20)
print('PAR OU ÍMPAR'.center(20))
print('='*20)
print('Vamos Jogar? ', end='')
#Variáveis
jogos = 0
#loop
while True:
    pc = randint(1, 10)
    user = int(input('Digite um valor: '))
    s = pc + user
    par_impar = ' '
# Escolhendo entre PAR ou ÍMPAR
    while par_impar not in 'PpIi':
        par_impar = str(input('Par ou Ímpar? [P/I]: ')).strip()[0]
    print(f'Você Jogou {user} e o computador {pc}. Total de {s}.')
    print('-'*20)
# Verificando o resultado
    if s % 2 == 0:
        print('DEU PAR!')
        if par_impar in 'Pp': # Caso de vitória com PAR
            print('Você venceu essa! Vamos de novo? ')
            print('-'*20)
            jogos += 1
        else: # Caso de derrota
            break
    else:
        print('DEU ÍMPAR!')
        if par_impar in 'Ii': # Caso de vitória com ÍMPAR
            print('Você venceu essa! Vamos de novo? ')
            print('-'*20)
            jogos += 1
        else: # Caso de derrota
            break
## Fim do programa
## Caso perca de primeira:
if jogos == 0:
    print('Você perdeu de primeira!')
elif jogos == 1:
    print('Você ganhou apenas 1!')
else:
    print(f'Após {jogos} vitórias consecutivas, você perdeu!')