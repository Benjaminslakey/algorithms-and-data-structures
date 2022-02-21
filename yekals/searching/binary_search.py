def binary_search(search_space, target, start=0, end=None):
    if end is None:
        end = len(search_space) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if search_space[mid] == target:
            return mid
        if search_space[mid] < target:
            end = mid - 1
        else:
            start = mid + 1
    return -1
