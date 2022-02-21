from random import shuffle

import pytest

from sort.merge_sort import merge_sort


@pytest.mark.parametrize('items', [
    pytest.param([2, 3, 4, 1, 52, 3]),
    pytest.param(['a', 'd', 'g', 'b', 'z', 'x', 'j']),
    pytest.param(list(range(100))),
    pytest.param(list(range(100, -1, -13))),
    pytest.param(list(range(100, -1, -3))),
])
def test_merge_sort(items):
    shuffle(items)
    sorted_items = merge_sort(items)
    assert sorted_items == sorted(items)
