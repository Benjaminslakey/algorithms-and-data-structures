import pytest


class Solution:
    """
    subproblem: f(text1[i:], text2[j:]) => suffixes
    relation:
        if text1[i] == text2[j]:
            1 + f(text1[i + 1, text2[j + 1])
        else:
            max(
                f(text1[i + 1], text2[j]),
                f(text1[i], text2[j + 1])
            )
    topological order: left to right => i...len(text1) , j...len(text2)
    base cases: if i >= len(text1) or j >= len(text2)
    original: f(0, 0)
    time complexity:
    """
    def __init__(self):
        self.memo = {}

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.top_down_dp(text1, text2, 0, 0)

    def top_down_dp(self, text1, text2, i, j):
        key = f"{i}:{j}"
        if key in self.memo:
            return self.memo[key]

        if i >= len(text1):
            return 0
        if j >= len(text2):
            return 0

        if text1[i] == text2[j]:
            longest = 1 + self.top_down_dp(text1, text2, i + 1, j + 1)
        else:
            longest = max(
                self.top_down_dp(text1, text2, i + 1, j),
                self.top_down_dp(text1, text2, i, j + 1)
            )
        self.memo[key] = longest
        return longest


@pytest.mark.parametrize('text1, text2, expected_lcs', [
    pytest.param("abcde", "ace", 3),
    pytest.param("their", "habit", 2),
    pytest.param("michaelangelo", "hieroglyphology", 5)
])
def test_lcs(text1, text2, expected_lcs):
    solver = Solution()
    result = solver.longestCommonSubsequence(text1, text2)
    assert result == expected_lcs

