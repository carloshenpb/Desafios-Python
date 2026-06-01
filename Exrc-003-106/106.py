def ajuda(comando):
        return help(comando)


#Programa principal
while True:
    comando = str(input('Digite a Função ou Biblioteca que deseja saber o manual: ')).strip()
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando= comando)
