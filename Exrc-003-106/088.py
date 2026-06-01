from random import randint
from time import sleep
# Incio
print('=-'*30)
print('GERADOR DE JOGOS PARA MEGA'.center(60))
print('=-'*30)
user = int(input('Digite a quantidade de jogos que deseja gerar:  '))
print('Gerando jogos.....')
sleep(3)
# Listas
jogos = []
jogo = []
# Gerando  os jogos
for j in range(0, user):
    while len(jogo) < 6: # Gerando um jogo
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogos.append(jogo[:])
    jogo.clear()
# Exibindo os resultados
for i, j in enumerate(jogos):
    print(f'{jogos.index(j)+1}° jogo: {j}')
    sleep(1)