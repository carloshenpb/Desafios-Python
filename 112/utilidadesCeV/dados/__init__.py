def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.', ).strip()
        if entrada == '' or not entrada.replace('.', '', 1).isdigit():
            print(f'\033[0;31mERRO: \"{entrada}\" não é um preço válido!\033[m')
        else:
            valido = True
            return float(entrada)
    return None