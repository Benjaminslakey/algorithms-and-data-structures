import pytest
from yekals.linked_list.singly_linked_list import SinglyLinkedList

"""
# Problem Statement

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices,
and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.

------------------------------------------------------------------------------------------------------------------------

# Constraints

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

The number of nodes in the linked list is in the range [0, 10^4].
-10^6 <= Node.val <= 10^6

------------------------------------------------------------------------------------------------------------------------

# Examples

## Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

## Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

------------------------------------------------------------------------------------------------------------------------

# Walk Through

o = odd_tail , p = prev_node, c = current_node
swap logic: p-> = c->   c-> = o->   o-> = c   c = p->

index|| 1 || 2 || 3 || 4 || 5 || 6 || 7 ||
----------------------------------------------------------
        2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
       op    c                           idx_o=1, idx_c=2
----------------------------------------------------------
        2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
        o    p    c                      idx_o=1, idx_c=3
----------------------------------------------------------
        2 -> 3 -> 1 -> 5 -> 6 -> 4 -> 7
             o    p    c                 idx_o=2, idx_c=4
----------------------------------------------------------
        2 -> 3 -> 1 -> 5 -> 6 -> 4 -> 7
             o         p    c            idx_o=2, idx_c=5   

            p-> = c->   c-> = o->   o-> = c   c = p->
               5->4        6->1        3->6    c=4
----------------------------------------------------------
        2 -> 3 -> 6 -> 1 -> 5 -> 4 -> 7
                  o         p    c       idx_o=3, idx_c=6
----------------------------------------------------------
        2 -> 3 -> 6 -> 1 -> 5 -> 4 -> 7
                  o              p    c  idx_o=3, idx_c=7
----------------------------------------------------------
        2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
                       o              pc  idx_o=4, idx_c=7
------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.oddEvenList(input_args)

    def oddEvenList(self, head):
        if head is None:
            return head

        odd_tail, prev = head, head
        node, node_idx = head.next, 2
        while node:
            if node_idx % 2 == 1: # is odd 
                ## swap nodes into place
                # remove odd node from list, replace it with node after
                prev.next = node.next
                # link removed odd node to the beginning of even list
                node.next = odd_tail.next
                # link removed odd node into the end of odd list
                odd_tail.next = node
                # mark node as the new end of the odd list
                odd_tail = odd_tail.next
                # set iterator as next node in even list
                node = prev.next
            else:
                # move pointers foward if we're on an even index
                prev = prev.next
                node = node.next
            node_idx += 1
        return head


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([], []),
    pytest.param([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
    pytest.param([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    sll = SinglyLinkedList.from_iterable(input_args)
    result = solver.solve(sll.head)
    result_sll = SinglyLinkedList(head=result)
    assert [n.val for n in result_sll] == expected_output


