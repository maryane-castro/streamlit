import streamlit as st

# Página 1
def page_one():
    st.title("Página 1")
    st.write("Bem-vindo à página 1!")
    uploaded_image = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

# Verifica se uma imagem foi carregada
    if uploaded_image is not None:
        # Exibe a imagem carregada
        st.image(uploaded_image, caption='Imagem Carregada', use_column_width=True)



def page_two():
    st.title("Página 2")
    st.write("Bem-vindo à página 2!")



















#main da vida
sidebar_selection = st.sidebar.selectbox("Selecione uma página", ("Página 1", "Página 2"))
if sidebar_selection == "Página 1":
    page_one()
else:
    page_two()
