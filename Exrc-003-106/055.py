#Captando o peso das 5 pessoas

maior_peso = 0
menor_peso = 0

for pessoas in range(0, 5):
    peso = float(input(' Qual o seu peso? KGs '))
    if pessoas == 0:
        maior_peso = menor_peso = peso
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

#Exibindo os resultados
print(f' O maior peso lido foi {maior_peso} KGs')
print(f' O menor peso lido foi {menor_peso} KGs')