def test_application_loads(page, base_url):
    response = page.goto(base_url)
    assert response is not None
    assert response.status == 200
