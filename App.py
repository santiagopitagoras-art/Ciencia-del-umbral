import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Ciencia del Umbral", layout="wide")
st.title("🧠 Ciencia del Umbral: Umbral de la Mente")
st.markdown("### Simulación de Sistemas Conscientes e Integración Contemplativa")

# Gráfico de Sintergia
st.subheader("Gráfico de Sintergia (Coherencia Atencional)")
t = np.linspace(0, 500, 500)
syntergy = np.cumsum(np.random.randn(500) * 0.02) + 0.5
fig, ax = plt.subplots()
ax.plot(t, syntergy, label="Índice de Sintergia S(t)")
ax.axvline(x=150, color='r', linestyle='--', label='Punto de Inflexión')
ax.legend()
st.pyplot(fig)

st.sidebar.info("Santiago Schiavoni · Ciencia del Umbral 2026")
