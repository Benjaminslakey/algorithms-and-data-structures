
def default_compare(a, b):
    return a <= b


def merge_sort(items, start=0, end=None, compare=default_compare):
    if end is None:
        end = len(items) - 1

    if start == end:
        return [items[start]]
    mid = start + (end - start) // 2
    left_half = merge_sort(items, start=start, end=mid, compare=compare)
    right_half = merge_sort(items, start=mid + 1, end=end, compare=compare)
    merged_items = []
    left, right = 0, 0
    left_bound, right_bound = len(left_half), len(right_half)
    while left < left_bound or right < right_bound:
        if right < right_bound and (left >= left_bound or not default_compare(left_half[left], right_half[right])):
            merged_items.append(right_half[right])
            right += 1
        elif left < left_bound and (right >= right_bound or default_compare(left_half[left], right_half[right])):
            merged_items.append(left_half[left])
            left += 1
    return merged_items
