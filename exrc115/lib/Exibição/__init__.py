from exrc113.lernúmeros import leiaint

def linha(tplin, lin = 30):
    print(tplin*lin)

def cabecalho(txt, tplin = '', center = 30, linh = 30):
    print(tplin*linh)
    print(txt.center(center))
    print(tplin * linh)

def menu(opcoes):
    cabecalho('MENU PRINCIPAL', '++', 60)
    contador = 1
    for item in opcoes:
        print(f'\033[0;33m{contador} -\033[m {item}')
        contador += 1
    linha('==')
    opcao = leiaint('\033[0;33mSua Opção: \033[m')
    return opcao

def exibirusers(arq):
    try:
        with open(arq,'rt') as arquivo:
            for lin in arquivo:
                dado = lin.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30}{dado[1]:>3} anos')
    except Exception as erro:
        print(f'\033[0;31mERRO:{erro}\033[m')
    else:
        return True



