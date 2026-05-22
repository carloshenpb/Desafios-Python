def ficha(nom = '<desconhecido>', gol = 0):
    print(f'O jogador {nom} fez um total de {gol} gol(s).')

#Programa principal
nome = str(input('Digite o nome do jogador: '))
gols = str(input(f'N° de gols marcados por {nome}: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nom=nome, gol=gols)