import pytest
from flask import session, url_for
from guest_routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_guest_login_valid(client):
    response = client.post('/guest/login', data={'booking_id': 'valid_booking_id'})
    assert response.status_code == 302  # Redirect status code
    assert response.location == url_for('guest_routes.guest_booking', _external=True)

def test_guest_login_invalid(client):
    response = client.post('/guest/login', data={'booking_id': 'invalid_booking_id'})
    assert response.status_code == 200
    assert b"Ogiltig bokingsreferens" in response.data

def test_guest_booking_authenticated(client):
    with client.session_transaction() as sess:
        sess['booking_id'] = 'authenticated_booking_id'
    response = client.get('/guest/booking')
    assert response.status_code == 200
    # Testa att se till att det returnerar bokningsinformationssidan
    assert b"guest_booking.html" in response.data

def test_guest_booking_unauthenticated(client):
    response = client.get('/guest/booking')
    assert response.status_code == 302  # Redirect status code
    assert response.location == url_for('guest_routes.guest_login', _external=True)

def test_guest_logout(client):
    response = client.post('/guest/logout')
    assert response.status_code == 302  # Redirect status code
    assert response.location == url_for('guest_routes.guest_logout_page', _external=True)

def test_guest_logout_page(client):
    response = client.get('/guest/logout_page')
    assert response.status_code == 200
    assert b"guest_logout_page.html" in response.data
