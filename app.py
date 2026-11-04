import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Aula Virtual - Contabilidad General", layout="wide")

# Buscar cualquier archivo HTML presente en el repositorio
html_file = None
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            html_file = os.path.join(root, file)
            break
    if html_file:
        break

if html_file:
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Renderizar el aula virtual en pantalla completa
    components.html(html_content, height=1200, scrolling=True)
else:
    st.error("⚠️ No se encontró ningún archivo .html en el repositorio de GitHub. Por favor, asegúrate de subir tu archivo HTML al repositorio.")