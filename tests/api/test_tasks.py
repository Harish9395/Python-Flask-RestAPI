import requests


def test_get_tasks():

    response = requests.get(
        "http://127.0.0.1:5000/api/tasks"
    )

    assert response.status_code == 200
