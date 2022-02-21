from abc import ABC
from typing import Protocol, List


class Comparable(Protocol):
    def __lt__(self, other):
        ...

    def __eq__(self, other):
        ...

    def __gt__(self, other):
        ...


class HeapException(Exception):
    ...


class Heap(ABC):
    root_idx = 0

    def __init__(self, nodes: List[Comparable] = None):
        if nodes is None:
            nodes = []
        self.nodes = nodes
        for idx in range((len(self.nodes) - 1) // 2, -1, -1):
            self._heapify_down(idx)

    def __repr__(self):
        return f"{self.nodes}"

    def __len__(self):
        return len(self.nodes)

    def invariant(self, a: Comparable, b: Comparable) -> bool:
        ...

    def dominates(self, parent_idx: int, child_idx: int) -> bool:
        parent_node = self._get_node(parent_idx)
        child_node = self._get_node(child_idx)
        return self.invariant(parent_node, child_node)

    @staticmethod
    def _parent_idx(node_idx: int) -> int:
        if node_idx == Heap.root_idx:
            return -1
        return node_idx // 2

    @staticmethod
    def _left_child_idx(node_idx: int) -> int:
        if node_idx == Heap.root_idx:
            return 1
        return 2 * node_idx

    @staticmethod
    def _right_child_idx(node_idx: int) -> int:
        if node_idx == Heap.root_idx:
            return 2
        return (2 * node_idx) + 1

    def _get_node(self, node_idx):
        if not Heap.root_idx <= node_idx < self.size():
            return None
        return self.nodes[node_idx]

    def _swap(self, node_idx, replacement_idx):
        temp = self.nodes[node_idx]
        self.nodes[node_idx] = self.nodes[replacement_idx]
        self.nodes[replacement_idx] = temp

    def _heapify_up(self, node_idx: int):
        parent_idx = self._parent_idx(node_idx)
        while parent_idx >= Heap.root_idx and not self.dominates(parent_idx, node_idx):
            self._swap(parent_idx, node_idx)
            node_idx = parent_idx
            parent_idx = self._parent_idx(node_idx)

    def _heapify_down(self, root_idx):
        num_nodes = self.size()
        if num_nodes <= 1:
            return

        parent_idx = root_idx
        while parent_idx < num_nodes:
            left_child_idx = self._left_child_idx(parent_idx)
            right_child_idx = self._right_child_idx(parent_idx)
            if not (
                    (left_child_idx < num_nodes and self.dominates(left_child_idx, parent_idx)) or
                    (right_child_idx < num_nodes and self.dominates(right_child_idx, parent_idx))
            ):
                break
            elif right_child_idx >= num_nodes or self.dominates(left_child_idx, right_child_idx):
                self._swap(left_child_idx, parent_idx)
                parent_idx = left_child_idx
            elif self.dominates(right_child_idx, left_child_idx):
                self._swap(right_child_idx, parent_idx)
                parent_idx = right_child_idx
            else:
                break

    def _insert(self, node):
        self.nodes.append(node)
        node_idx = len(self) - 1
        self._heapify_up(node_idx)

    def find_root(self):
        if self.is_empty():
            return None
        return self.nodes[Heap.root_idx]

    def delete_root(self):
        self.extract_root()

    def extract_root(self):
        if self.is_empty():
            raise HeapException("Heap is empty")
        root_node = self.nodes.pop(Heap.root_idx)
        if not self.is_empty():
            rightmost_node = self.nodes.pop()
            self.nodes.insert(Heap.root_idx, rightmost_node)
            self._heapify_down(Heap.root_idx)
        return root_node

    def size(self):
        return len(self)

    def is_empty(self):
        return len(self) == 0


class MinHeap(Heap):
    def invariant(self, a, b):
        return a <= b


class MaxHeap(Heap):
    def invariant(self, a, b):
        return a >= b
