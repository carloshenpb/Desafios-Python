'''soma = 0
#Laço de Repetição
for c in range(1, 501):
#Primeira condição ( número ímpares )
    if c % 2 == 1:
#Segunda condição ( números primos )
        if c % 3 == 0:
            soma += c
print(soma)'''

#Solução do Guanabara:

soma = 0
cont = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n # soma = soma + n
        cont += 1 # cont = cont + 1
print(f'A soma de todos os {cont} valores é {soma}')
