termo_inicial = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))

c = 1
while c <= 10:
    an = termo_inicial + (c - 1) * razao
    c = c + 1
    print(an, end=' -> ')
print('FIM')