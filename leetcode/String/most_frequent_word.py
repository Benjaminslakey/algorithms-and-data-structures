from typing import List

from collections import defaultdict

import pytest


class Solution:
    """
    split paragraph into words: O(n) time, O(1/2 n)space worst case
    record count of each word: O(n) time, O(n) space
    use dictionary to store counts for O(1) access to counts later
    transform banned word list to dictionary for O(1) access: O(k)
    for each word in the paragraph
        if word is not banned
            if count is higher than max
                set new max

    return max
    """

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words = set(banned)
        words = defaultdict(int)
        delimiters = {'!', '?', "'", '"', ',', '.', ';', ' '}
        curr_word = ""
        for char in paragraph:
            if char in delimiters:
                if curr_word:
                    words[curr_word] += 1
                curr_word = ""
            else:
                curr_word += char.lower()
        if curr_word:
            words[curr_word] += 1

        max_count = 0
        most_frequent = ""
        for word, count in words.items():
            if word not in banned_words and count > max_count:
                max_count = count
                most_frequent = word
        return most_frequent.lower()


@pytest.mark.parametrize('paragraph, banned, expected', [
    pytest.param("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"], "ball"),
    pytest.param("Bob", [], "bob"),
])
def test_most_common(paragraph, banned, expected):
    solver = Solution()
    result = solver.mostCommonWord(paragraph, banned)
    assert result == expected
