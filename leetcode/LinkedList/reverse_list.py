import pytest
from collections import deque

from yekals.linked_list.singly_linked_list import SinglyLinkedList

"""
# Problem Statement

Given the head of a singly linked list, reverse the list, and return the reversed list.

------------------------------------------------------------------------------------------------------------------------

# Constraints

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
------------------------------------------------------------------------------------------------------------------------

# Examples

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
------------------------------------------------------------------------------------------------------------------------

# Walk Through

------------------------------------------------------------------------------------------------------------------------

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.reverseList(input_args)

    def reverseList(self, head):
        return self.two_pointer_solution(head)

    def stack_solution(self, head):
        list_head = ListNode()
        stack = deque([])
        node = head
        while node:
            stack.append(node)
            node = node.next
        node = list_head
        while stack:
            next_node = stack.pop()
            node.next = next_node
            node = next_node
        node.next = None
        return list_head.next

    def two_pointer_solution(self, head):
        """
        we keep swapping the next node the the front of the list until we reach the end

        hptr -> 1 -> 2 -> 3 -> 4 -> 5
                n   nx                  n-> = nx->, nx-> = htpr-> = 1->3, 2->1, hptr->2
        hptr -> 2 -> 1 -> 3 -> 4 -> 5
                     n    nx
        hptr -> 3 -> 2 -> 1 -> 4 -> 5
                          n   nx
        hptr -> 4 -> 3 -> 2 -> 1 -> 5
                               n   nx
        hptr -> 5 -> 4 -> 3 -> 2 -> 1
        """

        head_ptr = ListNode(next=head)
        if head_ptr.next is None or head_ptr.next.next is None:
            return head
        node = head_ptr.next
        while node.next:
            nxt = node.next
            node.next = nxt.next
            nxt.next = head_ptr.next
            head_ptr.next = nxt
        return head_ptr.next


    def recursive_solution(self, head):
        def helper(node, prev):
            if node is None:
                return prev
            new_head = helper(node.next, node)
            node.next = prev 
            return new_head
        return helper(head, None)


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    pytest.param([1, 2], [2, 1]),
    pytest.param([], []),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    sll = SinglyLinkedList.from_iterable(input_args)
    result = solver.solve(sll.head)
    result_sll = SinglyLinkedList(result)
    assert [n.val for n in result_sll] == expected_output

