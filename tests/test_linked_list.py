import random
from unittest import TestCase

from faker import Faker

from data_structures.linked_list import LinkedList, Node


class TestLinkedList(TestCase):
    faker = Faker()
    list: LinkedList
    num_nodes = 5

    def setUp(self):
        nodes = [Node(x) for x in range(0, self.num_nodes)]
        self.list = LinkedList()
        for node in nodes:
            self.list.add(node)

    def test_add_node(self):
        random_node = Node(self.faker.sentence())
        self.list.add(random_node)

        last_node = self.list.find_last()

        self.assertEqual(
            last_node,
            random_node,
            f'Last node: {last_node} does not equal {random_node}.'
        )

    def test_add_first_node(self):
        random_node = Node(self.faker.sentence())
        self.list.add_first(random_node)

        self.assertEqual(
            self.list.head,
            random_node,
            f'Head node of list: {self.list.head} does not equal {random_node}'
        )

    def test_traverse(self):
        counter = 0
        for node in self.list.traverse():
            self.assertEqual(
                node.data,
                counter,
                f'Node data {node.data} does not equal {counter}.'
            )
            counter += 1

    def test_add_after(self):
        random_index = random.randint(0, self.num_nodes - 1)
        node = self.list.find(Node(random_index))

        random_node = Node(random.randint(self.num_nodes + 1, 100))
        self.list.add_after(node, random_node)

        self.assertEqual(
            node.next,
            random_node,
            f'Next node of {node} does not equal {random_node}'
        )

    def test_add_before(self):
        random_index = random.randint(0, self.num_nodes - 1)
        node = self.list.find(Node(random_index))

        random_node = Node(random.randint(self.num_nodes + 1, 100))
        self.list.add_before(node, random_node)

        self.assertEqual(
            random_node.next.data,
            node.data,
            f'Next node of {random_node}: {random_node.next} '
            f'does not equal {node}'
        )

    def test_find(self):
        random_index = random.randint(0, self.num_nodes - 1)
        random_node_to_find = Node(random_index)

        found_node = self.list.find(random_node_to_find)

        self.assertEqual(
            random_node_to_find.data,
            found_node.data,
            f'Found Node {found_node.data} is not equal '
            f'to {random_node_to_find.data}'
        )

    def test_find_non_existent(self):
        random_non_existent_index = random.randint(self.num_nodes + 1, 1000)
        res_should_be_none = self.list.find(Node(random_non_existent_index))

        self.assertIsNone(
            res_should_be_none,
            f'Result: {res_should_be_none} is not None as expected.'
        )

    def test_find_last(self):
        last_node = Node(self.num_nodes - 1)
        found_node = self.list.find_last()

        self.assertEqual(
            last_node.data,
            found_node.data,
            f'Last node {found_node} not equal to expected {last_node}'
        )

    def test_find_before(self):
        random_index_not_head = random.randint(1, self.num_nodes - 1)
        random_node = Node(random_index_not_head)

        node_before = self.list.find_before(random_node)

        self.assertEqual(
            node_before.data,
            random_index_not_head - 1,
            f'Node before {node_before.data} is not equal '
            f'to {random_index_not_head - 1}'
        )

    def test_delete(self):
        random_node = Node(random.randint(0, self.num_nodes - 1))
        self.list.delete(random_node)

        should_be_none = self.list.find(random_node)

        self.assertIsNone(
            should_be_none,
            f'{should_be_none} is not None as expected.'
        )
