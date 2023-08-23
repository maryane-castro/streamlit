import streamlit as st
import cv2
import numpy as np
from PIL import Image
from paddleocr import PaddleOCR

# Inicializa o PaddleOCR
ocr = PaddleOCR()

# Página 1
def page_one():
    st.title("Página 1")
    st.write("Bem-vindo à página 1!")
    uploaded_image = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

    # Verifica se uma imagem foi carregada
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        image = np.array(image)  # Converta a imagem PIL para uma matriz NumPy
        
        # Converte a imagem para escala de cinza
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        # Exibe a imagem em preto e branco
        st.image(grayscale_image, caption='Imagem em Preto e Branco', use_column_width=True)
        
        # Realiza a detecção de texto usando o PaddleOCR
        results = ocr.ocr(grayscale_image)

        # Exibe o texto detectado
        st.write("Texto Detectado:")
        for result in results[0]:
            text = result[1][0]
            st.write(text)

def page_two():
    st.title("Página 2")
    st.write("Bem-vindo à página 2!")

# Cria um menu para alternar entre as páginas
menu = ["Página 1", "Página 2"]
choice = st.sidebar.selectbox("Selecione uma Página", menu)

if choice == "Página 1":
    page_one()
else:
    page_two()




















#main da vida
sidebar_selection = st.sidebar.selectbox("Selecione uma página", ("Página 1", "Página 2"))
if sidebar_selection == "Página 1":
    page_one()
else:
    page_two()
