import os
import pytest


@pytest.fixture(scope="session")
def base_url():
    return os.environ["BASE_URL"]


@pytest.fixture
def page(page, request):
    yield page

    # Take screenshot if test failed
    if request.node.rep_call.failed:
        screenshot_path = f"screenshots/{request.node.name}.png"
        page.screenshot(path=screenshot_path)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        item.rep_call = report
