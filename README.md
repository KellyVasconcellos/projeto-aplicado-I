# Science for Life SA 

Através da análise de dados temos como missão contribuir para gestão de risco de doenças infecciosas, fornecendo dados sobre padrões e tendências de disseminação das doenças


## Integrantes do Grupo

- ANNA TERESA SOARES SACCHI - RA: 10441273  
- GLEIDER MACKEDANZ DE CAMPOS - RA: 10433464  
- GUSTAVO AZEVEDO GOMYDE - RA: 10424543  
- KELLY HARO VASCONCELLOS - RA: 10441014

## Tema

Análise Exploratória de Dados do Dataset “Notificação de Suspeita de Covid-19” - Comparação Entre os Estados Mais e Menos Populosos das Regiões Brasileiras.

## Contexto do Estudo

Este estudo visa realizar uma análise comparativa da incidência de suspeita de covid-19 em estados com os maiores e menores índices populacionais em cada região do Brasil. A análise se concentrará em dados brutos relacionados à síndrome gripal suspeita de covid-19, abrangendo somente os estados de cada região: Norte, Nordeste, Sul, Centro-Oeste e Sudeste. Utilizaremos os estados mais e menos populosos de cada região para o estudo:

- **Sul:** Paraná (PR) x Santa Catarina (SC)
- **Norte:** Pará (PA) x Tocantins (TO)
- **Sudeste:** São Paulo (SP) x Espírito Santo (ES)
- **Centro-Oeste:** Goiás (GO) x Mato Grosso do Sul (MS)
- **Nordeste:** Bahia (BA) x Sergipe (SE)

## Análises de Dados

- Comparar a evolução do Covid-19 entre os grupos mais e menos populosos.
- Analisar a volumetria geral das vacinas aplicadas por laboratório.
- Comparar a relação entre sexo e idade dos pacientes com suspeita de covid-19 entre os grupos mais e menos populosos.
- Ocorrência de Sintomas em Casos de Óbito.
- Quantificar atuação de profissionais da área da saúde.
- Analisar os casos assintomáticos.


## Estrutura do Repositório

- **`/data`**: Contém dataset com os conjuntos de dados brutos, porém por exceder o limite de 100MB está ignorado no ".gitignore".
- **`/data/unified_datasets`**: Script em Python responsável por unir cada dataset de cada estado em um único arquivo.

- **`/report`**: Relatório final do projeto, contendo os resultados e conclusões.

- **`src/notebooks`**: Notebooks Jupyter que documentam a análise exploratória e as visualizações geradas.
- **`src/scripts`**: Scripts em Python utilizados para análise e processamento dos dados.


## Link do Dataset Público

- **Síndromes Gripais Leve:** [Dataset de Notificações de Síndrome Gripal Leve](https://opendatasus.saude.gov.br/dataset/notificacoes-de-sindrome-gripal-leve-2024/resource/95bd0eb5-78fa-4223-9a90-ed93ce685d69?inner_span=True)


## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/KellyVasconcellos/projeto-aplicado-I.git
    ```

2. Acesse a pasta do projeto:
    ```bash
    cd projeto-aplicado-I
    ```

3. Abra o projeto no Visual Studio Code:
    ```bash
    code .
    ```

4. Descompacte o arquivo ZIP na pasta `/data` e certifique-se de que o arquivo CSV resultante esteja solto nesta pasta.

5. Instale as dependências de acordo com o arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```