import sys


def calc_goodness(s, n):
    goodness = 0
    for i in range(0, n // 2):
        if s[i] != s[n - i - 1]:
            goodness += 1
    return goodness


def min_operations(s, n, k):
    current_score = calc_goodness(s, n)
    score_change = k - current_score
    return abs(score_change)


def parse_input():
    num_test_cases = int(input())
    for case_num in range(num_test_cases):
        n, k = input().split(" ")
        s = input()
        result = min_operations(s, int(n), int(k))
        print(f"Case #{case_num + 1}: {result}")


if __name__ == "__main__":
    parse_input()
