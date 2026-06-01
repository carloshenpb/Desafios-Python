palavras = ('estudar', 'python', 'computador', 'tecnologia', 'barramentos',
            'programaçao', 'memoria', 'nuvem', 'internet', 'lib')

for palavra in palavras:
    print(f'\nA palavra {palavra.upper()} tem as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')