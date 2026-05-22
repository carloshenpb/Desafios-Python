# Inicio: Lendo o 1° termo e a razão
primeiro_term = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

# Definindo quantos termos serão exibidos
termos = int(input('Quantos termos dessa PA você deseja saber? '))

# Iniciando o loop
term = primeiro_term
cont = 1
total = 0
mais = termos
## 1° loop
while mais != 0:
    total += mais
## 2° loop
    while cont <= total:
        print(term, end='->')
        term += razao
        cont += 1
    print('PAUSA')
    print('=-=' * 10)
    mais = int(input('Quantos termos deseja saber a mais? '))
print(f'FIM! A PA se encerrou com {total} termos exibidos!')