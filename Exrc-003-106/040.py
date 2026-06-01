nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2)/2

print(f'Sua média foi: {media:.1f}')

if media < 5.0:
    print('REPROVADO!')
elif media < 7:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
