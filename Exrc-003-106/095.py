jogadores = []
jogador = dict()
gols = []
while True:
    jogador['nome'] = str(input('Digite o nome do jogador: ')).strip()
    jogador['partidas'] = int(input(f'Quantas partidas o {jogador['nome']} fez? '))
    for p in range(0, jogador['partidas']):
        gols.append(int(input(f'Gols na {p+1}° partida: ')))
    jogador['gols'] = gols[:]
    jogador['golstotal'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())
    while True:
        user = str(input('Deseja registrar mais jogadores? [S/N]: ')).upper().strip()[0]
        if user in 'SN':
            break
        print('Erro!')
    if user == 'N':
        break
print('=='*20)
print('DADOS DOS JOGADORES')
print('=='*20)
print(f'|{"N°:":<5}|{"Nome:":<10}|{"N°Partidas:":<10}|{"Total de gols:":<10}|')
for i, j in enumerate(jogadores):
    print(f'|{i:<5}|{j["nome"]:<10}|{j["partidas"]:<10} |{j["golstotal"]:<10}    |')
while True:
    busca = int(input('Mostrar lib de um jogador? (999 para parar):  '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print('Erro! Não existe jogador com esse código! ')
    else:
        print(f'<<<Estatísticas de {jogadores[busca]["nome"]}>>>')
        for p, g in enumerate(jogadores[busca]['gols']):
            if g == 0:
                print(f' -> Na {p+1}° partida ele não marcou gols.')
            else:
                print(f' -> Na {p+1}° partida ele marcou {g} gols.')

print('=='*20)
print('<<<< FIM >>>>')