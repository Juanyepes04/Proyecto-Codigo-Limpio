def test_listar_alquileres(client):
    response = client.get("/alquileres")

    assert response.status_code == 200


def test_alquiler_inexistente(client):
    response = client.get("/alquileres/99999")

    assert response.status_code == 200
    assert "error" in response.json()


def test_endpoint_alquileres_devuelve_lista(client):
    response = client.get("/alquileres")

    assert isinstance(response.json(), list)


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "mensaje" in response.json()


def test_swagger_disponible(client):
    response = client.get("/docs")

    assert response.status_code == 200


def test_redoc_disponible(client):
    response = client.get("/redoc")

    assert response.status_code == 200