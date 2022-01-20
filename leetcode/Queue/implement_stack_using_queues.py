from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque([])

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        num_items = len(self.queue)
        for _ in range(0, num_items - 1):
            item = self.queue.popleft()
            self.queue.append(item)
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
