import os
import pytest


@pytest.fixture(scope="session")
def base_url():
    return os.environ["BASE_URL"]
