#http://localhost:8501/

import streamlit as st
import cv2
import numpy as np
from PIL import Image
from paddleocr import PaddleOCR

# Inicializa o PaddleOCR
ocr = PaddleOCR()

# Função para desenhar caixas na imagem
def draw_boxes_on_image_pdi(image, results):
    img_with_boxes = image.copy()
    for result in results[0]:
        text = result[1][0]
        points = result[0]
        
        points = [(int(p[0]), int(p[1])) for p in points]

        for i in range(4):
            cv2.line(img_with_boxes, points[i], points[(i+1) % 4], (0, 255, 0), 2)
        

        #cv2.putText(img_with_boxes, text, points[0], cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return img_with_boxes




def draw_boxes_on_image_nlp(image, results):
    img_with_boxes = image.copy()
    for result in results[0]:
        text = result[1][0]
        points = result[0]
        
        points = [(int(p[0]), int(p[1])) for p in points]

        #for i in range(4):
        #    cv2.line(img_with_boxes, points[i], points[(i+1) % 4], (0, 255, 0), 2)
        

        cv2.putText(img_with_boxes, text, points[0], cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    return img_with_boxes


def pag1():
    st.title("PDI")
    uploaded_image = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        with st.spinner('Detectando bounding box...'):
            image = Image.open(uploaded_image)
            image = np.array(image)  # converte a imagem PIL para uma matriz NumPy
            
            results = ocr.ocr(image)

            image_with_boxes = draw_boxes_on_image_pdi(image, results)

            st.image(image_with_boxes, caption='Imagem com Caixas Delimitadoras', use_column_width=True)

def pag2():
    st.title("NLP")
    uploaded_image = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        with st.spinner('Detectando texto...'):
            image = Image.open(uploaded_image)
            image = np.array(image)  # converte a imagem PIL para uma matriz NumPy
            
            results = ocr.ocr(image)

            image_with_boxes = draw_boxes_on_image_nlp(image, results)

            st.image(image_with_boxes, caption='Imagem com Caixas Delimitadoras', use_column_width=True)




# main da vida
sidebar_selection = st.sidebar.selectbox("Selecione uma opção", ("PDI", "NLP"))
if sidebar_selection == "PDI":
    pag1()
else:
    pag2()
