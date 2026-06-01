num = int(input('Digite um número: '))

# Casos especiais:
if num == 1:
    print('O número 1 não é primo!')
elif num == 2:
    print('O número 2 é primo!')

# Checando se o número digitado é primo ou não:
else:
    for c in range(2, num):
        if num % c == 0:
            print(f'O número {num} não é primo!')
            break
    else:
        print(f'O número {num} é primo')
