"""

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.



Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9
"""
from copy import deepcopy
from typing import List

import pytest


class Solution:
    QUEEN_MARKER = 'Q'
    EMPTY_MARKER = '.'
    THREAT_MARKER = 'X'
    SAFE_MARKER = 'S'

    def __init__(self):
        self.discovered = set()
        self.solutions = []

    @staticmethod
    def get_queen_locations(chessboard):
        locations = []
        for r, row in enumerate(chessboard):
            for c, square in enumerate(row):
                if square == Solution.QUEEN_MARKER:
                    locations.append((r, c))
        return tuple(sorted(locations))

    def place_queen(self, chessboard, queen_location):
        qr, qc = queen_location
        chessboard[qr][qc] = self.QUEEN_MARKER

    def remove_queen(self, chessboard, queen_location):
        qr, qc = queen_location
        chessboard[qr][qc] = self.EMPTY_MARKER

    def record_solution(self, chessboard):
        solution_copy = deepcopy(chessboard)
        self.solutions.append(solution_copy)

    def get_candidates(self, chessboard):
        """
        return all open squares on the chessboard which are not currently under attack
        by one of the queens on the board
        """
        candidates = []
        n = len(chessboard)
        attack_board = [[self.SAFE_MARKER for _ in range(n)] for _ in range(n)]
        queen_locations = self.get_queen_locations(chessboard)
        for qr, qc in queen_locations:
            for r in range(n):
                attack_board[r][qc] = self.THREAT_MARKER
            for c in range(n):
                attack_board[qr][c] = self.THREAT_MARKER
            # 0, 0
            for delta in range(1, n + 1):
                for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    delta_row, delta_col = dr * delta, dc * delta
                    if -1 < qr + delta_row < n and -1 < qc + delta_col < n:
                        attack_board[qr + delta_row][qc + delta_col] = self.THREAT_MARKER

        for row in range(n):
            for column in range(n):
                if attack_board[row][column] == self.SAFE_MARKER:
                    candidates.append((row, column))
        return candidates

    def solve(self, board, num_queens):
        queens = self.get_queen_locations(board)
        if num_queens == 0 and queens not in self.discovered:
            self.record_solution(board)
            self.discovered.add(queens)
            return
        elif queens in self.discovered:  # prune search tree, don't explore this again
            return
        self.discovered.add(queens)

        for candidate in self.get_candidates(board):
            # need to prune duplicate solutions
            self.place_queen(board, candidate)
            self.solve(board, num_queens - 1)
            self.remove_queen(board, candidate)

    def resolve_solutions(self):
        resolved = []
        for solution in self.solutions:
            solve = ["".join(row) for row in solution]
            resolved.append(solve)
        return resolved

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[self.EMPTY_MARKER for _ in range(n)] for _ in range(n)]
        self.solve(board, n)
        return self.resolve_solutions()


def validate_queen_locations(board_size, queen_locations):
    # check that queens are not attacking each other
    queen_rows, queen_columns = set(), set()
    for row, column in queen_locations:
        assert row not in queen_rows
        assert column not in queen_columns
        queen_rows.add(row)
        queen_columns.add(column)


@pytest.mark.parametrize('num_queens, expected_solutions', [
    pytest.param(1, 1),
    pytest.param(2, 0),
    pytest.param(3, 0),
    pytest.param(4, 2),
    pytest.param(5, 10),
    pytest.param(6, 4),
    pytest.param(7, 40),
    pytest.param(8, 92),
    pytest.param(9, 352),
])
def test_n_queens(num_queens, expected_solutions):
    solver = Solution()
    result = solver.solveNQueens(num_queens)
    assert len(result) == expected_solutions
    previous_solutions = set()
    for solution in result:
        queens_on_board = solver.get_queen_locations(solution)
        assert len(queens_on_board) == num_queens
        validate_queen_locations(num_queens, queens_on_board)
        queen_locations = tuple(queens_on_board)
        assert queen_locations not in previous_solutions
        previous_solutions.add(queen_locations)


# [ 5 queens
#     ["Q....","..Q..","....Q",".Q...","...Q."],
#     ["Q....","...Q.",".Q...","....Q","..Q.."],
#     [".Q...","...Q.","Q....","..Q..","....Q"],
#     [".Q...","....Q","..Q..","Q....","...Q."],
#     ["..Q..","Q....","...Q.",".Q...","....Q"],
#     ["..Q..","....Q",".Q...","...Q.","Q...."],
#     ["...Q.","Q....","..Q..","....Q",".Q..."],
#     ["...Q.",".Q...","....Q","..Q..","Q...."],
#     ["....Q",".Q...","...Q.","Q....","..Q.."],
#     ["....Q","..Q..","Q....","...Q.",".Q..."]
# ]

# [ 6 queens
#     [".Q....","...Q..",".....Q","Q.....","..Q...","....Q."],
#     ["..Q...",".....Q",".Q....","....Q.","Q.....","...Q.."],
#     ["...Q..","Q.....","....Q.",".Q....",".....Q","..Q..."],
#     ["....Q.","..Q...","Q.....",".....Q","...Q..",".Q...."]
# ]

