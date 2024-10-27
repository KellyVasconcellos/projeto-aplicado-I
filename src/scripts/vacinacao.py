import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dicionário agrupando as variantes dos nomes
fabricantes = {
    "ASTRAZENECA": ["ASTRAZENECA", "ASTRAZENECA AB", "ASTRAZENECA/FIOCRUZ", "ASTRAZENECA/OXFORD", "AstraZeneca/Oxford", "Oxford-AstraZeneca", "University of Oxford/AstraZeneca"],
    "BIONTECH": ["BIONTECH", "BioNTech/Fosun Pharma/Pfizer", "Pfizer/BioNTech", "PFIZER/BIONTECH"],
    "BUTANTAN": ["Butantan/Sinovac", "FUNDACAO BUTANTAN", "INSTITUTO BUTANTAN", "SINOVAC/BUTANTAN"],
    "JANSSEN": ["JANSSEN", "JANSSEN-CILAG", "JOHNSON & JOHNSON/JANSSEN", "Janssen", "Janssen Biologics B.V.", "Janssen-Cilag"],
    "PFIZER": ["PFIZER", "PFIZER - PEDIÁTRICA", "PFIZER - PEDIÁTRICA MENOR DE 5 ANOS", "PFIZER MANUFACTURING BELGIUM NV - BELGICA", "PFIZER MANUFACTURING BELGIUM NV - BELGIVA", "PFIZER MANUFACTURING BELGIUM NV BELGIVA", "Pfizer"],
    "SINOVAC": ["SINOVAC", "SINOVAC LIFE SCIENCE CO LTD", "Sinovac"],
    "OUTROS": ["Pendente Identificação", "WYETH PHARMACEUTICALS", "SERUM INSTITUTE OF INDIA LTD", "SERUM INSTITUTE OF INDIA LTD."]
}

# Carregar o dataset
dataset = pd.read_csv('../../data/resultado.csv', sep=';', quotechar='"', low_memory=False)

# Exibir os nomes das colunas
print("Nomes das colunas no dataset:")
print(dataset.columns.tolist())

# Limpar os valores das colunas de laboratório (remover espaços)
dataset['codigoLaboratorioSegundaDose'] = dataset['codigoLaboratorioSegundaDose'].str.strip()
dataset['codigoLaboratorioPrimeiraDose'] = dataset['codigoLaboratorioPrimeiraDose'].str.strip()

# Função para mapear o nome do laboratório para o dicionário de fabricantes
def mapear_fabricante(laboratorio):
    for chave, variantes in fabricantes.items():
        if laboratorio in variantes:
            return chave
    return "OUTROS"  # Caso o nome não seja reconhecido, marcar como "OUTROS"

# Aplicar o mapeamento aos dados de laboratório
dataset['codigoLaboratorioPrimeiraDose'] = dataset['codigoLaboratorioPrimeiraDose'].apply(mapear_fabricante)
dataset['codigoLaboratorioSegundaDose'] = dataset['codigoLaboratorioSegundaDose'].apply(mapear_fabricante)

# Contar vacinas aplicadas por laboratório (primeira dose)
vacinas_primeira_dose = dataset['codigoLaboratorioPrimeiraDose'].value_counts().reset_index()
vacinas_primeira_dose.columns = ['Laboratório', 'Total Primeira Dose']

# Contar vacinas aplicadas por laboratório (segunda dose)
vacinas_segunda_dose = dataset['codigoLaboratorioSegundaDose'].value_counts().reset_index()
vacinas_segunda_dose.columns = ['Laboratório', 'Total Segunda Dose']

# Unir as duas contagens em um único DataFrame
vacinas_total = pd.merge(vacinas_primeira_dose, vacinas_segunda_dose, on='Laboratório', how='outer').fillna(0)

# Filtrar apenas os laboratórios mapeados (excluindo "OUTROS" e valores inválidos)
vacinas_total = vacinas_total[vacinas_total['Laboratório'] != "OUTROS"]

# Calcular o total de vacinas aplicadas por laboratório
vacinas_total['Total'] = vacinas_total['Total Primeira Dose'] + vacinas_total['Total Segunda Dose']

# Converter os totais para numéricos (se necessário)
vacinas_total['Total Primeira Dose'] = pd.to_numeric(vacinas_total['Total Primeira Dose'], errors='coerce')
vacinas_total['Total Segunda Dose'] = pd.to_numeric(vacinas_total['Total Segunda Dose'], errors='coerce')
vacinas_total['Total'] = pd.to_numeric(vacinas_total['Total'], errors='coerce')

# Exibir os resultados
print("\nVolumetria das vacinas aplicadas por laboratório:")
print(vacinas_total)

# Visualizações gráficas

# Gráfico separado para Primeira Dose, Segunda Dose e Total
plt.figure(figsize=(14, 7))

# Gráfico de barras para total de vacinas aplicadas por laboratório
vacinas_total.plot(x='Laboratório', y=['Total Primeira Dose', 'Total Segunda Dose'], kind='bar', figsize=(14, 7), color=['lightblue', 'lightgreen'])
plt.title('Vacinas Aplicadas por Laboratório (Primeira e Segunda Dose)')
plt.xlabel('Laboratório')
plt.ylabel('Número de Vacinas Aplicadas')
plt.xticks(rotation=45)
plt.legend(title='Tipo de Dose')
plt.tight_layout()

# Exibir o gráfico
plt.show()

# Gráfico de barras para o total de vacinas aplicadas (soma de todas as doses)
plt.figure(figsize=(14, 7))
sns.barplot(x='Laboratório', y='Total', data=vacinas_total, palette='viridis', legend=False)
plt.title('Total de Vacinas Aplicadas por Laboratório')
plt.xlabel('Laboratório')
plt.ylabel('Total de Vacinas Aplicadas')
plt.xticks(rotation=45)
plt.tight_layout()

# Exibir o gráfico
plt.show()
