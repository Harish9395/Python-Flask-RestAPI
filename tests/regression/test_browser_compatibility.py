import pytest


@pytest.mark.parametrize(
    "browser_name",
    [
        "chromium",
        "firefox",
        "webkit"
    ]
)
def test_browser_launch(browser_name, playwright, base_url):

    browser_type = getattr(playwright, browser_name)

    browser = browser_type.launch()

    page = browser.new_page()

    response = page.goto(base_url)

    assert response.ok

    browser.close()
