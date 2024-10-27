# Ocorrência de Sintomas em Casos de Óbito
import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV que está na mesma pasta
df = pd.read_csv('../../data/resultado.csv', delimiter=';')

# Conta quantas vezes 'Óbito' aparece na coluna 'evolucaoCaso'
obitos_count = df['evolucaoCaso'].value_counts().get('Óbito', 0)

# Exibe o resultado
print(f"Quantidade de ocorrências de 'Óbito': {obitos_count}")


# Filtra os casos em que 'evolucaoCaso' é igual a 'Óbito'
obito_df = df[df['evolucaoCaso'].str.contains('óbito|obito', case=False, na=False)]

# Combina todos os sintomas de todos os casos de óbito
sintomas_obito = obito_df['sintomas'].dropna().str.split(', ')

# Achata a lista de listas em uma única lista com todos os sintomas
todos_sintomas = [sintoma for sublist in sintomas_obito for sintoma in sublist]

# Conta a frequência de cada sintoma
frequencia_sintomas = pd.Series(todos_sintomas).value_counts()

# Calcula o total de sintomas
total_sintomas = frequencia_sintomas.sum()

# Calcula a porcentagem de cada sintoma
porcentagem_sintomas = (frequencia_sintomas / total_sintomas) * 100

# Cria um DataFrame para exibir tanto o número de ocorrências quanto a porcentagem
resultado = pd.DataFrame({
    'Ocorrências': frequencia_sintomas,
    'Porcentagem (%)': porcentagem_sintomas
})

# Exibe a tabela de resultados no console
print(resultado)

# Plotando o gráfico de barras
plt.figure(figsize=(10, 6))
resultado['Ocorrências'].plot(kind='bar', color='skyblue')

# Adiciona título e rótulos
plt.title('Ocorrências de Sintomas em Casos de Óbito')
plt.xlabel('Sintomas')
plt.ylabel('Número de Ocorrências')

# Rotaciona os rótulos do eixo X para melhorar a leitura
plt.xticks(rotation=45, ha='right')

# Exibe o gráfico
plt.tight_layout()
plt.show()

