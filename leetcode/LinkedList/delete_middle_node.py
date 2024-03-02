import pytest
from yekals.linked_list.singly_linked_list import SinglyLinkedList

"""
# Problem Statement

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
------------------------------------------------------------------------------------------------------------------------

# Constraints

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105

------------------------------------------------------------------------------------------------------------------------

# Examples

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

------------------------------------------------------------------------------------------------------------------------

# Walk Through
hptr -> 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6  idx = 0
 p      n
hptr -> 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6  idx = 1
        p    n
hptr -> 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6  idx = 2
             p    n                      
hptr -> 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6  idx = 3
                  p    n                      
p-> = (n->)

hptr -> 0 -> 1  idx = 0
  p     n
hptr -> 0 -> 1  idx = 1
        p    n

hptr -> 0  idx = 0
  p     n
------------------------------------------------------------------------------------------------------------------------
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.deleteMiddle(input_args)

    def deleteMiddle(self, head):
        length = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            length += 1
        if length == 0:
            return None

        middle = length // 2
        head_ptr = ListNode(next=head)
        prev, node = head_ptr, head
        idx = 0
        while idx < middle:
            prev, node = prev.next, node.next
            idx += 1
        prev.next = node.next
        return head_ptr.next


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]),
    pytest.param([1], []),
    pytest.param([1, 2], [1]),
    pytest.param([1, 7, 3, 5], [1, 7, 5]),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    sll = SinglyLinkedList.from_iterable(input_args)
    result = solver.solve(sll.head)
    result_sll = SinglyLinkedList(head=result)
    assert [n.val for n in result_sll] == expected_output


