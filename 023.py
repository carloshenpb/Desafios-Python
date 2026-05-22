
# num = str(input('Digite um número de 0 a 9999: '))
# print('Analisando o número {}...'.format(num))
# print('Unidade: {}'.format(num[3]))
# print('Dezena: {}'.format(num[2]))
# print('Centena: {}'.format(num[1]))
# print('Milhar: {}'.format(num[0]))
# Obs: não deu certo!
'''Solução do professor guanabara!'''

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número {}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))