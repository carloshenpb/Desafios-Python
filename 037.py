print('[ CONVERSOR ]')
num = int(input('Digite um número: '))
#Escolhendo para qual base o número digitado será convertido:
base = str(input('''Escolha qual para qual base deseja converter esse número:
1 para Binário
2 para Octal
3 para Hexadecimal
'''))
#Base binária:
if base == '1':
    resultado = bin(num)
    print(f'O número {num} convertido para base binária é igual a: {resultado[2:]}')
#Base octal:
elif base == '2':
    resultado = oct(num)
    print(f'O número {num} convertido para base octal é igual a: {resultado[2:]}')
#Base hexadécimal:
elif base == '3':
    resultado = hex(num)
    print(f'O número {num} convertido para base hexadecimal é igual a: {resultado[2:].upper()}')
else:
    print('Opcção invalida!')
