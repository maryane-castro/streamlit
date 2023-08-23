import streamlit as st
import cv2
import numpy as np
from PIL import Image
from paddleocr import PaddleOCR

# Inicializa o PaddleOCR
ocr = PaddleOCR()

# Função para desenhar caixas na imagem
def draw_boxes_on_image(image, results):
    img_with_boxes = image.copy()
    for result in results[0]:
        text = result[1][0]
        points = result[0]
        
        # Converter pontos para tuplas de números inteiros
        points = [(int(p[0]), int(p[1])) for p in points]

        # Desenha a caixa delimitadora
        for i in range(4):
            cv2.line(img_with_boxes, points[i], points[(i+1) % 4], (0, 255, 0), 2)
        
        # Escreve o texto detectado próximo à caixa
        #cv2.putText(img_with_boxes, text, points[0], cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    return img_with_boxes


# Página 1
def page_one():
    st.title("Página 1")
    st.write("Bem-vindo à página 1!")
    uploaded_image = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

    # Verifica se uma imagem foi carregada
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        image = np.array(image)  # Converta a imagem PIL para uma matriz NumPy
        
        # Realiza a detecção de texto usando o PaddleOCR
        results = ocr.ocr(image)

        # Desenha as caixas na imagem
        image_with_boxes = draw_boxes_on_image(image, results)

        # Exibe a imagem com as caixas desenhadas
        st.image(image_with_boxes, caption='Imagem com Caixas Delimitadoras', use_column_width=True)

def page_two():
    st.title("Página 2")
    st.write("Bem-vindo à página 2!")

# Main
sidebar_selection = st.sidebar.selectbox("Selecione uma página", ("Página 1", "Página 2"))
if sidebar_selection == "Página 1":
    page_one()
else:
    page_two()
