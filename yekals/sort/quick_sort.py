from random import randrange

from searching.median import median_of_medians


def deterministic_get_pivot(items, start, end):
    return median_of_medians(items, start, end)


def get_pivot(items, start, end) -> int:
    rand_pivot_idx = randrange(start, end)
    return items[rand_pivot_idx]


def partition(items, start, end, pivot):
    idx, left_bound, right_bound = start, start, end
    while idx <= right_bound:
        if items[idx] > pivot:
            items[right_bound], items[idx] = items[idx], items[right_bound]
            right_bound -= 1
        elif items[idx] < pivot:
            items[left_bound], items[idx] = items[idx], items[left_bound]
            idx += 1
            left_bound += 1
        else:
            idx += 1
    return max(start, left_bound - 1), min(end, right_bound + 1)


def quicksort(items, start=0, end=None):
    if end is None:
        end = len(items) - 1
    if start >= end:
        return
    pivot = get_pivot(items, start, end)
    partition_left, partition_right = partition(items, start, end, pivot)
    quicksort(items, start, partition_left)
    quicksort(items, partition_right, end)


