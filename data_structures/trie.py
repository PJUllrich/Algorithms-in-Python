from __future__ import annotations

from collections import deque
from typing import List, Optional, Tuple


class Node:
    """
    Node implementation for a Trie data structure.

    Attributes:
        char        single character of a word
        children    list of children nodes
        final       indicates whether the node ends a word (i.e. holds the
                    last character of a word)
    """

    char: Optional[str]
    children: dict
    final: bool

    def __init__(self, char: Optional[str]):
        self.char = char
        self.children = {}
        self.final = False


class Trie:
    """
    Implementation of a Trie data structure which holds strings

    Attributes:
        root    root node of the trie. Holds None as a character
    """
    root: Node

    def __init__(self, root: Node):
        self.root = root

    def insert(self, key: str):
        """
        Insert a string into the Trie.

        Iterates over every character of the string and adds new nodes if
        nodes holding the characters are not present.

        :param key: string to be stored in the trie
        """

        end_node, _ = self.find(key, True)
        end_node.final = True

    def is_member(self, key: str) -> bool:
        """
        Searches for a string in the Trie

        :param key: string to be searched for in the Trie
        :return: True if word was found. False otherwise.
        """

        found, _ = self.find(key)
        return found is not None

    def find(self, key: str, create: bool = False) \
            -> Tuple[Optional[Node], List[Node]]:
        """
        Finds a string in the Trie.

        Note that the returned trace does NOT include the end node.

        :param key:     string to be found
        :param create:  whether to create nodes for characters that weren't
                        found
        :return:        End node of word and trace of nodes to that end node
        """

        q = deque([c for c in key])

        trace = []
        node = self.root
        while len(q) > 0:
            trace.append(node)
            char = q.popleft()
            child = node.children.get(char, None)
            if child is None:
                if create:
                    child = Node(char)
                    node.children[char] = child
                else:
                    return None, trace

            node = child

        return node, trace

    def remove(self, key: str) -> bool:
        """
        Removes a string from the Trie.

        :param key: string to be removed
        :return: True if string could be removed. False otherwise.
        :raises: KeyError if the string could not be found in the Trie
        """

        end_node, trace = self.find(key)

        if end_node is None:
            raise KeyError(f'{key} does not exist in Trie')

        if len(end_node.children) > 0:
            return False

        while len(trace) > 1:
            node = trace.pop()
            if len(node.children) > 1:
                break

            node.children = {}

            if node.final:
                break

        return True
