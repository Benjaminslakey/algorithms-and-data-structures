import pytest

from sort.quick_sort import quicksort


@pytest.mark.parametrize('test_num', list(range(9)))
def test_quick_sort(sort_test_cases, test_num):
    items = sort_test_cases(test_num)
    quicksort(items)
    assert items == sorted(items)
