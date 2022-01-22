# @tags: [stack, string]

from collections import deque

import pytest


class IndexPointer:
    def __init__(self, i=0):
        self.i = i

    def __lt__(self, other):
        return self.i < other

    def __gt__(self, other):
        return self.i > other

    def __eq__(self, other):
        return self.i == other

    def __index__(self):
        return self.i

    def increment(self):
        self.i += 1
        return self


class Solution:
    @staticmethod
    def decode_string__recursive(s: str, idx: IndexPointer) -> str:
        decoded = ""
        num_str = ""
        while idx < len(s):
            char = s[idx]
            if char.isalpha():
                decoded += char
            if char == ']':
                break
            elif char.isdigit():
                while s[idx].isdigit():
                    num_str += s[idx]
                    idx.increment()
                nested = Solution.decode_string__recursive(s, idx.increment())
                decoded += nested * int(num_str)
                num_str = ""
            idx.increment()
        return decoded

    @staticmethod
    def decode_string__iterative(s: str) -> str:
        stack = deque([])
        decoded = ""
        partial = ""
        idx = 0
        while idx < len(s):
            char = s[idx]
            if char.isalpha():
                if not stack:
                    decoded += char
                else:
                    partial += char
            elif char.isdigit():
                num_str = ""
                while s[idx].isdigit():
                    num_str += s[idx]
                    idx += 1
                num = int(num_str)
                stack.append((num, partial))
                partial = ""
            elif char == ']':
                multiplier, parent = stack.pop()
                parent += partial * multiplier
                if not stack:
                    decoded += parent
                    partial = ""
                else:
                    partial = parent
            idx += 1
        return decoded


decode_string_test_cases = [
    pytest.param("3[a2[c]]", "accaccacc"),
    pytest.param("3[a2[c2[b]]]", "acbbcbbacbbcbbacbbcbb"),
    pytest.param("3[a]2[bc]", "aaabcbc"),
    pytest.param("13[a]2[bc]", "aaaaaaaaaaaaabcbc"),
    pytest.param("2[abc]3[de]fg", "abcabcdededefg"),
    pytest.param("2[abc]3[cd]ef", "abcabccdcdcdef"),
]


@pytest.mark.parametrize('encoded_string, expected_decoded_string', decode_string_test_cases)
def test_decode_string__recursive(encoded_string, expected_decoded_string):
    solver = Solution()
    decoded_string = solver.decode_string__recursive(encoded_string, IndexPointer())
    assert decoded_string == expected_decoded_string


@pytest.mark.parametrize('encoded_string, expected_decoded_string', decode_string_test_cases)
def test_decode_string__iterative(encoded_string, expected_decoded_string):
    solver = Solution()
    decoded_string = solver.decode_string__iterative(encoded_string, 0)
    assert decoded_string == expected_decoded_string
