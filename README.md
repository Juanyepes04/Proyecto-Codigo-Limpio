# 🚗 RentaCar

## Integrantes

* Juan Diego Yepes Valencia
* Jhon Lizarazo
* Jhon Garavito

---

# Descripción del Proyecto

RentaCar es un sistema de gestión de alquiler de vehículos desarrollado bajo una arquitectura cliente-servidor utilizando FastAPI para el backend, Streamlit para el frontend y Supabase (PostgreSQL) como sistema de almacenamiento de datos.

El sistema permite administrar clientes, vehículos y alquileres de manera centralizada, facilitando el control de disponibilidad de vehículos y el seguimiento de las operaciones de alquiler.

---

# Objetivos

* Gestionar clientes registrados.
* Gestionar vehículos disponibles para alquiler.
* Registrar y controlar alquileres.
* Validar reglas de negocio para garantizar la integridad de la información.
* Implementar una arquitectura organizada y escalable.

---

# Tecnologías Utilizadas

## Backend

* Python 3.12
* FastAPI
* Pydantic

## Frontend

* Streamlit
* Pandas
* Requests

## Base de Datos

* Supabase
* PostgreSQL

## Testing

* Pytest

## Documentación

* MkDocs

---

# Arquitectura del Proyecto

El proyecto está organizado en capas para separar responsabilidades:

```text
src
│
├── api
│   ├── main.py
│   └── routers
│
├── app
│   ├── main.py
│   └── pages
│
├── schemas
│
├── services
│
└── storage
```

### API

Contiene los endpoints REST desarrollados con FastAPI.

### App

Contiene la interfaz gráfica desarrollada con Streamlit.

### Schemas

Modelos de validación implementados con Pydantic.

### Services

Capa destinada a la lógica de negocio.

### Storage

Gestiona la conexión con Supabase.

---

# Modelo de Datos

El sistema está compuesto por tres entidades principales:

## Cliente

* id
* nombre
* telefono
* email
* activo

## Vehículo

* id
* marca
* modelo
* anio
* color
* placa
* disponible
* precio_por_dia

## Alquiler

* id
* cliente_id
* vehiculo_id
* fecha_inicio
* fecha_fin
* total
* activo

Relaciones:

* Un cliente puede tener varios alquileres.
* Un vehículo puede participar en varios alquileres.
* Un alquiler pertenece a un único cliente y a un único vehículo.

---

# Funcionalidades

## Gestión de Clientes

* Crear cliente.
* Consultar clientes.
* Actualizar cliente.
* Eliminar cliente.

## Gestión de Vehículos

* Crear vehículo.
* Consultar vehículos.
* Consultar vehículos disponibles.
* Actualizar vehículo.
* Eliminar vehículo.

## Gestión de Alquileres

* Crear alquiler.
* Consultar alquileres.
* Actualizar alquiler.
* Eliminar alquiler.
* Cálculo automático del valor total del alquiler.

---

# Reglas de Negocio

El sistema implementa las siguientes validaciones:

* El cliente debe existir para registrar un alquiler.
* El vehículo debe existir para registrar un alquiler.
* El vehículo debe estar disponible.
* La fecha final no puede ser menor que la fecha inicial.
* Al eliminar un alquiler, el vehículo vuelve a estar disponible.
* El valor total del alquiler se calcula automáticamente según los días de alquiler y el precio por día del vehículo.

---

# Instalación

## Clonar el repositorio

```bash
git clone https://github.com/Juanyepes04/Proyecto-Codigo-Limpio.git
cd Proyecto-Codigo-Limpio
```

## Crear entorno virtual

```bash
python -m venv .venv
```

## Activar entorno virtual

Linux / WSL:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Variables de Entorno

Configurar las credenciales de Supabase:

```env
SUPABASE_URL=tu_url
SUPABASE_KEY=tu_key
```

---

# Ejecución del Backend

```bash
uvicorn src.api.main:app --reload
```

Documentación Swagger:

```text
http://127.0.0.1:8000/docs
```

Documentación ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# Ejecución del Frontend

```bash
streamlit run src/app/main.py
```

---

# Pruebas

Ejecutar pruebas automáticas:

```bash
pytest
```

---

# Resultados Esperados

El sistema permite administrar integralmente el proceso de alquiler de vehículos mediante una interfaz web intuitiva conectada a una API REST y respaldada por una base de datos PostgreSQL en Supabase.
