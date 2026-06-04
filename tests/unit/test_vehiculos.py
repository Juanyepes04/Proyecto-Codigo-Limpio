def test_listar_vehiculos(client):
    response = client.get("/vehiculos")

    assert response.status_code == 200


def test_vehiculo_inexistente(client):
    response = client.get("/vehiculos/99999")

    assert response.status_code == 200
    assert "error" in response.json()


def test_endpoint_vehiculos_devuelve_lista(client):
    response = client.get("/vehiculos")

    assert isinstance(response.json(), list)