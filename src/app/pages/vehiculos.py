import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Vehículos")

# ==================================
# CREAR VEHÍCULO
# ==================================

st.header("Crear Vehículo")

with st.form("crear_vehiculo"):

    marca = st.text_input("Marca")
    modelo = st.text_input("Modelo")
    anio = st.number_input("Año", step=1)
    color = st.text_input("Color")
    placa = st.text_input("Placa")
    precio_por_dia = st.number_input("Precio por día")

    submitted = st.form_submit_button("Crear Vehículo")

    if submitted:

        response = requests.post(
            f"{API_URL}/vehiculos",
            json={
                "marca": marca,
                "modelo": modelo,
                "anio": anio,
                "color": color,
                "placa": placa,
                "precio_por_dia": precio_por_dia
            }
        )

        if response.status_code in [200, 201]:
            st.success("Vehículo creado correctamente")
        else:
            st.error(response.text)


# ==================================
# LISTAR VEHÍCULOS
# ==================================

st.header("🚗 Lista de Vehículos")

response = requests.get(f"{API_URL}/vehiculos")

if response.status_code == 200:

    vehiculos = response.json()

    if vehiculos:

        total = len(vehiculos)

        disponibles = sum(
            1 for v in vehiculos
            if v["disponible"]
        )

        ocupados = total - disponibles

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Vehículos",
                total
            )

        with col2:
            st.metric(
                "Disponibles",
                disponibles
            )

        with col3:
            st.metric(
                "Ocupados",
                ocupados
            )

        st.divider()

        busqueda = st.text_input(
            "🔍 Buscar por marca, modelo o placa"
        )

        if busqueda:

            vehiculos_filtrados = [

                v for v in vehiculos

                if busqueda.lower() in v["marca"].lower()

                or busqueda.lower() in v["modelo"].lower()

                or busqueda.lower() in v["placa"].lower()
            ]

        else:

            vehiculos_filtrados = vehiculos

        for vehiculo in vehiculos_filtrados:

            estado = "🟢 Disponible"

            if not vehiculo["disponible"]:
                estado = "🔴 Ocupado"

            with st.container():

                col1, col2 = st.columns([4, 1])

                with col1:

                    st.markdown(
                        f"""
                        ### 🚗 {vehiculo['marca']} {vehiculo['modelo']}
                        """
                    )

                    st.write(
                        f"🚘 Placa: {vehiculo['placa']}"
                    )

                    st.write(
                        f"🎨 Color: {vehiculo['color']}"
                    )

                    st.write(
                        f"📅 Año: {vehiculo['anio']}"
                    )

                    st.write(
                        f"💰 Precio por día: ${vehiculo['precio_por_dia']:,.0f}"
                    )

                    st.write(estado)

                with col2:

                    if st.button(
                        f"Eliminar {vehiculo['id']}"
                    ):

                        requests.delete(
                            f"{API_URL}/vehiculos/{vehiculo['id']}"
                        )

                        st.success(
                            "Vehículo eliminado"
                        )

                        st.rerun()

                st.divider()

    else:
        st.info(
            "No existen vehículos registrados"
        )

else:
    st.error(
        "Error al cargar vehículos"
    )