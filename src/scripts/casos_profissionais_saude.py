# Quantidade de profissionais da área da saúde
import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV que está na mesma pasta
df = pd.read_csv('../../data/resultado.csv', delimiter=';')

# Filtra os casos em que 'profissionalSaude' é igual a 'Sim'
saude_df = df[df['profissionalSaude'] == 'Sim']

# Remover o número e o hífen, mantendo apenas a descrição do CBO
saude_df['cbo_descricao'] = saude_df['cbo'].str.split(' - ').str[1]

# Conta a frequência de cada valor na coluna 'cbo_descricao'
frequencia_cbo = saude_df['cbo_descricao'].value_counts()

# Calcula o total de ocorrências
total_cbo = frequencia_cbo.sum()

# Calcula a porcentagem de cada CBO
porcentagem_cbo = (frequencia_cbo / total_cbo) * 100

# Cria um DataFrame com a quantidade e a porcentagem
resultado = pd.DataFrame({
    'Ocorrências': frequencia_cbo,
    'Porcentagem (%)': porcentagem_cbo
})

# Exibe o DataFrame no console
print(resultado)

# Seleciona as 5 áreas com maior ocorrência
top_5_cbo = frequencia_cbo.head(5)

# Plotando o gráfico de barras para as 5 maiores áreas de CBO (sem o número)
plt.figure(figsize=(10, 6))
top_5_cbo.plot(kind='bar', color='lightblue')

# Adiciona título e rótulos
plt.title('Top 5 Áreas de CBO para Profissionais da Saúde')
plt.xlabel('CBO')
plt.ylabel('Número de Ocorrências')

# Rotaciona os rótulos do eixo X para melhorar a leitura
plt.xticks(rotation=45, ha='right')

# Exibe o gráfico
plt.tight_layout()
plt.show()

print('total de profissionais da saude:')
print(total_cbo)

print(frequencia_cbo.describe())