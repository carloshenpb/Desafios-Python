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
    -> Documentação da API Brasil API (1.0.0): [[https://brasilapi.com.br/docs]]
### Funcionamento do código principal:
        [Início do Programa]
         │
         ▼
┌─────────────────────────────────┐
│ Carregar dados do arquivo       │ <─── Se o arquivo não existir,
│ 'empresas.json' para a memória  │      inicia uma lista vazia []
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│     Exibir Menu de Opções       │ ◄────────────────────────┐
└─────────────────────────────────┘                          │
         │                                                   │
         ▼                                                   │
[Usuário escolhe uma opção]                                  │
         │                                                   │
         ├──► Opção 1: Buscar Novo CNPJ                      │
         │    │                                              │
         │    ▼                                              │
         │   Fazer requisição à Brasil API ──────────────────┤
         │   (Captura: Dados básicos + Natureza Jurídica)    │
         │    │                                              │
         │    ▼                                              │
         │   Separar Cidade/UF + Montar Endereço Extenso ────┤
         │    │                                              │
         │    ▼                                              │
         │   Dar .append() na lista em memória               │
         │                                                   │
         ├──► Opção 2: Exibir Empresas Salvas                │
         │    │                                              │
         │    ▼                                              │
         │   Escolher formato: [1] Simples ou [2] Tabela ────┤
         │    │                                              │
         │    ▼                                              │
         │   Ler da memória ──► Renderizar dados ────────────┤
         │                                                   │
         ├──► Opção 3: Filtrar CNPJ (Novidade!)              │
         │    │                                              │
         │    ▼                                              │
         │   Escolher tipo de filtro:                        │
         │   ├── [1] Por Cidade                              │
         │   ├── [2] Por Estado                              │
         │   └── [3] Por Natureza Jurídica                   │
         │    │                                              │
         │    ▼                                              │
         │   Varrer a lista verificando a condição ──────────┤
         │    │                                              │
         │    ▼                                              │
         │   Exibir apenas os resultados correspondentes     │
         │                                                   │
         ├──► Opção 4: Adicionar Manualmente                 │
         │    │                                              │
         │    ▼                                              │
         │   Pedir inputs (incluindo Natureza Jurídica)      │
         │    │                                              │
         │    ▼                                              │
         │   Montar dicionário ──► .append() na lista ───────┤
         │                                                   │
         ├──► Opção 5: Editar Dado Existente                 │
         │    │                                              │
         │    ▼                                              │
         │   Buscar CNPJ na lista ──► Alterar chaves ────────┤
         │                                                   │
         └──► Opção 6: Sair do Programa                      │
              │                                              │
              ▼                                              │
         ┌───────────────────────────────┐                   │
         │ Salvar lista atualizada       │                   │
         │ no arquivo 'empresas.json'    │                   │
         └───────────────────────────────┘                   │
              │                                              │
              ▼                                              │
         [Fim do Programa]                                   │
                                                             │
   (Se o usuário escolher uma opção inválida)                │
   └─────────────────────────────────────────────────────────┘