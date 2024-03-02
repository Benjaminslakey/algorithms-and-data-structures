from typing import Protocol, Any

class ListNode(Protocol):
    val: Any
    next: 'ListNode'

class LinkedList(Protocol):
    head: ListNode 

    def __len__(self) -> int:
        ...


class ListIterator:
    def __init__(self, ll: LinkedList):
        self.ll: LinkedList = ll
        self.__current: ListNode = ll.head 

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.ll) == 0 or self.__current is None:
            raise StopIteration
        prev = self.__current
        self.__current = prev.next
        return prev
