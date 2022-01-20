from collections import deque


class MyQueue:

    def __init__(self):
        self.push_stack = deque([])
        self.pop_stack = deque([])

    def _switch_stacks(self):
        if 0 < len(self.push_stack) and 0 < len(self.pop_stack):
            raise Exception("both stacks have items in them")
        current_stack = self.push_stack if len(self.push_stack) > 0 else self.pop_stack
        target_stack = self.pop_stack if len(self.push_stack) > 0 else self.push_stack
        while len(current_stack):
            item = current_stack.pop()
            target_stack.append(item)

    def push(self, x: int) -> None:
        if len(self.pop_stack) > 0:
            self._switch_stacks()
        self.push_stack.append(x)

    def pop(self) -> int:
        if len(self.push_stack) > 0:
            self._switch_stacks()
        return self.pop_stack.pop()

    def peek(self) -> int:
        if len(self.push_stack) > 0:
            return self.push_stack[0]
        elif len(self.pop_stack) > 0:
            return self.pop_stack[-1]

    def empty(self) -> bool:
        return len(self.push_stack) + len(self.pop_stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
