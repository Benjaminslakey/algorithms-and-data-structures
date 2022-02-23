import heapq
from typing import Optional, List

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SortableNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

    def __gt__(self, other):
        return self.node.val > other.node.val

    def __eq__(self, other):
        return self.node.val == other.node.val

    def next(self):
        self.node = self.node.next


class Solution:
    """
    O(n log m) where M is the Math of lists and N is the total Math of items in all lists
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head_ptr = ListNode()
        new_list = head_ptr
        min_heap = [SortableNode(head_node) for head_node in lists if head_node]

        heapq.heapify(min_heap)
        while min_heap:
            list_head_container = min_heap[0]
            new_list.next = list_head_container.node
            new_list = new_list.next
            list_head_container.next()
            if list_head_container.node is not None:
                heapq.heapreplace(min_heap, list_head_container)
            else:
                heapq.heappop(min_heap)
        return head_ptr.next


def build_lists(lists_as_arrays) -> List[Optional[ListNode]]:
    list_heads = []
    for list_arr in lists_as_arrays:
        head_ptr = ListNode()
        list_node = head_ptr
        for num in list_arr:
            list_node.next = ListNode(num)
            list_node = list_node.next
        list_heads.append(head_ptr.next)
    return list_heads


@pytest.mark.parametrize('lists, expected', [
    pytest.param([[]], []),
    pytest.param([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    pytest.param([[1, 5, 8, 9], [2, 6], [], [4], [3, 7]], list(range(1, 10))),
])
def test_merge_k_sorted_lists(lists, expected):
    list_heads = build_lists(lists)
    solver = Solution()
    result = solver.mergeKLists(list_heads)
    result_array = []
    while result:
        result_array.append(result.val)
        result = result.next

    assert result_array == expected
