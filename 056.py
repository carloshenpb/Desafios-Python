soma_idades = 0
nome_mais_velho = str('')
idade_mais_velho = 0
contagem = 0
for pessoas in range(1, 5):
    print(f'---- {pessoas}° PESSOA ----')
    nome = str(input('Qual seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = str(input('[H/M] ').lower())
#Captando nome e idade do homem mais velho
    if sexo == 'h':
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            nome_mais_velho = nome
#Somando idades para calcular a média
    soma_idades += idade
#Contando quantas mulheres têm menos de 20 anos
    if sexo == 'm':
        if idade < 20:
            contagem +=1
#Calculando a média e idade
media_idade = soma_idades/4

#Mostrando resultados
print(f'A média de idade é {media_idade}')
print(f'O homem mais velho é o {nome_mais_velho}')
if contagem == 1:
    print('Apenas uma mulher possui menos de 20 anos!')
else:
    print(f'{contagem} mulheres possuem menos de 20 anos!')