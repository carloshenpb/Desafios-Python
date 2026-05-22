from exrc115.lib.Exibição import cabecalho


def arquivoexiste(nome):
    try:
        arquivo = open(nome,'at')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except Exception as erro:
        print(f'\033[0;31mERRO: Não foi possível criar o arquivo "{nome}"\033[m')
        print(f'\033[0;31mERRO: {erro}\033[m')
    else:
        return print(f'\033[0;32m O arquivo "{nome}" foi criado com sucesso!\033[m')

def testararquivo(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    except Exception as erro:
        print(f'\033[0;31mERRO: {erro}\033[m')
        return False
    else:
        return True


def lerarquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except Exception as erro:
        print(f'\033[0;31mERRO: Erro ao ler o arquivo! {erro}\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS', '==', center=60)
        print(arquivo.read())


