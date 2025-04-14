from datetime import datetime, timedelta

def test_create_reservation_success(client):
    start_time = datetime.now().isoformat()
    response = client.post("/reservations/", json={
        "table_id": 1,
        "customer_name": "Alice",
        "reserved_time": start_time,
        "duration_minutes": 30
    })
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "Alice"

def test_create_reservation_conflict(client):
    start_time = datetime.now().isoformat()
    # Первая — должна пройти
    client.post("/reservations/", json={
        "table_id": 1,
        "customer_name": "Bob",
        "reserved_time": start_time,
        "duration_minutes": 30
    })
    # Вторая — должна конфликтовать
    response = client.post("/reservations/", json={
        "table_id": 1,
        "customer_name": "Charlie",
        "reserved_time": start_time,
        "duration_minutes": 15
    })
    assert response.status_code == 500 or response.status_code == 400
    