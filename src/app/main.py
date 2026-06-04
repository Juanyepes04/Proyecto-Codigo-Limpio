import streamlit as st
import requests

st.set_page_config(
    page_title="RentaCar",
    page_icon="🚗",
    layout="wide"
)

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stMetric {
    background-color: #262730;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}

div[data-testid="stSidebar"] {
    background-color: #111827;
}

h1, h2, h3 {
    color: #2563eb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)

API_URL = "http://127.0.0.1:8000"

st.title("🚗 RentaCar")

st.caption(
    "Panel administrativo para la gestión de vehículos, clientes y alquileres"
)

st.divider()

st.markdown(
    """
    Bienvenido al panel administrativo del sistema de alquileres.
    """
)

try:
    vehiculos = requests.get(f"{API_URL}/vehiculos").json()
    clientes = requests.get(f"{API_URL}/clientes").json()
    alquileres = requests.get(f"{API_URL}/alquileres").json()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Vehículos Registrados",
            len(vehiculos)
        )

    with col2:
        st.metric(
            "Clientes Registrados",
            len(clientes)
        )

    with col3:
        st.metric(
            "Alquileres Totales",
            len(alquileres)
        )

except Exception:
    st.error("No fue posible conectar con la API")

st.divider()

st.subheader("📋 Módulos del Sistema")

c1, c2, c3 = st.columns(3)

with c1:
    st.info(
        """
        🚗 Vehículos

        Gestión completa de vehículos.
        """
    )

with c2:
    st.success(
        """
        👥 Clientes

        Administración de clientes.
        """
    )

with c3:
    st.warning(
        """
        📄 Alquileres

        Gestión de contratos de alquiler.
        """
    )