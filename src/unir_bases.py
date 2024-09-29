import pandas as pd
import os

# Definir o diretório onde os arquivos CSV estão localizados
diretorio_entrada = '.'  # Diretório onde os arquivos CSV estão localizados
diretorio_saida = 'saida'  # Diretório onde o arquivo combinado será salvo

# Crie o diretório de saída se ele não existir
if not os.path.exists(diretorio_saida):
    os.makedirs(diretorio_saida)

# Lista para armazenar os DataFrames
lista_df = []

# Percorra todos os arquivos no diretório de entrada
for arquivo in os.listdir(diretorio_entrada):
    if arquivo.endswith('.csv'):
        # Cria o caminho completo para o arquivo
        caminho_arquivo = os.path.join(diretorio_entrada, arquivo)
        
        # Leia o arquivo CSV e adicione à lista de DataFrames
        df = pd.read_csv(caminho_arquivo, delimiter=';', quotechar='"')
        lista_df.append(df)

# Combine todos os DataFrames
df_combined = pd.concat(lista_df, ignore_index=True)

# Defina o nome do arquivo de saída
arquivo_saida = os.path.join(diretorio_saida, 'resultado.csv')

# Salve o DataFrame combinado em um novo arquivo CSV
df_combined.to_csv(arquivo_saida, index=False, sep=';', quotechar='"')

print(f'Arquivo combinado salvo como {arquivo_saida}')
