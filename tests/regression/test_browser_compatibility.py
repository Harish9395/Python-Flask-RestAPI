def test_browser_launch(page, base_url):

    response = page.goto(base_url)

    assert response is not None
    assert response.status == 200
