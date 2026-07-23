import pytest

@pytest.mark.regression
def test_security_headers(page, base_url):

    response = page.goto(base_url)

    headers = response.headers

    assert "content-type" in headers
    assert headers["content-type"].startswith("text/html")
