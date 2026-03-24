import streamlit as st
import pandas as pd
import numpy as np

# 1. Configuración de la pestaña del navegador
st.set_page_config(page_title="Ciencia del Umbral", page_icon="🧠", layout="wide")

# 2. Título y Estética (Tu marca personal)
st.title("🧠 Ciencia del Umbral")
st.markdown("### *Explorando People Analytics y Neurociencia*")
st.write("---")

# 3. La Barra Lateral (Interactividad pura)
st.sidebar.header("Panel de Control")
nombre = st.sidebar.text_input("Introducí tu nombre", "Santi")
nivel_interés = st.sidebar.slider("Nivel de profundidad del análisis", 0, 100, 50)

# 4. Un saludo dinámico
st.write(f"¡Hola **{nombre}**! Bienvenido al dashboard de **Shanti Mind Data**.")
st.info(f"Estamos procesando datos con un nivel de detalle del {nivel_interés}%.")

# 5. Un gráfico de prueba para que veas la potencia
st.subheader("Simulación de Niveles Neuroquímicos")
datos_dummy = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Dopamina', 'Serotonina', 'Oxitocina']
)

st.line_chart(datos_dummy)

st.write("---")
st.caption("Desarrollado por Shanti Mind Data - 2024")


