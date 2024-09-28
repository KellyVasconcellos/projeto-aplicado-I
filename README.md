# projeto-aplicado-I

## Análise Exploratória de Dados do Dataset “Notificação de Suspeita de Covid-19” - Comparação Entre os Estados Mais e Menos Populosos das Regiões Brasileiras.

## Integrantes do Grupo

- ANNA TERESA SOARES SACCHI - RA: 10441273  
- GLEIDER MACKEDANZ DE CAMPOS - RA: 10433464  
- GUSTAVO AZEVEDO GOMYDE - RA: 10424543  
- KELLY HARO VASCONCELLOS - RA: 10441014


## Contexto do Estudo

Este estudo visa realizar uma análise comparativa da incidência de suspeita de covid-19 em estados com os maiores e menores índices populacionais em cada região do Brasil. A análise se concentrará em dados brutos relacionados à síndrome gripal suspeita de covid-19, abrangendo estados de cada região: Norte, Nordeste, Sul, Centro-Oeste e Sudeste.

## Referências de Aquisição do Dataset

- **Origem dos Dados:** Os dados são oriundos do sistema e-SUS Notifica, disponibilizados pelo Ministério da Saúde e pela Secretaria de Vigilância em Saúde e Ambiente (SVSA). O dataset contém informações sobre a síndrome gripal leve e moderada suspeita de covid-19.
- **Limitações de Uso:** Dados públicos podem ter limitações relacionadas à precisão, atualização e escopo da cobertura. Estados e municípios que utilizam sistemas próprios de notificação de casos suspeitos de covid-19 estão em processo de integração com o e-SUS Notifica, o que pode resultar em diferenças substanciais nos dados até a finalização do processo de integração.
- **Período da Coleta:** Dados coletados desde março de 2020 até o ano de 2024.

## Descrição do Dataset

O dataset contém informações detalhadas sobre casos de síndrome gripal leve e moderada com suspeita de covid-19, incluindo variáveis como sintomas, condições de saúde, dados demográficos e resultados de testes. As principais colunas incluem: sintomas, profissional da saúde, raça e cor, outros sintomas, cbo, condições, sexo, estado, município, origem, datas sobre a evolução do caso, dados de vacinação e realização de testagem.

## Estados Utilizados no Estudo

Utilizaremos os estados mais e menos populosos de cada região para o estudo:

- **Sul:** Paraná (PR) x Santa Catarina (SC)
- **Norte:** Pará (PA) x Tocantins (TO)
- **Sudeste:** São Paulo (SP) x Espírito Santo (ES)
- **Centro-Oeste:** Goiás (GO) x Mato Grosso do Sul (MS)
- **Nordeste:** Bahia (BA) x Sergipe (SE)

## Metas

- Comparar a evolução do Covid-19 entre os grupos mais e menos populosos nas regiões brasileiras.
- Analisar a volumetria das vacinas aplicadas por laboratório.
- Comparar a relação entre sexo e idade dos pacientes com suspeita de covid-19.
- Relacionar dados climáticos com os casos de covid-19.

## Cronograma de Atividades

**Etapa 1 - Coleta e Preparação dos Dados (Semana 1 e 2)**

- Obter os dados do dataset.
- Preparar e limpar os dados para análise.
- Elaborar proposta de solução analítica.

**Etapa 2 - Análise Exploratória (Semana 3 e 4)**

- Realizar análise descritiva e exploratória dos dados.
- Criar visualizações para comparar os estados selecionados.

**Etapa 3 - Análise Comparativa (Semana 5 e 6)**

- Comparar a incidência de covid-19 entre os estados.
- Interpretar os resultados e identificar padrões regionais.

**Etapa 4 - Texto e Apresentação dos Resultados (Semana 7 e 8)**

- Revisar e ajustar a proposta analítica e a análise exploratória (Data Storytelling).
- Verificar a documentação dos scripts no GitHub.

**Etapa 5 - Revisão e Entrega (Semanas finais)**

- Finalizar e formatar a proposta e a análise.
- Entregar e apresentar o projeto finalizado.

## Análise de Dados

Nesta etapa estamos entregando os scripts em Python das análises:
- Comparar a evolução do Covid-19 entre os grupos mais e menos populosos nas regiões brasileiras está no script: **""**

- Volumetria das vacinas aplicadas por laboratório está no script: **"vacinacao.py"**

- Comparar a relação entre sexo e idade dos pacientes com suspeita de
covid-19 está no script: **"media_sexo_idade.py"**

- Relacionar dados climáticos com os casos de covid-19 está no script: **""**

## Links Úteis

- [Link do Repositório](https://github.com/KellyVasconcellos/projeto-aplicado-I)

## Link dos Datasets

- **Síndromes Gripais Leve:** [Dataset de Notificações de Síndrome Gripal Leve](https://opendatasus.saude.gov.br/dataset/notificacoes-de-sindrome-gripal-leve-2024/resource/95bd0eb5-78fa-4223-9a90-ed93ce685d69?inner_span=True)
- **Dados Meteorológicos (Dividido por Anos):** [Portal do INMET](https://portal.inmet.gov.br/dadoshistoricos)
