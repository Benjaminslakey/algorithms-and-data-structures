import heapq
from collections import Counter, defaultdict
from typing import List

import pytest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        count_map = defaultdict(list)
        heap = []
        for num, count in counts.items():
            count_map[count].append(num)
            heap.append(-1 * count)
        heapq.heapify(heap)
        output = []
        while k > 0:
            cnt = heapq.heappop(heap)
            num = count_map[cnt * -1].pop()
            output.append(num)
            k -= 1
        return output


@pytest.mark.parametrize('nums, k, most_frequent', [
    pytest.param([1], 1, [1]),
    pytest.param([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    pytest.param([1, 1, 1, 2, 2, 3], 3, [1, 2, 3]),
    pytest.param([1, 1, 1, 2, 2, 3, 4, 4, 4], 3, [1, 2, 4]),
])
def test_k_most_frequent(nums, k, most_frequent):
    solver = Solution()
    frequent = solver.topKFrequent(nums, k)
    assert sorted(frequent) == sorted(most_frequent)
