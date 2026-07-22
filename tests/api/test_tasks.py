import requests


def test_get_tasks(base_url):

    response = requests.get(
        f"{base_url}/api/tasks"
    )

    assert response.status_code == 200
