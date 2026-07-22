import os
import pytest


@pytest.fixture(scope="session")
def base_url():
    return os.environ["BASE_URL"]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        item.test_report = report


@pytest.fixture
def page(page, request):
    yield page

    # Screenshot for both passed and failed tests
    status = "passed" if request.node.test_report.passed else "failed"

    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    screenshot_path = f"{screenshot_dir}/{request.node.name}_{status}.png"

    page.screenshot(
        path=screenshot_path,
        full_page=True
    )
