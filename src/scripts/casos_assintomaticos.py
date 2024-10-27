# Casos Assintomáticos por sexo, Raça/Cor e idade

import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV que está na mesma pasta
df = pd.read_csv('../../data/resultado.csv', delimiter=';')

# Filtra os casos assintomáticos (onde o campo 'sintomas' contém 'Assintomático')
assintomaticos_df = df[df['sintomas'].str.contains('Assintomático', case=False, na=False)]

# Analisando a distribuição de assintomáticos por sexo
frequencia_sexo = assintomaticos_df['sexo'].value_counts()

# Analisando a distribuição de assintomáticos por raça/cor
frequencia_raca = assintomaticos_df['racaCor'].value_counts()

# Analisando a distribuição de assintomáticos por faixa etária
# (Para análise mais detalhada, vamos definir faixas etárias)
bins = [0, 18, 30, 40, 50, 60, 70, 100]  # Faixas de idade
labels = ['0-18', '19-30', '31-40', '41-50', '51-60', '61-70', '71+']
assintomaticos_df['faixa_etaria'] = pd.cut(assintomaticos_df['idade'], bins=bins, labels=labels)
frequencia_idade = assintomaticos_df['faixa_etaria'].value_counts()

# Exibindo os resultados
print("Frequência de Casos Assintomáticos por Sexo:")
print(frequencia_sexo)
print("\nFrequência de Casos Assintomáticos por Raça/Cor:")
print(frequencia_raca)
print("\nFrequência de Casos Assintomáticos por Faixa Etária:")
print(frequencia_idade)

# Gerando gráficos para visualização

# Gráfico de casos assintomáticos por sexo
plt.figure(figsize=(8, 6))
frequencia_sexo.plot(kind='bar', color='salmon')
plt.title('Casos Assintomáticos por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Número de Casos')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Gráfico de casos assintomáticos por raça/cor
plt.figure(figsize=(8, 6))
frequencia_raca.plot(kind='bar', color='lightblue')
plt.title('Casos Assintomáticos por Raça/Cor')
plt.xlabel('Raça/Cor')
plt.ylabel('Número de Casos')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Gráfico de casos assintomáticos por faixa etária
plt.figure(figsize=(8, 6))
frequencia_idade.plot(kind='bar', color='lightgreen')
plt.title('Casos Assintomáticos por Faixa Etária')
plt.xlabel('Faixa Etária')
plt.ylabel('Número de Casos')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()