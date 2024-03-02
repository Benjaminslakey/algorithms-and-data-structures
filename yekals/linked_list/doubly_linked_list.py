from yekals.linked_list.iterator import ListIterator


class DoubleLinkNode:
    def __init__(self, val=0, nxt=None, prev=None):
        """use nxt instead of next to prevent shadowing next builtin"""
        self.val = val
        self.next = nxt
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.__length = None

    def __len__(self) -> int:
        if self.__length is not None:
            return self.__length
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        self.__length = length
        return self.__length

    def __repr__(self):
        vals = [f"{n.val}" for n in self]
        return "<->".join(vals)

    def __iter__(self):
        return ListIterator(self)

    @staticmethod
    def from_iterable(iterable):
        list_head = DoubleLinkNode()
        prev = None
        for val in iterable:
            node = DoubleLinkNode(val=val, prev=prev)
            if prev is not None:
                prev.next = node
            else:
                list_head.next = node
            prev = node
        return DoublyLinkedList(list_head.next)

# TODO: add tests
