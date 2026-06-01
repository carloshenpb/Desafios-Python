print('TABUADA')
num = int(input('Qual número você deseja saber a tabuada? '))
print(f'Aqui está a tabuda do {num}')
for c in range(1,11):
    print(f'{num} x {c} = {num * c}')