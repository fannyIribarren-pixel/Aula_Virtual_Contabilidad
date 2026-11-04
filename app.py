import streamlit as st
import streamlit.components.v1 as components

# Configuración de página completa
st.set_page_config(page_title="Aula Virtual - Contabilidad", layout="wide")

# Leer el archivo HTML
with open("Aula_Virtual_Contabilidad.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Mostrar el contenido HTML en la aplicación Streamlit
components.html(html_content, height=1000, scrolling=True)