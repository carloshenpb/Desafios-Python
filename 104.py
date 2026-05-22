def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor

#Programa Principal
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')