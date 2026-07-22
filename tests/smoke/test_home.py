import pytest


@pytest.mark.smoke
def test_home(page, base_url):

    response = page.goto(base_url)

    assert response.status == 200

    assert "App Works!!!" in page.locator("body").text_content()
