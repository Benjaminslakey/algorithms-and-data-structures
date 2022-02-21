import pytest

from trees.heap import MinHeap, MaxHeap


@pytest.mark.parametrize('nodes', [
    [],
    [25],
    [213, 1214],
    [213, 1214, 523],
    [213, 1214, 523, 141],
    [213, 1214, 523, 141, 623, 1241, 51],
    [213, 1214, 523, 141, 623, 1241, 51, 123415, 32981, 12, 1],

])
def test_min_heap_sort(nodes):
    min_heap = MinHeap(nodes)
    for current_min in sorted(nodes):
        heap_root = min_heap.extract_root()
        assert current_min == heap_root


@pytest.mark.parametrize('nodes', [
    [],
    [25],
    [213, 1214],
    [213, 1214, 523],
    [213, 1214, 523, 141],
    [213, 1214, 523, 141, 623, 1241, 51],
    [213, 1214, 523, 141, 623, 1241, 51, 123415, 32981, 12, 1],

])
def test_max_heap_sort(nodes):
    max_heap = MaxHeap(nodes)
    for current_max in sorted(nodes, reverse=True):
        heap_root = max_heap.extract_root()
        assert current_max == heap_root


@pytest.mark.parametrize('nodes, valid_heap', [
    pytest.param([], []),
    pytest.param([25], [25]),
    pytest.param([213, 1214], [213, 1214]),
    pytest.param([213, 1214, 523], [213, 523, 1214]),
    pytest.param([213, 1214, 523, 141], [141, 213, 523, 1214]),
    pytest.param([213, 1214, 523, 141, 623, 1241, 51], [51, 141, 523, 213, 623, 1241, 1214]),
    pytest.param([213, 1214, 523, 141, 623, 1241, 51, 123415, 32981, 12, 1],
                 [1, 12, 213, 51, 623, 523, 141, 123415, 32981, 1214, 1241]),
])
def test_min_heap_construction(nodes, valid_heap):
    min_heap = MinHeap(nodes)
    assert min_heap.nodes == valid_heap
