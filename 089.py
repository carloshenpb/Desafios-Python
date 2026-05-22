# Começo
print('+=/'*20)
print('REGISTRO DE ALUNOS'.center(60))
print('+=/'*20)
# Listas e Variavéis
listaalun = []
dados = []
media = 0
# Registrando lib
while True:
    dados.append(str(input('Nome do Aluno: ')))
    dados.append(float(input('1° Nota: ')))
    dados.append(float(input('2° Nota: ')))
    listaalun.append(dados[:])
    dados.clear()
    user = ' '
    while user not in 'SN':
        user = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if user == 'N':
        break
# Exibindo os resultados
print('+=/'*20)
print('___'*20)
print(f'|{"N°":<2}|{"NOME":<15}|{"MÉDIA":<5}|')
for i, a in enumerate(listaalun):
    media = (a[1]+a[2])/2
    print(f'|{i:<2}|{a[0]:<15}|{media:<5.1f}|')
print('___'*20)

while True:
    user = ' '
    while user not in 'NS':
        user = str(input('Deseja saber as notas de algum aluno em específico? [S/N]:  ')).upper().strip()[0]
        if user in 'N':
            print('+=/' * 20)
            print('FIM')
            break
        else:
            user1 = int(input('Qual número do aluno que você deseja saber as notas? '))
            if user1 <= len(listaalun) - 1:
                print('___'*20)
                print(f'''As notas do aluno(a) {listaalun[user1][0]} foram as seguintes: 
                1°Nota: {listaalun[user1][1]:<5}
                2°Nota: {listaalun[user1][2]:<5}''')
                print('___' * 20)
