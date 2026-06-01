def leiaint(entrada):
    while True:
        try:
            valor =(input(entrada)).strip()
            num = int(valor)
        except (ValueError, TypeError):
            if valor == '':
                print('\033[0;31mERRO! É preciso digitar um número!\033[m')
                continue
            else:
                print('\033[0;31mERRO! O Valor digitado não é um número inteiro! Tente novamente....\033[m')
                continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuário prefiriu não digitar um número!\033[m')
            return 0
        else:
            return num


def leiafloat(entrada):
    while True:
        try:
            valor = (input(entrada)).strip().replace(',', '.')
            num = float(valor)
        except (ValueError, TypeError):
            if valor == '':
                print('\033[0;31mERRO! É preciso digitar um número!\033[m')
                continue
            else:
                print('\033[0;31mERRO! O valor digitado não é um número real! Tente novamente....\033[m')
                continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar um número\033[m')
            return 0
        else:
            return str(num).replace('.', ',')