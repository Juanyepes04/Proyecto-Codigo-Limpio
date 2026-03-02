import typer
from rich.console import Console
from rich.table import Table

from mi_app.storage import VehiculoStorage, ClienteStorage, AlquilerStorage
from mi_app.services import VehiculoService, ClienteService, AlquilerService
from mi_app.exceptions import RentSystemException

app = typer.Typer()
console = Console()

vehiculo_service = VehiculoService(VehiculoStorage())
cliente_service = ClienteService(ClienteStorage())
alquiler_service = AlquilerService(
    AlquilerStorage(),
    ClienteStorage(),
    VehiculoStorage(),
)


@app.command()
def crear_vehiculo(
    marca: str,
    modelo: str,
    año: int,
    color: str,
    placa: str,
    precio: float,
):
    """Crea un nuevo vehículo."""
    try:
        vehiculo = vehiculo_service.crear_vehiculo(
            marca, modelo, año, color, placa, precio
        )
        console.print("Vehículo creado correctamente", style="green")
        console.print(vehiculo)
    except RentSystemException as e:
        console.print(str(e), style="red")


@app.command()
def crear_cliente(nombre: str, telefono: str, email: str):
    """Crea un nuevo cliente."""
    try:
        cliente = cliente_service.crear_cliente(nombre, telefono, email)
        console.print("Cliente creado correctamente", style="green")
        console.print(cliente)
    except RentSystemException as e:
        console.print(str(e), style="red")


@app.command()
def listar_vehiculos():
    """Lista todos los vehículos."""
    vehiculos = vehiculo_service.storage.obtener_todos()

    table = Table(title="Vehículos")
    table.add_column("ID")
    table.add_column("Marca")
    table.add_column("Modelo")
    table.add_column("Disponible")

    for v in vehiculos:
        table.add_row(
            str(v.id),
            v.marca,
            v.modelo,
            "Sí" if v.disponible else "No",
        )

    console.print(table)


@app.command()
def alquilar(cliente_id: int, vehiculo_id: int):
    """Crea un alquiler."""
    try:
        alquiler = alquiler_service.crear_alquiler(cliente_id, vehiculo_id)
        console.print("Alquiler creado correctamente", style="green")
        console.print(alquiler)
    except RentSystemException as e:
        console.print(str(e), style="red")


@app.command()
def devolver(alquiler_id: int):
    """Devuelve un vehículo."""
    try:
        alquiler_service.devolver_vehiculo(alquiler_id)
        console.print("Vehículo devuelto correctamente", style="green")
    except RentSystemException as e:
        console.print(str(e), style="red")


if __name__ == "__main__":
    app()