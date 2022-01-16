# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def __init__(self):
        self.max_depth = 0
        self.sum = 0

    def depthSumInverse(self, nestedList) -> int:
        self.find_max_depth(nestedList, 0)
        self.helper(nestedList, 0)
        return self.sum

    def find_max_depth(self, nestedList, depth):
        self.max_depth = max(self.max_depth, depth)
        for nested in nestedList:
            if not nested.isInteger():
                self.find_max_depth(nested.getList(), depth + 1)

    def helper(self, nestedList, depth):
        for nested in nestedList:
            if nested.isInteger():
                self.sum += (nested.getInteger() * (self.max_depth - depth + 1))
            else:
                self.helper(nested.getList(), depth + 1)

# @todo add unit tests
# @tags: array, recursion
