from __future__ import annotations

from typing import Optional


class Node:
    data: any
    left: Optional[Node]
    right: Optional[Node]

    def __init__(self, data: any):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    root: Optional[Node]

    def __init__(self):
        self.root = None

    def insert(self, data: any, node: Optional[Node] = None):
        if self.root is None:
            self.root = Node(data)
            return

        node = self.root if node is None else node

        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert(data, node.right)
        else:
            node.data = data

    def find(self, data: any, node: Optional[Node] = None):
        if self.root is None:
            return None

        node = self.root if node is None else node

        if data == node.data:
            return node
        elif data < node.data:
            if node.left is None:
                return None
            return self.find(data, node.left)
        else:
            if node.right is None:
                return None
            return self.find(data, node.right)
