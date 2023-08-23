import streamlit as st

# Página 1
def page_one():
    st.title("Página 1")
    st.write("Bem-vindo à página 1!")

# Página 2
def page_two():
    st.title("Página 2")
    st.write("Bem-vindo à página 2!")

# Sidebar para seleção de página
sidebar_selection = st.sidebar.selectbox("Selecione uma página", ("Página 1", "Página 2"))

# Exibição da página selecionada
if sidebar_selection == "Página 1":
    page_one()
else:
    page_two()
