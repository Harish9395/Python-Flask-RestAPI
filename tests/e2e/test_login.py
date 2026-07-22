import pytest

@pytest.mark.regression
def test_login(page, base_url):
    page.goto(base_url)
    # login steps
