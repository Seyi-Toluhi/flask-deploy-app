import os
os.environ.setdefault("SECRET_KEY", "test-secret-key")

from app import app

def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_dashboard_elements():
    """Verify the dashboard loads with all key sections."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Total Clients" in response.data
    assert b"Active Projects" in response.data
    assert b"Recent Invoices" in response.data
    assert b"Add Client" in response.data
    assert b"Mark as Paid" in response.data

def test_submit_flow():
    client = app.test_client()
    res = client.post("/submit", data={"text":"hello"}, follow_redirects=True)
    assert res.status_code == 200
    assert b"You typed: hello" in res.data