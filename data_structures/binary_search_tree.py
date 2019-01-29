from __future__ import annotations

from typing import Optional


class Node:
    """
    Node class for a Binary Search Tree. Holds one data value and
    optional references to left and right child nodes
    """
    data: any
    left: Optional[Node]
    right: Optional[Node]

    def __init__(self, data: any):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Implementation of basic functions of a Binary Search Tree.

    Supports insertion and finding Nodes in a Binary Search Tree.
    """
    root: Optional[Node]

    def __init__(self, root: Node):
        self.root = root

    def insert(self, data: any, node: Optional[Node] = None):
        """
        Insert data into the Binary Search Tree.

        Gets called recursively until a suitable place for the data value
        is found.

        :param data: Any object implementing the greater/smaller/equal
        functionality
        :param node: A node in the Binary Search Tree that gets passed on by
        recursive calls
        """

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
        """
        Finds a Node in the Binary Search Tree with a given data value.

        This function gets called recursively until either a node is found
        that contains the searched for data or the bottom layer of the tree
        is reached.

        :param data: The data of the Node that is searched for
        :param node: A Node in the Binary Search Tree that is passed on by
        recursive calls.
        :return: Optional[Node]
        """

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
