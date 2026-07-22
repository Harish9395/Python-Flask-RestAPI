def test_browser_launch(playwright, base_url):

    browser = playwright.chromium.launch()

    page = browser.new_page()

    response = page.goto(base_url)

    assert response.ok

    browser.close()
