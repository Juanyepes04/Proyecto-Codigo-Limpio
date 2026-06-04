import streamlit as st
import requests
from datetime import date

API_URL = "http://127.0.0.1:8000"

st.title("📄 Gestión de Alquileres")

# ==========================
# CARGAR DATOS
# ==========================

clientes = requests.get(
    f"{API_URL}/clientes"
).json()

vehiculos = requests.get(
    f"{API_URL}/vehiculos/disponibles"
).json()

# ==========================
# CREAR ALQUILER
# ==========================

st.header("➕ Crear Alquiler")

if clientes and vehiculos:

    clientes_dict = {
        f"{c['nombre']} (ID {c['id']})": c["id"]
        for c in clientes
    }

    vehiculos_dict = {
        f"{v['marca']} {v['modelo']} - {v['placa']}": v
        for v in vehiculos
    }

    with st.form("crear_alquiler"):

        cliente_seleccionado = st.selectbox(
            "Cliente",
            list(clientes_dict.keys())
        )

        vehiculo_seleccionado = st.selectbox(
            "Vehículo",
            list(vehiculos_dict.keys())
        )

        fecha_inicio = st.date_input(
            "Fecha inicio",
            value=date.today()
        )

        fecha_fin = st.date_input(
            "Fecha fin",
            value=date.today()
        )

        enviar = st.form_submit_button(
            "Crear Alquiler"
        )

        if enviar:

            response = requests.post(
                f"{API_URL}/alquileres",
                json={
                    "cliente_id":
                    clientes_dict[cliente_seleccionado],

                    "vehiculo_id":
                    vehiculos_dict[
                        vehiculo_seleccionado
                    ]["id"],

                    "fecha_inicio":
                    str(fecha_inicio),

                    "fecha_fin":
                    str(fecha_fin)
                }
            )

            if response.status_code == 200:

                data = response.json()

                if "error" in data:
                    st.error(data["error"])
                else:
                    st.success(
                        "Alquiler creado correctamente"
                    )

                    st.success(
                        f"💰 Total: ${data['total_calculado']:,.0f}"
                    )

                    st.rerun()

            else:
                st.error(
                    "Error al crear alquiler"
                )

else:

    st.warning(
        "Debe existir al menos un cliente y un vehículo disponible."
    )

st.divider()

st.header("📊 Resumen de Alquileres")

alquileres_response = requests.get(
    f"{API_URL}/alquileres"
)

if alquileres_response.status_code == 200:

    alquileres = alquileres_response.json()

    total_alquileres = len(alquileres)

    ingresos = sum(
    a.get("total") or 0
    for a in alquileres
    )

    vehiculos_ocupados = sum(
        1 for v in requests.get(
            f"{API_URL}/vehiculos"
        ).json()
        if not v["disponible"]
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Alquileres",
            total_alquileres
        )

    with col2:
        st.metric(
            "Ingresos",
            f"${ingresos:,.0f}"
        )

    with col3:
        st.metric(
            "Vehículos Ocupados",
            vehiculos_ocupados
        )

st.divider()

st.header("📋 Historial de Alquileres")

if alquileres:

    clientes_map = {
        c["id"]: c["nombre"]
        for c in clientes
    }

    todos_vehiculos = requests.get(
        f"{API_URL}/vehiculos"
    ).json()

    vehiculos_map = {
        v["id"]:
        f"{v['marca']} {v['modelo']}"
        for v in todos_vehiculos
    }

    for alquiler in alquileres:

        with st.container():

            cliente_nombre = clientes_map.get(
                alquiler["cliente_id"],
                "Desconocido"
            )

            vehiculo_nombre = vehiculos_map.get(
                alquiler["vehiculo_id"],
                "Desconocido"
            )

            col1, col2 = st.columns([4, 1])

            with col1:

                st.subheader(
                    f"📄 Alquiler #{alquiler['id']}"
                )

                st.write(
                    f"👤 Cliente: {cliente_nombre}"
                )

                st.write(
                    f"🚗 Vehículo: {vehiculo_nombre}"
                )

                st.write(
                    f"📅 Inicio: {alquiler['fecha_inicio']}"
                )

                st.write(
                    f"📅 Fin: {alquiler['fecha_fin']}"
                )

                total = alquiler.get("total") or 0

                st.write(f"💰 Total: ${total:,.0f}")

            with col2:

                if st.button(
                    f"Eliminar {alquiler['id']}"
                ):

                    requests.delete(
                        f"{API_URL}/alquileres/{alquiler['id']}"
                    )

                    st.success(
                        "Alquiler eliminado"
                    )

                    st.rerun()

            st.divider()