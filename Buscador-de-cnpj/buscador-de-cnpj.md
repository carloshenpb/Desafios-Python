# Buscador de CNPJ (Python)

## Mini Projeto com objetivo de aprender sobre manipulação de arquivos .json e uso de APIs com python.
### Objetivos:
    -> Buscar sobre um determinado CNPJ através da API: Brasil API (1.0.0)
    -> Salvar os dados em um arquivo .json que deve ter as seguintes informações:
        - nome fantasia
        - razão social
        - cnpj
        - endereço por extenso
            - Rua Carlos Drummond de Andrade, 61, Vale Dourado, Petrolina-PE.
        - cep
        - contatos:
            - tel-1 : 0000-0000
            - tel-2 : 0000-0000
            - e-mail: emailexemplo@gmail.com
        - Natureza Juridica
    -> Exibir os dados:
        - Em tabela 
        - De maneira simples
    -> Editar dados manualmente:
        - Adiconar empresa de maneira manual no arquivo .json
        - Editar dado salvo no arquivo .json
    -> Filtrar CNPJ por condições como:
        - cidade
        - estado
        - natureza juridica

### Materiais utilizados para pesquisa:
    -> -> Cofre pessoal do Obsidian. 
    -> I.A (Claude e Gemini).
    -> Tutoriais no youtube.
    -> Documentação da API 
### Funcionamento do código principal:
[MENU PRINCIPAL] BUSCADOR DE CNPJ
 ├── 1. Buscar CNPJ
 │       └── Pede o CNPJ, consome a API e salva no JSON.
 │
 ├── 2. Exibir lista de CNPJ
 │       ├── 1. Exibição simples  -> Mostra os dados brutos aninhados.
 │       └── 2. Exibição tabular  -> Organiza as empresas em colunas alinhadas.
 │
 ├── 3. Filtrar CNPJs
 │       ├── 1. Filtrar dados de um único CNPJ -> Busca direta O(1) na memória.
 │       └── 2. Outros Filtros -> Submenu por UF, Município ou Natureza Jurídica.
 │
 ├── 4. Editar dados manualmente
 │       ├── 1. Adicionar Empresa Manualmente  -> Cria um registro do zero sem API.
 │       └── 2. Editar dados de CNPJ existente -> Navega por chaves e subdicionários para alterar valores.
 │
 └── 5. Sair
         └── Encerra o sistema.