import pytest


class Solution:
    """
    subproblem: is this smaller version of t a subsequence of this smaller version of s => subsequence(s[i], t[j])
    relation:  if s[i] = t[j] => s[i + 1], t[j + 1] else s[i + 1], t[j]
    topo: for s[i...n] for t[j...m]
    base case: i >= len(s) => False or j >= len(t) => True
    original: s[0], t[0]
    time: (s + 1) * (t + 1)
    """
    def __init__(self):
        self.memo = {}

    def isSubsequence(self, s: str, t: str) -> bool:
        return self.top_down_dp(s, t, 0, 0)

    def top_down_dp(self, s, t, i, j):
        key = f"{i}:{j}"
        if j >= len(s):
            return True
        if i >= len(t):
            return False

        if t[i] == s[j]:
            is_subseq = self.top_down_dp(s, t, i + 1, j + 1)
        else:
            is_subseq = self.top_down_dp(s, t, i + 1, j)
        self.memo[key] = is_subseq
        return is_subseq


@pytest.mark.parametrize('s, t, expected', [
    pytest.param("abc", "ahbgdc", True),
    pytest.param("abc", "ahgdc", False),
])
def test_is_subsequence(s, t, expected):
    solver = Solution()
    result = solver.isSubsequence(s, t)
    assert result == expected
