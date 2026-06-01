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