import json
import os

import pytest


DATA_DIR = os.path.join(os.path.dirname(os.getcwd()), "data")


@pytest.fixture
def sort_test_cases():
    test_cases = []
    with open(os.path.join(DATA_DIR, "shuffled_sort_tests.json")) as fixture:
        test_cases = json.load(fixture)

    def get_test(num):
        return test_cases[num]
    return get_test
