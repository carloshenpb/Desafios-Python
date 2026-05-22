def maior (*num):
    print('=~'*20)
    if len(num) == 0:
        print('Nenhum valor foi informado!')
    if len(num) == 1:
        print(f'Foi digitado apenas o número {num}.')
    if len(num) > 1:
        print('Esses foram os números: ')
        for p in num:
            print(p, end=' ')
        print()
        print(f'> Foram informados {len(num)} números.')
        print(f'> O maior valor informado foi {max(num)}')


# Programa principal
maior(1, 5, 7 ,0 ,2)
maior(4, 9 , 7)
maior(0, 1 , 5 , 10, 11)
maior(0, 6)
maior()
maior(1)
