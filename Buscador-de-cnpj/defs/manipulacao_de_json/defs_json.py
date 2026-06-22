import json
from os.path import join
from defs.menus.menus import so_opcoes, título_simples

pasta_padrao = r'C:\Users\carlo\PycharmProjects\Desafios\Buscador-de-cnpj\arquivos'
arquivo_padrao = join(pasta_padrao, f"empresas.json")

def exibir_json_simples():
    """
    Lê o arquivo JSON padrão e exibe no terminal a relação de CNPJs cadastrados
    e suas respectivas estruturas de dados brutas de forma direta e simplificada.
    Utilizado para fins de visualização da organização e aninhamento do arquivo.
    """
    with open(arquivo_padrao, "r", encoding="utf-8") as arquivo:
        empresas = json.load(arquivo)
        for cnpj, dicionario_cnpj in empresas.items():
            print('___'*30)
            print(f'{cnpj} :')
            for dado, valor in dicionario_cnpj.items():
                print(f'{dado} : {valor}')

def exibir_json_tabela():
    """
    Lê o arquivo JSON padrão e exibe os dados das empresas em formato de tabela no terminal.
    Modela colunas alinhadas com larguras fixas para organizar visualmente as informações principais.
    """
    with open(arquivo_padrao, "r", encoding="utf-8") as arquivo:
        empresas = json.load(arquivo)
        print('Empresas cadastradas:')
        print(f'{"CNPJ":<18}|{"Razão Social":<40}|{"Nome Fantasia":<30}|{"Município":<20}|{"UF":<4}|{"Natureza Jurídicia":<30}')
        for cnpj, dicionario_cnpj in empresas.items():
            print('-----'*30)
            razao_social = dicionario_cnpj['razão social'][:40]
            nome_fantasia = dicionario_cnpj['nome fantasia'][:30]
            municipio = dicionario_cnpj['endereço']['municipio'][:20]
            uf = dicionario_cnpj['endereço']['uf'][:4]
            natureza_juridica = dicionario_cnpj['natureza jurídica'][:30]
            print(f'{cnpj:<18}|{razao_social:<40}|{nome_fantasia:<30}|{municipio:<20}|{uf:<4}|{natureza_juridica:<30}')

def filtrar_cnpj_especifico(cnpj):
    """
    Busca e exibe detalhadamente todas as informações de um CNPJ específico 
    gravado no arquivo JSON local, incluindo dados de endereço e a lista de contatos.

    Argumentos:
        cnpj (str ou int): O CNPJ a ser localizado e exibido.
    """
    cnpj = ''.join(caractere for caractere in str(cnpj) if caractere.isdigit())
    try:
        with open(arquivo_padrao, "r", encoding="utf-8") as arquivo:
            empresas = json.load(arquivo)
            if not cnpj in empresas:
                print('ERRO: Este CNPJ não possuí registro!')
            else:
                dados_empresa = empresas[cnpj]
                título_simples(f'Dados da {dados_empresa.get("razão social")}')
                print(f'Razão social : {dados_empresa.get("razão social")}')
                print(f'CNPJ : {dados_empresa.get("cnpj")}')
                print(f'Nome fantasia : {dados_empresa.get("nome fantasia")}')
                print(f'Natureza Jurídica: {dados_empresa.get("natureza jurídica")}')
                print('--'*60)
                contatos = dados_empresa.get("contatos")
                print('Contatos: ')
                print(f'e-mail : {contatos.get("e-mail")}')
                telefones = contatos.get("telefones", [])
                for num, telefones in enumerate(telefones, start = 1):
                    print(f'Telefone {num} : ({telefones.get("ddd")}) {telefones.get("número_telefone")}')
                print('--'*60)
                endereco = dados_empresa.get("endereço")
                print(f'Endereço : {endereco.get("tipo logradouro")} {endereco.get("logradouro")}, {endereco.get("número da residência")}, {endereco.get("complemento")}')
                print(f'Bairro : {endereco.get("bairro")}')
                print(f'Cidade : {endereco.get("municipio")}-{endereco.get("uf")}')

    except Exception as erro:
        print(f'ERRO: {erro.__class__.__name__} : {erro}')

