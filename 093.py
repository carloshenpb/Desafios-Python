jogador = dict()
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
totalpartidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for p in range(0, totalpartidas):
    gols.append(int(input(f'Gols na {p+1}° partida: ')))
jogador['gols'] = gols[:]
jogador['golstotal'] = sum(gols)
print('¨¨'*20)
for k, v in jogador.items():
    print(f'{k.upper()} recebeu o valor: {v}')
print('¨¨'*20)
print(jogador)
print('¨¨'*20)
for p, g in enumerate(jogador["gols"]):
    if g == 0:
        print(f'Na {p+1}° partida jogada ele não fez gol')
    else:
        print(f'Na {p + 1}° partida jogada ele fez: {g} gols')
print(f'Somando um total de: {jogador["golstotal"]} gols.')
