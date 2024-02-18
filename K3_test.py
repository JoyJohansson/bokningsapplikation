import pytest
from K3_routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_room_info(client):
    with client.session_transaction() as sess:
        sess['start_date'] = '2024-02-18'
        sess['end_date'] = '2024-02-20'
    response = client.get('/room_info?room_id=your_room_id')
    assert response.status_code == 200
    # Testa att se till att det returnerar sidan med ruminfo
    assert b"k3_room_info.html" in response.data
