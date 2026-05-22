print('_'*40)
print('CADASTRO DE PESSOAS'.center(40))
print('_'*40)
#Varáveis
maior_dezoito = homens = mlhrs_com_menos_vinte =  0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'HhMm': ##caso o sexo digitado não seja valido
        sexo = str(input('Sexo: [H/M] ')).strip()[0]
    print('_'*40)
#Pessoas maiores de 18
    if idade >= 18:
        maior_dezoito += 1
#Quantidade de homens registrados
    if sexo in 'Hh':
        homens += 1
#Mulheres com menos de 20 anos
    if sexo in 'Mm':
        if idade < 20:
            mlhrs_com_menos_vinte +=1
#Perguntando se o usuário deseja continuar
    user = ' '
    while user not in 'SsNn':
        user = str(input('Deseja continuar a registrar mais pessoas? [S/N] ')).strip()[0]
    if user in 'Nn':
        break
    print('_' * 40)
print('=='*20)
print('FIM'.center(40))
print('=='*20)
print(f'''Foram registrados:
>{maior_dezoito} maiores de 18 anos.
>{homens} homens.
>{mlhrs_com_menos_vinte} mulheres com menos de 20 anos.''')
