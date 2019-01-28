import random
from unittest import TestCase

import igraph

from algorithms.search.depth_first_search import depth_first_search
from util.graph import create_random_graph


class TestDepthFirstSearch(TestCase):
    graph: igraph.Graph

    def setUp(self):
        self.graph = create_random_graph()

    def test_find_vertex(self):
        start = 0
        find = random.randint(1, self.graph.vcount() - 1)

        found = depth_first_search(self.graph, start, find)

        self.assertEqual(
            find,
            found,
            f'Could not find vertex {find} in graph. Result: {found}'
        )

    def test_find_non_existent(self):
        start = 0
        find = self.graph.vcount() + 1

        found = depth_first_search(self.graph, start, find)

        self.assertIsNone(
            found,
            f'Result is not None as expected. Result: {found}'
        )

    def test_start_and_find_vertex_are_equal(self):
        start = random.randint(0, self.graph.vcount())
        find = start

        found = depth_first_search(self.graph, start, find)

        self.assertEqual(
            find,
            found,
            f'Result is not equal to expected outcome: {find}. Result: {found}'
        )

    def test_find_vertex_with_negative_id(self):
        start = 0
        find = random.randint(1, self.graph.vcount()) * -1

        self.assertRaises(
            ValueError,
            depth_first_search,
            self.graph,
            start,
            find
        )

    def test_start_vertex_has_negative_id(self):
        start = random.randint(1, self.graph.vcount()) * -1
        find = random.randint(1, self.graph.vcount())

        self.assertRaises(
            ValueError,
            depth_first_search,
            self.graph,
            start,
            find
        )
