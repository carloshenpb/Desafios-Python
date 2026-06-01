from datetime import date

ano_atual = date.today().year
contador = 0
contador_2 = 0
#Captando datas de nascimento
for pessoas in range(1, 8):
    ano_nasc = int(input(f'Digite o ano de nascimento da {pessoas}° pessoa: '))
    idade_atual = ano_atual - ano_nasc

    if idade_atual >= 21:
        contador += 1
    else:
        contador_2 += 1
print(f'O número de maiores de idade é {contador}')
print(f'O número de menores de idade é {contador_2}')