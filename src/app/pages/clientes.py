import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.title("👥 Gestión de Clientes")

tab1, tab2 = st.tabs([
    "➕ Registrar Cliente",
    "📋 Clientes Registrados"
])

# -------------------------
# REGISTRAR CLIENTE
# -------------------------

with tab1:

    st.subheader("Nuevo Cliente")

    with st.form("crear_cliente"):

        nombre = st.text_input("Nombre")
        telefono = st.text_input("Teléfono")
        email = st.text_input("Correo Electrónico")

        enviar = st.form_submit_button("Guardar Cliente")

        if enviar:

            data = {
                "nombre": nombre,
                "telefono": telefono,
                "email": email
            }

            response = requests.post(
                f"{API_URL}/clientes",
                json=data
            )

            if response.status_code == 200:
                st.success("Cliente creado correctamente")
            else:
                st.error("Error al crear cliente")

# -------------------------
# LISTAR CLIENTES
# -------------------------

with tab2:

    st.subheader("Listado de Clientes")

    response = requests.get(f"{API_URL}/clientes")

    if response.status_code == 200:

        clientes = response.json()

        if clientes:

            df = pd.DataFrame(clientes)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Total Clientes",
                    len(clientes)
                )

            with col2:
                activos = sum(
                    1 for c in clientes
                    if c["activo"]
                )

                st.metric(
                    "Clientes Activos",
                    activos
                )

            with col3:
                st.metric(
                    "Registros",
                    len(clientes)
                )

            st.divider()

            busqueda = st.text_input(
                "🔍 Buscar cliente"
            )

            if busqueda:

                clientes_filtrados = [
                    c for c in clientes
                    if busqueda.lower()
                    in c["nombre"].lower()
                ]

                df = pd.DataFrame(clientes_filtrados)

            else:

                df = pd.DataFrame(clientes)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            st.divider()

            st.subheader("🗑️ Eliminar Cliente")

            cliente_id = st.number_input(
                "ID del Cliente",
                min_value=1,
                step=1
            )

            if st.button("Eliminar Cliente"):

                response = requests.delete(
                    f"{API_URL}/clientes/{cliente_id}"
                )

                if response.status_code == 200:
                    st.success("Cliente eliminado")
                    st.rerun()
                else:
                    st.error("Error al eliminar")

        else:
            st.info("No existen clientes registrados")