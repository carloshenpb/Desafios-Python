def moeda(v: float = 0, moed = 'R$'):
    """
      Modifica a formatação original do python de acordo com o Real R$ ou a moeda escolhida.
      :param v: Armazena o valor float inserido ( ex: o preço de um produto ).
      :param moed: Armazena a moeda utilizada ( ex: R$ -> Real ou US$ -> Dolar).
      :return: O valor armazenado em v com a formatação de moeda.
      """
    return f'{moed}{v:.2f}'.replace('.', ',')

def dobro(v=0, f=True):
    """
    Calcula o dobro de um valor e retorna a formatação de moeda(ex: R$ 15,50) ou formatação padrão do python( ex: 15.5).
    :param v: Armazena o valor inserido ( ex: O preço de um produto ).
    :param f: Indica se o resultado deve ser formatado pela função moeda (True) ou retornar o valor puro (False).
    :return: O dobro do valor v, com ou sem formatação de moeda.
    """
    d = v*2
    if not f:
        return d
    return moeda(d)

def metade(v=0, f=True):
    """
    Calcula a metade de um valor e retorna a formatação de moeda(ex: R$ 15,50) ou formatação padrão do python( ex: 15.5).
    :param v: Armazena o valor inserido ( ex: O preço de um produto ).
    :param f:Indica se o resultado deve ser formatado pela função moeda (True) ou retornar o valor puro (False).
    :return: A metade do valor v, com ou sem formatação de moeda.
    """
    m = v/2
    if not f:
        return m
    return moeda(m)

def aumentar(v=0, taxa=0, f=True):
    """
    Calcula o aumento de um determinado valor de acordo com a taxa inserida
    e retorna a formatação de moeda(ex: R$ 15,50) ou formatação padrão do python( ex: 15.5).
    :param v: Armazena o valor inicial que será reajustado ( ex: preço de um produto )
    :param taxa: Armazena a porcentagem do aumento ( ex: inserir 5 para aumentar 5% )
    :param f: Indica se o resultado deve ser formatado pela função moeda (True) ou retornar o valor puro (False).
    :return: O valor original acrescido do com a taxa de aumento, com ou sem formatação de moeda
    """
    au = v + (v * taxa/100)
    if not f:
        return au
    return moeda(au)

def diminuir(v=0, taxa=0, f=True):
    """
    Calcula a subtração de um determinado valor de acordo com a taxa inserida
    e retorna a formatação de moeda(ex: R$ 15,50) ou a formatação padrão do Python (ex: 15.5)
    :param v: Armazena o valor inicial que será reajustado ( ex: preço de um produto )
    :param taxa: Armazena a porcentagem da subtração ( ex: inserir 5 para subtrair 5% )
    :param f: Indica se o resultado deve ser formatado ( True ) ou retornar o valor padrão ( False )
    :return: O valor original subtraído pela taxa de subtração, com ou sem formatação de moeda.
    """
    di = v - (v * taxa/100)
    if not f:
        return di
    return moeda(di)
