import streamlit as st
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import requests

st.set_page_config(page_title="Brasileirão",page_icon="⚽",layout="wide")

# Exibindo a imagem na sidebar
st.sidebar.image('https://logodownload.org/wp-content/uploads/2017/11/cbf-logo-selecao-logo-brasil.png', width=80)

# Navegação entre páginas
st.sidebar.title("Campeonato Brasileiro")
st.sidebar.write("Confira as principais informações do campeonato Brasileiro entre os anos de 2013 e 2023")


# Lê o CSV em um DataFrame
df = pd.read_csv('datasets/db.csv')

# Filtra o DataFrame para o último campeão
df_ultimo_campeao = df[(df['Ano'] == 2023) & (df['Posição'] == 1)]

# Obtém o nome do time do último campeão (primeira linha correspondente)
nome_time = df_ultimo_campeao['Time'].iloc[0] if not df_ultimo_campeao.empty else "Nenhum campeão encontrado"
# Pontos
pontos_time = df_ultimo_campeao['Pontos'].iloc[0] if not df_ultimo_campeao.empty else "Nenhum campeão encontrado"
# Vitorias
vitorias_time = df_ultimo_campeao['Vitórias'].iloc[0] if not df_ultimo_campeao.empty else "Nenhum campeão encontrado"
# Gols
gols_time = df_ultimo_campeao['Gols Pró'].iloc[0] if not df_ultimo_campeao.empty else "Nenhum campeão encontrado"

# Cria colunas e exibe a mensagem de sucesso
a, b, c, d = st.columns(4)
a.success(f"Ultimo campeão: {nome_time}")
b.info(f"Total de pontos: {pontos_time}")
c.warning(f"Vitórias: {vitorias_time}")
d.error(f"Gols marcados: {gols_time}")

st.divider()

# Recebe o intervalo de anos do usuário por meio de um seletor
start_, end_ = st.sidebar.select_slider(
    "Selecione o período:",
    options=sorted(df['Ano'].unique()),  # Garante que os anos estejam ordenados
    value=(min(df['Ano']), max(df['Ano']))  # Define o intervalo inicial como o mínimo e máximo
)

# Garante que a coluna 'Ano' está formatada como inteiro
df['Ano'] = df['Ano'].astype(int)

# Filtra os dados para o intervalo de anos selecionado
colocados = df[(df['Ano'] >= start_) & (df['Ano'] <= end_)  # Filtra pelos anos dentro do intervalo
][df['Posição']==1][['Ano','Posição', 'Time', 'Vitórias', 'Empates', 'Derrotas', 'Pontos']].sort_values('Ano', ascending=False)

# Exibe os dados filtrados
st.title('Resultados:')
st.dataframe(colocados, hide_index=True)


st.divider()

st.write("Para saber mais da participação do seu time do coração, selecione-o abaixo:")


df_select = df[(df['Ano'] >= start_) & (df['Ano'] <= end_)  # Filtra pelos anos dentro do intervalo
]
# Adiciona uma opção padrão para o selectbox
option = st.selectbox(
    "Selecione um time",
    options=["Selecione um time"] + sorted(df_select['Time'].unique()),  # Adiciona a opção inicial
    index=0
)

# Aplica o filtro somente se um time válido for selecionado
if option != "Selecione um time":
    time_escolhido = df_select[df_select['Time'] == option]
    # Exibe o time selecionado
    st.dataframe(time_escolhido, hide_index=True)
else:
    st.info("Por favor, selecione um time para exibir os resultados.")

st.sidebar.divider()

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


csv = convert_df(df)

st.sidebar.download_button(
   "Download da base",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)