# Tupla com números de 0 a 20 por extenso
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
# Digitando o número desejado
while True:
    user = int(input('Digite um número entre 0 e 20:'))
    if 0 <= user <= 20:
        print(f'Você digitou o número {numeros[user].upper()}')
    else:
        print('Erro! Tente novamente!')
    user_2 = ' '
    while user_2 not in 'SsNn':
        user_2 = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if user_2 in 'Nn':
        break
print('FIM')