import pytest

@pytest.mark.regression
def test_home_page_content(page, base_url):

    page.goto(base_url)

    body = page.locator("body")

    assert body.is_visible()

    page_content = body.text_content()

    assert page_content is not None
    assert "App Works!!!" in page_content
