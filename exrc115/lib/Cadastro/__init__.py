from exrc115.lib.Arquivo import testararquivo
from exrc115.lib.Exibição import linha
from exrc113.lernúmeros import leiaint

def leialetras(msg):
    while True:
        try:
            entrada = str(input(msg)).strip()
            if entrada == '' or not entrada.replace(' ', '').isalpha():
                raise TypeError('ERRO: Entrada inválida!')
        except TypeError:
            print('\033[0;31mERRO: Entrada Inválida! (digite somente letras!)\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO Usuário não digitou nada! \033[m')
            return '<Desconhecido>'
        else:
            return entrada

def cadastrodeusuers(arq):
    testararquivo(arq)
    try:
        linha('+=', 30)
        nome = leialetras('\033[0;33mInserir nome: \033[m')
        idade = leiaint('\033[0;33mInserir idade: \033[m')
        linha('+=', 30)
    except (ValueError, TypeError):
        print('\033[0;31mERRO: Digitação inválida digite algo válido.\033[m')
    except KeyboardInterrupt:
        print('\033[0;31mERRO: Digite alguma coisa!')
    else:
        try:
            with open(arq, 'at') as arquivo:
                arquivo.write(f'\n{nome};{idade}')
        except Exception as erro:
            print(f'\033[0;31mERRO: Erro ao escrever algo no arquivo! {erro}\033[m')
        else:
            return print('\033[0;33mRegistro bem sucedido!\033[m')
