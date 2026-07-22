import pytest


def test_browser_launch(browser, base_url):
    context = browser.new_context()
    page = context.new_page()

    response = page.goto(base_url)

    assert response.ok

    context.close()
