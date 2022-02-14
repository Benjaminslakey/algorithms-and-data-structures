from typing import Optional


class TrieNode:
    def __init__(self, character):
        self.value = character
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = TrieNode(letter)
                node.children[letter] = new_node
                node = new_node
        node.children[0] = True

    def _find(self, word: str) -> Optional[TrieNode]:
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._find(word)
        if node is None:
            return False
        return 0 in node.children

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None
