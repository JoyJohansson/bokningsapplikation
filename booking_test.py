import pytest
from flask import session
from booking_routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_room(client):
    response = client.get('/contacts')
    assert response.status_code == 200
    # Testa att se till att det returnerar en sida utan data
    assert b"No data found" in response.data

def test_book_room(client):
    response = client.post('/book', data={'room_id': 'your_room_id'})
    assert response.status_code == 200
    # Testa att se till att det returnerar en bekräftelsesida
    assert b"k4_booking_confirmation.html" in response.data

def test_save_booking(client):
    # Antag att vi har alla nödvändiga formdata här
    with client.session_transaction() as sess:
        sess['start_date'] = '2024-02-18'
        sess['end_date'] = '2024-02-20'
        sess['selected_guests'] = 2
    response = client.post('/save_booking', data={'options': ['option1', 'option2'], 'booking_ID': 'your_booking_id', 'room_id': 'your_room_id', 'epost1': 'test@example.com', 'name': 'Test Name', 'price_per_night': '100'})
    assert response.status_code == 200
    # Testa att se till att det returnerar en bekräftelsesida
    assert b"k4_booking_confirmation.html" in response.data

def test_guest_booking(client):
    with client.session_transaction() as sess:
        sess['booking_id'] = 'your_booking_id'
    response = client.get('/guest/booking')
    assert response.status_code == 200
    # Testa att se till att det returnerar bokningsinformationssidan
    assert b"guest_booking.html" in response.data

def test_cancel_booking(client):
    # Antag att du har en bokning i databasen för att testa avbokning
    response = client.get('/cancel_booking?booking_id=your_booking_id')
    assert response.status_code == 200
    # Testa att se till att det returnerar ett meddelande om att avbokningen lyckades
    assert b"Booking canceled successfully" in response.data
