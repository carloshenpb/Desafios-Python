def dobro(v):
    """
    Calcula o dobro de um valor
    :param v: Armazena o valor inserido
    :return: Retorna o dobro do valor armazenado no parametro v
    """
    d = v*2
    return d

def metade(v):
    """
    Calcula a metade de um valor
    :param v: Armazena o valor inserido
    :return: Retorna a metade do valor armazenado em v
    """
    m = v/2
    return m

def aumentar(v, taxa):
    """
    Calcula o aumento de um determinado valor de acordo com a taxa inserida.
    :param v: Armazena o valor inicial que será reajustado ( ex: preço de um produto )
    :param taxa: Armazena a porcentagem do aumento ( ex: inserir 5 para aumentar 5% )
    :return: O valor original acrescido com a taxa de aumento.
    """
    au = v * taxa/100
    return v + au

def diminuir(v, taxa):
    """
    Calcula a subtração de um determinado valor de acordo com a taxa inserida
    :param v: Armazena o valor inicial que será reajustado ( ex: preço de um produto )
    :param taxa: Armazena a porcentagem que será subtraída do valor original ( ex: inserir 5 para subtrair 5% )
    :return: O valor original subtraído pela taxa de subtração.
    """
    di = v * taxa/100
    return v - di

def moeda(v = 0, moeda = 'R$'):
    """
    Modifica a formatação original do python de acordo com o Real R$ ou a moeda escolhida
    :param v: Armazena o valor inserido ( ex: o preço de um produto )
    :param moeda: Armazena a moeda utilizada ( ex: R$ -> Real ou US$ -> Dolar)
    :return: O valor armazenado em v com a formatação de moeda.
    """
    return f'{moeda}{v:.2f}'.replace('.', ',')