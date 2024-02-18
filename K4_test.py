import pytest
from K4_routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_K4_routes(client):
    response = client.get('/K4_routes')
    assert response.status_code == 200
    assert b"This is the route function for K4_routes." in response.data

def test_bekraftelse(client):
    booking_reference = "your_booking_reference"
    response = client.get(f'/bekraftelse?booking_ref={booking_reference}')
    assert response.status_code == 200
    assert bytes(booking_reference, 'utf-8') in response.data
    assert b"k4_booking_confirmation.html" in response.data
