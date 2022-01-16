from typing import List

FRESH = 1
ROTTEN = 2


class Orange:
    def __init__(self, state, row, column):
        self.state = state
        self.row = row
        self.column = column
        self.neighbors = set()

    def __str__(self):
        return f"[{self.row}][{self.column}]{'rotten' if self.state == ROTTEN else 'fresh'}"

    def __repr__(self):
        return self.__str__()


def get_neighbors(orange, grid):
    height = len(grid)
    width = len(grid[0])
    neighbors = set()
    if orange.row - 1 >= 0:
        neighbors.add(grid[orange.row - 1][orange.column])
    if orange.row + 1 < height:
        neighbors.add(grid[orange.row + 1][orange.column])
    if orange.column - 1 >= 0:
        neighbors.add(grid[orange.row][orange.column - 1])
    if orange.column + 1 < width:
        neighbors.add(grid[orange.row][orange.column + 1])
    return neighbors


def parse_oranges(grid):
    disjoint_orange = False
    fresh_oranges = set()
    rotten_oranges = set()
    # parse grid into Orange instances
    for r, row in enumerate(grid):
        for c, square in enumerate(row):
            orange = Orange(square, r, c)
            if orange.state == FRESH:
                fresh_oranges.add(orange)
            elif orange.state == ROTTEN:
                rotten_oranges.add(orange)
            else:
                orange = None
            grid[r][c] = orange
    # check for any disjoint fresh oranges, we know if a fresh orange has no neighbors at all, it can never rot
    for orange in fresh_oranges:
        orange.neighbors = get_neighbors(orange, grid)
        if orange.neighbors == {None}:
            return {}, {}, True
    # iterate over parsed graph and store adjacent node pointers on each orange for easier / more readable access code
    for orange in rotten_oranges:
        orange.neighbors = get_neighbors(orange, grid)
    return fresh_oranges, rotten_oranges, disjoint_orange


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        if disjoint sets or no rotten oranges
            return -1

        use changed set to record which fresh oranges become rotten this minute

        find all starting rotten oranges
        while fresh orange set is not empty
            for each fresh orange
                check for rotten neighbors
                if has rotten neighbors, then this will turn rotten
                    add to changed set
            remove changed oranges from fresh set
            add changed to rotten set
            if fresh set of oranges is empty, game is over
                return minutes
        """
        fresh_oranges, rotten_oranges, disjoint_orange = parse_oranges(grid)
        if disjoint_orange or (not rotten_oranges and fresh_oranges):
            return -1
        minutes = 0
        while fresh_oranges:
            minutes += 1
            rotted_this_minute = set()
            # determine what rotted by recording all fresh oranges with a rotten neighbor
            for orange in fresh_oranges:
                for nearby in orange.neighbors:
                    if nearby is not None and nearby.state == ROTTEN:
                        rotted_this_minute.add(orange)
                        break  # if we know this will turn rotten, no need to check any more neighbors
            # if no oranges rotted in this minute, any remaining fresh oranges are unreachable and we cannot continue
            if not rotted_this_minute:
                return -1
            # modify oranges  after exploring all currently fresh, otherwise rot will grow outward fast than 1 dist
            # per minute
            for orange in rotted_this_minute:
                orange.state = ROTTEN
            fresh_oranges -= rotted_this_minute  # set diff
            rotten_oranges |= rotted_this_minute  # set union
        return minutes

# @todo add unit tests
