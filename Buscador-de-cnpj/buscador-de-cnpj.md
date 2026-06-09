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
    -> Exibir os dados:
        - Em tabela 
        - De maneira simples
    -> Editar dados manualmente:
        - Adiconar empresa de maneira manual no arquivo .json
        - Editar dado salvo no arquivo .json

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
         │   Fazer requisição à Brasil API ──► Tratar dados ─┤
         │   e dar .append() na lista                        │
         │                                                   │
         ├──► Opção 2: Exibir Empresas Salvas                │
         │    │                                              │
         │    ▼                                              │
         │   Ler da memória ──► Exibir (Simples ou Tabela) ──┤
         │                                                   │
         ├──► Opção 3: Adicionar Manualmente                 │
         │    │                                              │
         │    ▼                                              │
         │   Pedir inputs do usuário ──► .append() na lista ─┤
         │                                                   │
         ├──► Opção 4: Editar Dado Existente                 │
         │    │                                              │
         │    ▼                                              │
         │   Buscar CNPJ na lista ──► Alterar chaves ────────┤
         │                                                   │
         └──► Opção 5: Sair do Programa                      │
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