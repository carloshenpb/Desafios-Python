print('=!='*30)
print(' '*15, 'SEQUÊNCIA DE FIBONACCI')
print('=!='*30)
#Indicando quantos termos serão exibidos
num_terms = int(input('Quantos termos você deseja saber? '))
#2 primeiros termos
term1 = 0
term2 = 1
print(f'{term1} -> {term2}', end=' -> ')
#Inciando o loop
cont = 2
while cont < num_terms:
    term3 = term1 + term2
    print(term3, end=' -> ')
    term1 = term2
    term2 = term3
    cont += 1
print('FIM')
