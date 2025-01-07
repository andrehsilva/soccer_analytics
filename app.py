import streamlit as st

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
