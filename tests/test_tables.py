def test_create_table(client):
    response = client.post("/tables/", json={"name": "A1", "seats": 4, "location": "Window"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "A1"

def test_get_tables(client):
    response = client.get("/tables/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
