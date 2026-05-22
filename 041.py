from datetime import date
#captando ano de nascimento do competidor
ano_nasci = int(input('Qual o ano de nascimento do competidor? '))

#calculando a idade atual do competidor
ano_atual = date.today().year
idade_compt = ano_atual - ano_nasci

#Definindo a categoria do competidor
if idade_compt <= 9:
    print('O competidor deverá competir na categoria MIRIM!')
elif idade_compt <=14:
    print('O competidor deverá competir na categoria INFANTIL!')
elif idade_compt <= 19:
    print('O competidor deverá competir na categoria JUVENIL!')
elif idade_compt <= 25:
    print('O competidor deverá competir na categoria SÊNIOR!')
else:
    print('O competidor deverá competir na categoria MASTER!')