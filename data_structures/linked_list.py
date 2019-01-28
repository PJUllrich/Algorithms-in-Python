from __future__ import annotations


class Node:
    data: any
    next: Node

    def __eq__(self, other: Node):
        return self.data == other.data

    def __str__(self):
        return str(self.data)

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    head: Node

    def __init__(self):
        self.head = None

    def add(self, node: Node):
        if self.head is None:
            return self.add_first(node)

        end = self.find_last()
        end.next = node

    def add_first(self, node: Node):
        node.next = self.head
        self.head = node

    def traverse(self):
        tmp = self.head

        while tmp is not None:
            yield tmp
            tmp = tmp.next

    def add_after(self, node: Node, to_insert: Node):
        tmp = self.head
        while tmp.next is not None and tmp != node:
            tmp = tmp.next

        if tmp is not None:
            to_insert.next, tmp.next = tmp.next, to_insert

    def add_before(self, node: Node, to_insert: Node):
        if self.head is None:
            return

        if node == self.head:
            self.add_first(to_insert)
            return

        tmp = self.head
        while tmp.next is not None and tmp.next != node:
            tmp = tmp.next

        to_insert.next = tmp.next
        tmp.next = to_insert

    def find(self, node: Node):
        tmp = self.head
        while tmp is not None and tmp != node:
            tmp = tmp.next

        return tmp

    def find_last(self):
        node = self.head
        while node.next is not None:
            node = node.next

        return node

    def find_before(self, node: Node):
        tmp = self.head
        while tmp.next != node and tmp.next is not None:
            tmp = tmp.next

        return tmp

    def delete(self, node: Node):
        if self.head is None:
            return

        if node == self.head:
            self.head = self.head.next
            return

        before = self.find_before(node)
        before.next = node.next
