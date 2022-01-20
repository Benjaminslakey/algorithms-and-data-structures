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


class Solution:
    def decodeString__recursive(self, s):
        def helper(s, idx):
            if not s:
                return ""

            decoded_string = ""
            nested_multiplier = 1
            while idx < len(s):
                char = s[idx]
                if char.isnumeric():
                    num_str = ""
                    while s[idx].isnumeric():
                        num_str += s[idx]
                        idx.increment()
                    nested_multiplier = int(num_str)
                elif char == "[":
                    idx.increment()
                    decoded_string += nested_multiplier * helper(s, idx)
                    nested_multiplier = 1
                elif char == "]":
                    idx.increment()
                    return decoded_string
                else:
                    decoded_string += char
                    idx.increment()
            return decoded_string
        return helper(s, IndexPointer())

    def decodeString__iterative(self, s: str) -> str:
        decoded_string = ""
        stack = deque([])
        i = 0
        while i < len(s):
            char = s[i]
            if char.isalpha():
                decoded_string += char
            elif char.isnumeric():
                num_str = ""
                while s[i].isnumeric():
                    num_str += s[i]
                    i += 1
                count = int(num_str)
            i += 1

        return decoded_string


@pytest.mark.parametrize('encoded_sting, decoded_string', [
    pytest.param("3[a]2[bc]", "aaabcbc"),
    pytest.param("13[a]2[bc]", "aaaaaaaaaaaaabcbc"),
    pytest.param("2[abc]3[de]fg", "abcabcdededefg"),
    pytest.param("3[a2[c]]", "accaccacc"),
    pytest.param("2[abc]3[cd]ef", "abcabccdcdcdef"),
    pytest.param("3[a2[c2[b]]]", "acbbcbbacbbcbbacbbcbb"),
])
def test_decode_string(encoded_sting, decoded_string):
    solver = Solution()
    result = solver.decodeString__recursive(encoded_sting)
    assert result == decoded_string
