import random
from unittest import TestCase

from data_structures.binary_search_tree import BinarySearchTree, Node


class TestBinarySearchTree(TestCase):
    tree: BinarySearchTree

    def setUp(self):
        random_node = Node(random.randint(0, 100))
        self.tree = BinarySearchTree(random_node)

    def test_insert_root(self):
        random_node = Node(random.randint(0, 100))
        tree = BinarySearchTree(random_node)

        self.assertEqual(
            tree.root.data,
            random_node.data,
            f'Root node data {tree.root.data} '
            f'does not equal {random_node.data}'
        )

    def test_insert_multiple(self):
        for n in range(0, random.randint(5, 10)):
            self.tree.insert(n)

        self._check_binary_search_tree(self.tree.root)

    def test_find_root(self):
        node_found = self.tree.find(self.tree.root.data)

        self.assertEqual(
            self.tree.root.data,
            node_found.data,
            f'Root data {self.tree.root.data} '
            f'is not equal to {node_found.data}'
        )

    def test_find(self):
        num_nodes = random.randint(5, 10)
        for n in range(0, num_nodes):
            self.tree.insert(n)

        random_node_data = random.randint(0, num_nodes - 1)

        found_node = self.tree.find(random_node_data)

        self.assertEqual(
            found_node.data,
            random_node_data,
            f'Found node data {found_node.data} '
            f'does not equal {random_node_data}'
        )

    def test_find_non_existent(self):
        num_nodes = random.randint(5, 10)
        for n in range(0, num_nodes):
            self.tree.insert(n)

        random_node_data = random.randint(num_nodes, 100)

        res_should_be_none = self.tree.find(random_node_data)

        self.assertIsNone(
            res_should_be_none,
            f'{res_should_be_none} should be None.'
        )

    def _check_binary_search_tree(self, node: Node):
        if node.left is not None:
            self.assertLess(
                node.left.data,
                node.data,
                f'Left node data {node.left.data} '
                f'is greater than or equal to parent node data {node.data}'
            )
            self._check_binary_search_tree(node.left)

        if node.right is not None:
            self.assertGreater(
                node.right.data,
                node.data,
                f'Right node data {node.right.data} is equal or less than '
                f'parent node data {node.data}'
            )
            self._check_binary_search_tree(node.right)
