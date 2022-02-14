import pytest


def remove_duplicates(nums):
    """
    one pass to mark duplicates
    next pass to move first non duplicate into duplicate position
    """
    left, right = 0, 1
    while right < len(nums):
        if nums[right] > nums[left]:
            left += 1
            right += 1
        else:
            left, right = right, right + 1
            while right < len(nums) and nums[right] == nums[left]:
                right += 1
            if right < len(nums):
                nums[left] = nums[right]


@pytest.mark.parametrize('nums, expected_uniques', [
    pytest.param([2, 3, 5, 5, 7, 11, 11, 11, 13], 6),
    pytest.param([2, 3, 5, 5, 7, 11, 11, 11, 12, 13], 7),
    pytest.param([1, 2, 3, 4, 5], 0)
])
def test_remove_duplicates(nums, expected_uniques):
    remove_duplicates(nums)
    prev = -1
    for idx in range(expected_uniques):
        num = nums[idx]
        assert num != prev
