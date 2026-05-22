num = contador = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    contador = contador + 1
    soma = soma + num
    num = int(input('Digite um número: '))
print(f'Foram digitados {contador} números!')
print(f'A soma entre esses números é igual a: {soma}')
print('FIM')
