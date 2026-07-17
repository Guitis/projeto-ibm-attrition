## Organização do projeto

```
├── .env               <- Arquivo de variáveis de ambiente
├── .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git
├── ambiente.yml       <- O arquivo de requisitos para reproduzir o ambiente de análise
├── LICENSE            <- Licença de código aberto se uma for escolhida
├── README.md          <- README principal para desenvolvedores que usam este projeto.
|
├── dados              <- Arquivos de dados para o projeto e streamlit.
|
├── modelos            <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos
|
├── notebooks          <- Cadernos Jupyter. A convenção de nomenclatura é um número (para ordenação),
│                         as iniciais do criador e uma descrição curta separada por `-`, por exemplo
│                         `01-gtb-eda`.
│
|   └──src             <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python
|      ├── config.py    <- Configurações básicas do projeto
|      └── graficos.py  <- Scripts para criar visualizações exploratórias e orientadas a resultados
|
├── referencias         <- Dicionários de dados, manuais e todos os outros materiais explicativos.
|     |
|     |__ 01_sobre_a_base.md <- Markdown explicativo sobre a base
|     |__ 02_dicionario_de_dados.md <- Dicionário explicativo dos dados da base
|     |__ 03_organizacao_do_projeto <- Markdown explicativo sobre a organização dos arquivos/pastas do projeto
|
|
├── relatorios         <- Análises geradas em HTML, PDF, LaTeX, etc.
|   |__ gif_ibm.gif    <- Gif demonstrando a utilização do projeto
|   |
│   └── imagens        <- Gráficos e figuras gerados para serem usados em relatórios
|
├── ambiente.yml       <- Lista de todas as ferramentas e versões de códigos que o projeto precisa para roda
├── home.py            <- Página principal do web app do streamlit
├── LICENSE            <- Documento para estabelecer as regras legais de uso
├── requirements.txt   <- Lista de todas as bibliotecas (pacotes extras) e as versões exatas a qual foi criado o projeto
```