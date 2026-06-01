num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite mais um: '))
num_3 = int(input('Digite mais um: '))
num_4 = int(input('Digite só mais um: '))
tupla = (num_1, num_2, num_3, num_4)
# Verificando quantos 9 foram digitados
print('_'*40)
print(f'> O número 9 foi digitado {tupla.count(9)} vezes' if 9 in tupla else '> O valor 9 não foi digitado')
# Verificando a posição do 1° valor 3
print(f'> O valor 3 foi digitado pela primeira vez na posição {tupla.index(3)}.' if 3 in tupla else '> O valor 3 não foi digitado')
# Verificando quantos números são par
cont = 0
for n in range (0,4):
    if tupla [n] % 2 == 0:
        cont += 1
print('>Não foram digitados números pares.' if cont == 0 else f'> Foram digitados {cont} números pares.')
