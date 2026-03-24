import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de página
st.set_page_config(page_title="Ciencia del Umbral", layout="wide")

st.title("🧠 Ciencia del Umbral: Umbral de la Mente")
st.markdown("### Simulación de Sistemas Conscientes e Integración Contemplativa")

# Protocolos
with st.expander("Ver Protocolos de Investigación (TAPIC / PRAP)"):
    st.write("""
    **13.1.3 Protocolo TAPIC:** Terapia Asistida por Psicodélicos con Integración Contemplativa.
    - **Racionalidad:** Desacoplamiento de DMN y ventana de plasticidad.
    - **Integración:** 12 semanas para cristalizar insights.
    """)

# Gráfico de Sintergia
st.subheader("Gráfico de Sintergia (Coherencia Atencional)")
t = np.linspace(0, 500, 500)
syntergy = np.cumsum(np.random.randn(500) * 0.01) + 0.5
fig, ax = plt.subplots()
ax.plot(t, syntergy, label="Índice de Sintergia S(t)")
ax.axvline(x=100, color='r', linestyle='--', label='Inicio de Práctica')
ax.legend()
st.pyplot(fig)

st.sidebar.info("Santiago Schiavoni · 2026")


