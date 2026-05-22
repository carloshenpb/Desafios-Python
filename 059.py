from time import sleep

# Lendo os Valores
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))

# Menu
user = 0
while user != 5:
    user = int(input('''Escolha no menu o que deseja fazer com esses valores:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    '''))
    if user == 1:
        soma = n1 + n2
        print(f'A soma dos valores é: {n1} + {n2} = {soma}')
        sleep(1)
    elif user == 2:
        multi = n1 * n2
        print(f'A multiplicação dos valores é: {n1} * {n2} = {multi}')
        sleep(1)
    elif user == 3:
        print(f'O maior valor digitado é: {max(n1, n2)}')
        sleep(1)
    elif user == 4:
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))
    elif user == 5:
        print('Encerrando o Programa!')
    else:
        print('Opção inválida! Tente novamente!')
    print('=-='*20)
print('FIM DO PROGRAMA!')
