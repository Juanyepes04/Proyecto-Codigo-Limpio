import json
import pytest
from pathlib import Path
from datetime import datetime

from mi_app.services import (
    VehiculoService,
    ClienteService,
    AlquilerService,
)
from mi_app.storage import (
    VehiculoStorage,
    ClienteStorage,
    AlquilerStorage,
)
from mi_app.exceptions import (
    ElementoNoEncontradoError,
    ClienteInactivoError,
    VehiculoNoDisponibleError,
    ClienteConAlquilerActivoError,
    AlquilerYaFinalizadoError,
)


@pytest.fixture
def setup_database(tmp_path):
    db_path = tmp_path / "database.json"

    initial_data = {
        "vehiculos": [],
        "clientes": [],
        "alquileres": [],
    }

    with open(db_path, "w") as f:
        json.dump(initial_data, f)

    # parcheamos la ruta global
    from mi_app import storage

    storage.DATABASE_PATH = db_path

    return db_path



def test_crear_vehiculo(setup_database):
    storage = VehiculoStorage()
    service = VehiculoService(storage)

    vehiculo = service.crear_vehiculo(
        "Toyota", "Corolla", 2020, "Blanco", "ABC123", 100.0
    )

    assert vehiculo.id == 1
    assert vehiculo.disponible is True



def test_crear_cliente(setup_database):
    storage = ClienteStorage()
    service = ClienteService(storage)

    cliente = service.crear_cliente(
        "Juan", "123456", "juan@test.com"
    )

    assert cliente.id == 1
    assert cliente.activo is True



def test_crear_alquiler_exitoso(setup_database):
    veh_storage = VehiculoStorage()
    cli_storage = ClienteStorage()
    alq_storage = AlquilerStorage()

    veh_service = VehiculoService(veh_storage)
    cli_service = ClienteService(cli_storage)
    alq_service = AlquilerService(
        alq_storage, cli_storage, veh_storage
    )

    cliente = cli_service.crear_cliente(
        "Juan", "123", "juan@test.com"
    )

    vehiculo = veh_service.crear_vehiculo(
        "Toyota", "Corolla", 2020, "Rojo", "XYZ123", 120
    )

    alquiler = alq_service.crear_alquiler(
        cliente.id, vehiculo.id
    )

    assert alquiler.activo is True


    