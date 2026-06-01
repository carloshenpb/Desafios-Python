from operator import index
times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol',
         'Bahia', 'Botafogo', 'São Paulo', 'Bragantino',
         'Corinthians', 'Fluminense', 'Ceará', 'Internacional',
         'Atlético MG', 'Grêmio', 'Vasco', 'Santos', 'Vitória',
         'Juventude', 'Fortaleza', 'Sport' )
print('__'*20)
print('BRASILEIRÃO 2025'.center(40))
print('__'*20)
# 5 primeiros colocados (G5)
print('>5 primeiros colocados:')
for c in range(1,6):
    print(f' Em {c}° está o {times[c-1]}')
print('__'*20)
# 4 ultimos colocados (Z4)
print('>4 ultimos colocados:')
for c in range(16, 20):
    print(f'Em {c+1}° está o {times[c]}')
print('__'*20)
# Times em ordem alfabética
print('Times em ordem alfabética:')
print(sorted(times))
print('__'*20)
# Em qual posição está o Fluminense
pos_flu = times.index('Fluminense') + 1
print(f'O {times[9]} está em {pos_flu}° colocado!')
