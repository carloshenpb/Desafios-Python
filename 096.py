def area(l, c):
    a = l * c
    print('--'*20)
    print(f'> Medidas: {l}m X {c}m.')
    print(f'> A área desse terrno é de {a}.')

# Programa principal
largura = float(input('Digite a largura do terreno(m): '))
comprimento = float(input('Digite o comprimento do terreno(m): '))
area( l=largura, c=comprimento )
