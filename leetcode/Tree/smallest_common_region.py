import pytest
from typing import List

"""
You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region x contains another region y then x is bigger than y. Also, by definition, a region x contains itself.

Given two regions: region1 and region2, return the smallest region that contains both of them.

If you are given regions r1, r2, and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

It is guaranteed the smallest region exists.

 

Example 1:

Input:
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
Output: "North America"
Example 2:

Input: regions = [["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]], region1 = "Canada", region2 = "South America"
Output: "Earth"

"""
class TreeNode:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent 
        self.children = []


def construct_tree(regions):
    existing_nodes = {}
    for region_def in regions:
        region_name, children = region_def[0], region_def[1:]
        if region_name in existing_nodes:
            node = existing_nodes[region_name]
        else:
            node = TreeNode(region_name)
            existing_nodes[region_name] = node
        for child_name in children:
            if child_name in existing_nodes:
                child = existing_nodes[child_name]
                child.parent = node
                node.children.append(child)
            else:
                child = TreeNode(child_name, node)
                existing_nodes[child_name] = child
    return existing_nodes


class Solution:
    """
    identified as variation of lowest common ancestor n-ary tree problem.
    1. construct tree with backwards links / parent pointers.
    2. save lookup table of all nodes based on their region name.
    3. fetch nodes from lookup table and traverse upwards to root, recording path
    4. traverse upwards from second node checking for path intersection using set for constant time lookup
    5. return intersection point
    """
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        lowest_common_ancestor = ""
        nodes = construct_tree(regions)
        r1_node, r2_node = nodes[region1], nodes[region2]
        r1_path = set()
        while r1_node is not None:
            r1_path.add(r1_node.name)
            r1_node = r1_node.parent
        while r2_node is not None:
            if r2_node.name in r1_path:
                lowest_common_ancestor = r2_node.name
                break
            r2_node = r2_node.parent
        return lowest_common_ancestor



@pytest.mark.parametrize('regions, region1, region2, expected', [
    pytest.param(
        [
            ["Earth","North America","South America"],
            ["North America","United States","Canada"],
            ["United States","New York","Boston"],
            ["Canada","Ontario","Quebec"],
            ["South America","Brazil"]
        ],
        "Quebec", "New York", "North America"
    ),
])
def test_find_smallest_region(regions, region1, region2, expected):
    solver = Solution()
    result = solver.findSmallestRegion(regions, region1, region2)
    assert result == expected

