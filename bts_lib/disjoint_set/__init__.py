from collections import defaultdict


class DisjointSet:
    def __init__(self):
        self.parents = {}
        self.depths = defaultdict(int)

    def find(self, x):
        """ use path compression to amortize future find operations to constant time """
        parent = self.parents[x]
        if parent == x:
            return x
        self.parents[x] = self.find(parent)
        self.depths[x] = 1
        return self.parents[x]

    def union(self, x, y):
        """
        use height comparison to keep tree as balanced as possible so next find operation will
        be more efficient before paths get compressed"""
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            if self.depths[x] > self.depths[y]:
                self.parents[parent_y] = parent_x
            elif self.depths[y] > self.depths[x]:
                self.parents[parent_x] = parent_y
            else:
                self.parents[parent_y] = parent_x
                self.depths[x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def add(self, x):
        self.parents[x] = x
