import pytest

# Tests para el controlador de productos


def test_get_products(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder obtener la lista de productos
    response = test_client.get("/api/taxis", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder crear un nuevo producto
    data = {
        "chofer": "Smartphone",
        "color": "red",
        "frec": True,
        "ingresos": 100.11,
    }
    response = test_client.post("/api/taxis", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["chofer"] == "Smartphone"
    assert response.json["color"] == "red"
    assert response.json["frec"] == True
    assert response.json["ingresos"] == 100.11


def test_get_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder obtener un producto específico
    # Este test asume que existe al menos un producto en la base de datos
    response = test_client.get("/api/taxis/1", headers=admin_auth_headers)
    assert response.status_code == 200
    assert "chofer" in response.json


def test_get_nonexistent_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar obtener un producto inexistente
    response = test_client.get("/api/taxis/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "taxi no encontrado"


def test_create_product_invalid_data(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar crear un producto sin datos requeridos
    data = {"chofer": "Laptop"}  # Falta description, price y stock
    response = test_client.post("/api/taxis", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"


def test_update_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder actualizar un producto existente
    data = {
        "chofer": "Smartphone",
        "color": "blue",
        "frec": True,
        "ingresos": 100.11,
    }
    response = test_client.put("/api/taxis/1", json=data, headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["chofer"] == "Smartphone"
    assert response.json["color"] == "blue"
    assert response.json["frec"] == True
    assert response.json["ingresos"] == 100.11


def test_update_nonexistent_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar actualizar un producto inexistente
    data = {
        "chofer": "Smartphone",
        "color": "red",
        "frec": True,
        "ingresos": 100.11,
    }
    response = test_client.put(
        "/api/taxis/999", json=data, headers=admin_auth_headers
    )
    assert response.status_code == 404
    assert response.json["error"] == "taxi no encontrado"


def test_delete_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder eliminar un producto existente
    response = test_client.delete("/api/taxis/1", headers=admin_auth_headers)
    assert response.status_code == 204

    # Verifica que el producto ha sido eliminado
    response = test_client.get("/api/taxis/1", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "taxi no encontrado"


def test_delete_nonexistent_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar eliminar un producto inexistente
    response = test_client.delete("/api/taxis/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "taxi no encontrado"
