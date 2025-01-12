import streamlit as st
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import requests
import zipfile

# Configurações do arquivo de autenticação
kaggle_username = ""  # Substitua pelo seu username
kaggle_key = ""  # Substitua pela sua API Key

# Informações do dataset
# O slug deve conter o proprietário e o nome do dataset. Ex.: "andrehrsilva/brasileiro-2024-srie-a-dataset"
dataset_slug = "victorhts/brasileiro-srie-a-resultados-2013-2023"
output_dir = "./datasets"  # Diretório para salvar o dataset

# Endpoint da API
url = f"https://www.kaggle.com/api/v1/datasets/download/{dataset_slug}"

# Cabeçalhos de autenticação para a API da Kaggle
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {kaggle_key}"
}

# Requisição para baixar o dataset
response = requests.get(url, headers=headers, stream=True)

# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{dataset_slug.replace('/', '_')}.zip")
    with open(output_file, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Dataset baixado com sucesso em: {output_file}")



# Exibindo a imagem na sidebar
st.sidebar.image('https://logodownload.org/wp-content/uploads/2017/11/cbf-logo-selecao-logo-brasil.png', width=100)

# Navegação entre páginas
page = st.sidebar.selectbox("Escolha uma página:", ["Home", "Football"])

# Conteúdo para cada página
if page == "Home":
    st.title("Página Inicial")
    st.write("Bem-vindo à página inicial do Campeonato Brasileiro!")
elif page == "Football":
    st.title("Futebol")
    st.write("Aqui está a página de Futebol!")
    # Caminho para o arquivo CSV
    caminho_csv = os.path.join(output_dir, "Brasileiro 2024 (Srie A) - Dataset.csv")

    # Lê o CSV em um DataFrame
    df = pd.read_csv(caminho_csv)
    st.dataframe(df)
    # Exibe as 5 primeiras linhas
    print(df.head())


        

