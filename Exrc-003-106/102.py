def linha():
    print('=-' * 20)
def fatorial(num, show = False):
    """-> Calcula o fatorial de um número
    :param num: O número que terá o fatorial cálculado
    :param show: (Opicional) Exibição detalhada do cálculo
    :return: Retorna o fatorial de num"""
    print(f'{num}! = ', end='')
    ftr = 1
    for cont in range(num, 0, -1):
        if show:
            print(cont, end='')
            print(' x ' if cont > 1 else ' = ', end='')
        ftr *= cont
    return ftr

#Programa principal
n = int(input('Digite um número: '))
linha()
print(fatorial(n))
linha()
print(fatorial(n, show=True))
linha()
help(fatorial)
