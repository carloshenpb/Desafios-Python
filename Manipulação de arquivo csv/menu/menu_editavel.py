def menu (nome_menu, opcoes):
    print('==='*20)
    print(f'{nome_menu}'.upper().center(60))
    print('==='*20)
    contador = 1
    for item in opcoes:
        print(f'{contador} - {item}')
        contador += 1
    print('==='*20)
    opcao = int(input('Digite a opção que deseja: '))
    print('==='*20)
    return opcao


