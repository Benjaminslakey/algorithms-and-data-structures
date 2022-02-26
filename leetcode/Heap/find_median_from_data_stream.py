"""
Problem Statement

The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
------------------------------------------------------------------------------------------------------------------------
Constraints


-10^5 <= num <= 10^5
There will be at least one element in the data structure before calling findMedian.
At most 5 * 10^4 calls will be made to addNum and findMedian.
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

------------------------------------------------------------------------------------------------------------------------
Follow Ups

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
import heapq


# Solution class goes here
class MedianFinder:

    def __init__(self):
        self.count = 0
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if self.count == 0 or (self.min_heap and num > self.min_heap[0]):
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -1 * num)

        if len(self.min_heap) < len(self.max_heap):
            smaller, larger = self.min_heap, self.max_heap
        else:
            smaller, larger = self.max_heap, self.min_heap
        while len(larger) > len(smaller) + self.count % 2:
            item = heapq.heappop(larger)
            heapq.heappush(smaller, item * -1)

        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (self.min_heap[0] + (-1 * self.max_heap[0])) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        return -1 * self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
