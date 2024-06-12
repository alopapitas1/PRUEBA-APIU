def test_get_products_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" debería poder obtener la lista de productos
    response = test_client.get("/api/taxis", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_product_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder crear un producto
    data = {"chofer": "Smartphone",
        "color": "blue",
        "frec": True,
        "ingresos": 100.11}
    response = test_client.post("/api/taxis", json=data, headers=user_auth_headers)
    assert response.status_code == 403



def test_update_product_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder actualizar un producto
    data = {"name": "Laptop", "description": "Updated description", "price": 1600.0, "stock": 5}
    response = test_client.put("/api/taxis/1", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_delete_product_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder eliminar un producto
    response = test_client.delete("/api/taxis/1", headers=user_auth_headers)
    assert response.status_code == 403