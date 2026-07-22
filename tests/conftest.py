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


@pytest.fixture(autouse=True)
def screenshot_after_test(request, page):
    yield

    if hasattr(request.node, "test_report"):
        status = "passed" if request.node.test_report.passed else "failed"

        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        screenshot_path = f"{screenshot_dir}/{request.node.name}_{status}.png"

        page.screenshot(
            path=screenshot_path,
            full_page=True
        )
