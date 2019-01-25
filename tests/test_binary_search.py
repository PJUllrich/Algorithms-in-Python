import random
from unittest import TestCase

from algorithms.search.binary_search import binary_search


class TestBinarySearch(TestCase):
    arr: list

    def setUp(self):
        length = random.randint(10, 1000)
        self.arr = range(0, length)

    def test_find_value_in_array(self):
        val = random.randint(0, len(self.arr))

        pos = binary_search(self.arr, val)

        self.assertEqual(
            val,
            pos,
            f'Result {pos} not equal to expected {val}'
        )

    def test_find_non_existent(self):
        val = random.randint(0, 100) * -1

        result = binary_search(self.arr, val)

        self.assertIsNone(
            result,
            f'Result {result} not None as expected'
        )

    def test_find_first_element(self):
        val = 0

        result = binary_search(self.arr, val)

        self.assertEqual(
            result,
            0,
            f'Result {result} is not 0 as expected'
        )

    def test_find_last_item(self):
        val = len(self.arr) - 1

        result = binary_search(self.arr, val)

        self.assertEqual(
            result,
            val,
            f'Result {result} is not {val} as expected'
        )