def filtros_json_padrao():
    filtros = ['Filtrar por UF', 'Filtrar por Cidade', 'Filtrar por NJ']
    user = so_opcoes(filtros)
    
    with open(arquivo_padrao, "r", encoding="utf-8") as arquivo:
        empresas = json.load(arquivo)
    
    if user == 1:
        uf = str(input('Digite a UF: ')).strip().upper()
        try:
            teste_empresa = False
            for cnpj, dados_empresa in empresas.items():
                 if (
                "endereço" in dados_empresa
                and dados_empresa["endereço"]["uf"] == uf
                ):
                     if teste_empresa == False:
                         print('~~'*60)
                         print(f'Empresas localizadas em {uf}:')
                         print('~~'*60)
                         print(f'{"CNPJ":<18}|{"Razão Social":<40}|{"Endereço":<40}|{"Bairro":<25}|{"Município":<25}|{"UF":<4}|')
                         print('=='*80)
                     teste_empresa = True
                     razao_social = dados_empresa.get("razão social", "Não informada")[:40]
                     dados_endereco = dados_empresa.get("endereço")
                     municipio = dados_endereco.get("municipio", "Não informado")[:25]
                     uf_empresa = dados_endereco.get("uf", "Não Informada")[:4]
                     logradouro = dados_endereco.get("logradouro", "Não informado")[:30]
                     tipo_logradouro = dados_endereco.get("tipo logradouro", "Não informado")
                     numero_residencia = dados_endereco.get("número da residência", "S/N")
                     complemento = dados_endereco.get("complemento", "S/C")
                     endereco_extenso = f'{tipo_logradouro} {logradouro}, {numero_residencia}, {complemento}'[:40]
                     bairro = dados_endereco.get("bairro")[:25]
                     print(f'{cnpj:<18}|{razao_social:<40}|{endereco_extenso:<40}|{bairro:<25}|{municipio:<25}|{uf_empresa:<4}|')
                     print('--'*80)
            if teste_empresa == False:
                print('xx'*60)
                print(f'AINDA NÃO EXISTEM EMPRESAS CADASTRADAS NA UF {uf}')
                print('xx'*60)
        except Exception as e:
            print(f'ERRO : {e.__class__.__name__} : {e}')
    elif user == 2:
        cidade = str(input('Digite a cidade: ')).strip().upper()
        try:
            teste_empresa = False
            for cnpj, dados_empresa in empresas.items():
                if(
                    "endereço" in dados_empresa
                    and dados_empresa["endereço"]["municipio"] == cidade
                ):
                    if teste_empresa == False:
                        print('~~'*60)
                        print(f'Empresas localizadas em {cidade}:')
                        print('~~'*60)
                        print(f'{"CNPJ":<18}|{"Razão Social":<40}|{"Endereço":<40}|{"Bairro":<25}|{"Município":<25}|{"UF":<4}|')
                        print('=='*80)
                    teste_empresa == True
                    razao_social = dados_empresa.get("razão social", "Não informada")[:40]
                    dados_endereco = dados_empresa.get("endereço")
                    municipio = dados_endereco.get("municipio", "Não informado")[:25]
                    uf_empresa = dados_endereco.get("uf", "Não Informada")[:4]
                    tipo_logradouro = dados_endereco.get("tipo logradouro", "Não informado")
                    logradouro = dados_endereco.get("logradouro", "Não informado")[:30]
                    numero_residencia = dados_endereco.get("número da residência", "S/N")
                    complemento = dados_endereco.get("complemento", "S/C")
                    endereco_extenso = f'{tipo_logradouro} {logradouro}, {numero_residencia}, {complemento}'[:40]
                    bairro = dados_endereco.get("bairro")[:25]
                    print(f'{cnpj:<18}|{razao_social:<40}|{endereco_extenso:<40}|{bairro:<25}|{municipio:<25}|{uf_empresa:<4}|')
                    print('--'*80)
            if teste_empresa == False:
                print('xx'*60)
                print(f'NÃO EXISTEM EMPRESAS CADASTRADAS NO MUNICIPIO DE {cidade}')
                print('xx'*60)
        except Exception as e:
            print(f'ERRO : {e.__class__.__name__}:{e}')
    elif user == 3:
        natureza_juridica = str(input('Digite a natureza jurídica: ')).strip().title()
        try:
            teste_empresa = False
            for cnpj, dados_empresa in empresas.items():
                if("natureza jurídica" in dados_empresa 
                and dados_empresa["natureza jurídica"] == natureza_juridica):
                    if teste_empresa == False:
                        print('~~'*60)
                        print(f'{natureza_juridica}: ')
                        print('~~'*60)
                        print(f'{"CNPJ":<18}|{"Razão Social":<40}|{"Natureza Jurídica":<30}')
                        print('=='*60)
                    teste_empresa = True
                    razao_social = dados_empresa.get("razão social", "Não informada")[:40]
                    ntrza_juri = dados_empresa.get("natureza jurídica")
                    print(f'{cnpj:<18}|{razao_social:<40}|{ntrza_juri:<30}')
                    print('--'*80)
            if teste_empresa == False:
                print('xx'*60)
                print(f'NÃO EXISTEM EMPRESAS DO TIPO {natureza_juridica.upper()}')
                print('xx'*60)
        except Exception as e:
            print(f'ERRO : {e.__class__.__name__}:{e}')