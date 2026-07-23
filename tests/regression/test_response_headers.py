import pytest


@pytest.mark.regression
def test_security_headers(page, base_url):

    response = page.goto(base_url)

    assert response is not None
    assert response.status == 200

    headers = response.headers

    assert "content-type" in headers
    assert headers["content-type"].startswith("text/html")
