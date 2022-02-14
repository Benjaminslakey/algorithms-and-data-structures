from typing import List

import pytest


class Solution:
    """
    3^n

    make a dictionary to represent my graph / adj list
    each number in the adj list points to it's list of possible children
    perform depth first search start from empty string as my root
    """

    def __init__(self):
        self.combinations = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        graph = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        self.dfs(digits, graph, 0, [])
        return self.combinations

    def dfs(self, digits, graph, idx, letters):
        if not idx < len(digits):
            self.combinations.append("".join(letters))
            return

        digit = digits[idx]
        children = graph[digit]
        for child in children:
            letters.append(child)
            self.dfs(digits, graph, idx + 1, letters)
            letters.pop()


@pytest.mark.parametrize('digits, expected_letter_combos', [
    pytest.param("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    pytest.param("7", ["p", "q", "r", "s"]),
    pytest.param("", []),
])
def test_letter_combos(digits, expected_letter_combos):
    solver = Solution()
    result = solver.letterCombinations(digits)
    assert result == expected_letter_combos
