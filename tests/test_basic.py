from app import app

def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_submit_flow():
    client = app.test_client()
    res = client.post("/submit", data={"text":"hello"}, follow_redirects=True)
    assert res.status_code == 200
    assert b"You typed: hello" in res.data