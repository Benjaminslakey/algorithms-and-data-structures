from typing import List

import pytest


def reverse_digits(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def get_left(digits, idx):
    if idx > 0:
        return digits[idx - 1]
    return "10"


def next_greatest_number(number):
    digits: List[str] = list(str(number))
    right: int = len(digits) - 1
    while get_left(digits, right) >= digits[right] and -1 < right:
        right -= 1
    if right <= 0:
        return number
    first_descending, right = right - 1, len(digits) - 1
    while digits[right] <= digits[first_descending] and first_descending + 1 < right:
        right -= 1
    # swap digits
    digits[first_descending], digits[right] = digits[right], digits[first_descending]
    # reverse the rest
    reverse_digits(digits, first_descending + 1, len(digits) - 1)
    return int("".join(digits))


@pytest.mark.parametrize('number, expected', [
    pytest.param(111, 111),
    pytest.param(321, 321),
    pytest.param(19876543210, 20113456789),
    pytest.param(123, 132),
    pytest.param(5174, 5417),
    pytest.param(218765, 251678),
    pytest.param(135798642, 135824679),
    pytest.param(18446714479876543210, 18446714480123456779),
])
def test_next_greatest(number, expected):
    result = next_greatest_number(number)
    assert result == expected
