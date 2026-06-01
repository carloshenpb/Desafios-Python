aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input(f'Digite a média de {aluno['nome']}: '))
print('-+'*20)
print(f' O nome do Aluno é {aluno['nome']}')
print(f' A média foi de {aluno['média']}')
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
    print(f'Aluno {aluno['situação']}')
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
    print(f'Aluno em {aluno['situação']}')
else:
    aluno['situação'] = 'Reprovado'
    print(f'Aluno {aluno['situação']}')
print('-+'*20)
for k, i in aluno.items():
    print(f'{k} = {i}')