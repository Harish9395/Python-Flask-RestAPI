def test_home_page_content(page, base_url):

    page.goto(base_url)

    body = page.locator("body")

    assert body.is_visible()

    assert (
        "App Works!!!"
        in body.text_content()
    )
