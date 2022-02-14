"""
Given pivot index P, rearrange array, Nums, so that all elements in Nums...
    pivot -> Nums[P]
    smaller than pivot reside to the left of all elements equal to pivot
    larger than pivot, reside to the right of pivot
    all elements equal to pivot reside in the middle

    [1, 2, 6, 5, 1, 4 ,3, 1, 2, 3, 7] pivot idx -> 3
              ^
    [1, 2, 1, 2, 3, 3, 1, 4,  || 5, ||  7, 6]
"""
import pytest


def flag_partition(nums, p):
    pivot = nums[p]
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[right] < pivot:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        if nums[right] >= pivot:
            right -= 1
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] > pivot:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        if nums[left] <= pivot:
            left += 1


@pytest.mark.parametrize('nums, p', [
    pytest.param([1, 2, 6, 5, 1, 4, 3, 1, 2, 3, 7], 3),
    pytest.param([0, 1, 2, 0, 1, 1, 2], 3),
    pytest.param([1, 3, 6, 6, 7, 5, 1, 2, 6, 6, 9], 4),
    pytest.param([1, 3, 6, 6, 7, 5, 1, 2, 6, 6, 9], 3)
])
def test_flag_partition(nums, p):
    pivot = nums[p]
    flag_partition(nums, p)
    partition_num = 1
    for num in nums:
        if partition_num == 1:
            assert num <= pivot
            if num == pivot:
                partition_num = 2
        elif partition_num == 2:
            assert num >= pivot
            if num > pivot:
                partition_num = 3
        else:
            assert num > pivot

