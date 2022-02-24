import pytest

from sort.merge_sort import merge_sort


@pytest.mark.parametrize('test_num', list(range(9)))
def test_merge_sort(sort_test_cases, test_num):
    items = sort_test_cases(test_num)
    sorted_items = merge_sort(items)
    assert sorted_items == sorted(items)
