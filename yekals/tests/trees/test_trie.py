from typing import List

import pytest

from trees.trie import Trie


@pytest.mark.parametrize('words', [
    pytest.param(["ben", "benjamin", "bentayga", "bentley", "neb", "benihana"]),
    pytest.param(["apple", "ape", "application", "app", "aperol"]),
])
def test_trie_lookup(words: List[str]):
    trie = Trie()
    for word in words:
        trie.insert(word)
    for word in words:
        assert trie.search(word)
