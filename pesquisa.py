import pandas as pd

# Ajuste o caminho para onde seu arquivo CSV está localizado
arquivo_csv = "saida/resultado.csv"

# Carregar o arquivo CSV
df = pd.read_csv(arquivo_csv, delimiter=";", quotechar='"')

# Contar o número de ocorrências distintas em uma coluna
result = df['estadoNotificacaoIBGE'].value_counts()

# Exibir o resultado
print(result)
