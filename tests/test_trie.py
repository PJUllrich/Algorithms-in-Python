import random
from typing import List
from unittest import TestCase

from faker import Faker

from data_structures.trie import Node, Trie


class TestTrie(TestCase):
    faker = Faker()
    trie: Trie
    words: List[str]

    def setUp(self):
        self.trie = Trie(Node(None))
        self.words = self._populate_trie()

    def test_insert(self):
        word = self.faker.word()
        self.trie.insert(word)

        self.assertTrue(
            self.trie.find(word)[0],
            f'Word {word} could not be found in Trie.'
        )

    def test_insert_multiple(self):
        for word in self.words:
            self.assertTrue(
                self.trie.find(word)[0],
                f'Word {word} could not be found in Trie.'
            )

    def test_is_member(self):
        for word in self.words:
            self.assertTrue(
                self.trie.is_member(word),
                f'Word {word} is not a member in Trie, but should be.'
            )

    def test_find_non_existent(self):
        non_existent_word = self.faker.word()
        while non_existent_word in self.words:
            non_existent_word = self.faker.word()

        found, trace = self.trie.find(non_existent_word)

        self.assertIsNone(
            found,
            f'Result {found}:{trace} is not None as expected.'
        )

    def test_remove(self):
        long_word = self.faker.word() * 2
        self.trie.insert(long_word)

        self.assertTrue(
            self.trie.remove(long_word),
            f'Word {long_word} could not be removed.'
        )

    def test_remove_non_existent(self):
        long_word = self.faker.word() * 2

        while self.trie.is_member(long_word):
            long_word = self.faker.word() * 2

        self.assertRaises(
            KeyError,
            self.trie.remove,
            long_word
        )

    def _populate_trie(self):
        num_words = random.randint(3, 10)
        words = [self.faker.word() for _ in range(0, num_words)]

        [self.trie.insert(word) for word in words]

        return words
