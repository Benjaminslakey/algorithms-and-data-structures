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


def parse_count(i, s):
    num_repeat = ""
    while i < len(s):
        if not s[i].isdigit():
            break
        num_repeat += s[i]
        i += 1
    return num_repeat


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

    def decodeString(self, s):
        stack = []
        encoded = ""
        idx = 0
        while idx < len(s):
            c = s[idx]
            if c.isdigit():
                count = parse_count(idx, s)
                repeat_count = int(count)
                # since we know the input will always be well formed, the next character after parsing out count will be the opening brace
                # do both steps here, skipping past the opening brace in the string and appending to the stack
                stack.append((encoded, repeat_count))
                encoded = ""
                idx += len(count)
            elif c == ']':
                prev_string, repeat_count = stack.pop()
                encoded = prev_string + (encoded * repeat_count)
            else:
                encoded += c
            idx += 1
        return encoded



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
    decoded_string = solver.decodeString(encoded_string)
    assert decoded_string == expected_decoded_string
