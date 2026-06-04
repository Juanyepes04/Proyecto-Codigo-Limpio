def test_listar_clientes(client):
    response = client.get("/clientes")

    assert response.status_code == 200


def test_cliente_inexistente(client):
    response = client.get("/clientes/99999")

    assert response.status_code == 200
    assert "error" in response.json()


def test_endpoint_clientes_devuelve_lista(client):
    response = client.get("/clientes")

    assert isinstance(response.json(), list)