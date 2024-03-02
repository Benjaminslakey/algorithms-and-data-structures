from yekals.linked_list.iterator import ListIterator


class SingleLinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.__length = None
        self.__current = None

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
        return "->".join(vals)


    def __iter__(self):
        return ListIterator(self)
         

    @staticmethod
    def from_iterable(iterable):
        list_head = SingleLinkNode()
        prev = list_head
        for val in iterable:
            node = SingleLinkNode(val=val)
            prev.next = node
            prev = node
        return SinglyLinkedList(list_head.next)

