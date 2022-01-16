# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        to_explore = deque([None, root])
        level_averages = []
        current_level_sum = 0
        current_level_node_count = 0
        while to_explore:
            current = to_explore.pop()
            if current is None:
                level_averages.append(current_level_sum / current_level_node_count)
                current_level_sum = 0
                current_level_node_count = 0
                if len(to_explore) > 0:
                    to_explore.appendleft(None)
                continue
            current_level_sum += current.val
            current_level_node_count += 1
            if current.left:
                to_explore.appendleft(current.left)
            if current.right:
                to_explore.appendleft(current.right)
        return level_averages

# @todo add unit tests
