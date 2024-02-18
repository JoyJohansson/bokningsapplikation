import pytest
from admin_routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_admin_register(client):
    # Anropa admin register sidan
    response = client.get('/admin/register')
    assert response.status_code == 200

    # Skicka ett POST request med giltig data
    response = client.post('/admin/register', data=dict(
        username='testadmin',
        password='testpassword'
    ), follow_redirects=True)
    assert b"Admin Dashboard" in response.data

def test_admin_login(client):
    # Anropa admin login sidan
    response = client.get('/admin/login')
    assert response.status_code == 200

    # Skicka ett POST request med giltiga inloggningsuppgifter
    response = client.post('/admin/login', data=dict(
        username='testadmin',
        password='testpassword'
    ), follow_redirects=True)
    assert b"Admin Dashboard" in response.data

    # Testa ogiltiga inloggningsuppgifter
    response = client.post('/admin/login', data=dict(
        username='wronguser',
        password='wrongpassword'
    ), follow_redirects=True)
    assert b"Ogiltiga inloggningsuppgifter" in response.data


def test_admin_dashboard(client):
    # Skicka en GET request till dashboard utan inloggning
    response = client.get('/admin/dashboard', follow_redirects=True)
    assert b"Admin Login" in response.data

    # Logga in som admin
    client.post('/admin/login', data=dict(
        username='testadmin',
        password='testpassword'
    ), follow_redirects=True)

    # Skicka en GET request till dashboard efter inloggning
    response = client.get('/admin/dashboard')
    assert response.status_code == 200
    assert b"Admin Dashboard" in response.data


def test_admin_logout(client):
    # Logga in som admin
    client.post('/admin/login', data=dict(
        username='testadmin',
        password='testpassword'
    ), follow_redirects=True)

    # Skicka en POST request för att logga ut
    response = client.post('/admin/logout', follow_redirects=True)
    assert b"Admin Logout Page" in response.data

    # Verifiera att admin_token inte finns i session längre
    with client as c:
        response = c.get('/admin/dashboard')
        assert b"Admin Login" in response.data