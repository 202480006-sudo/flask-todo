from app import app

def test_get_tasks():
    client = app.test_client()
    response = client.get('/api/tasks')
    assert response.status_code == 200


def test_create_task():
    client = app.test_client()
    response = client.post('/api/tasks', json={
        "title": "Test Task"
    })
    assert response.status_code == 201


def test_create_invalid():
    client = app.test_client()
    response = client.post('/api/tasks', json={})
    assert response.status_code == 400