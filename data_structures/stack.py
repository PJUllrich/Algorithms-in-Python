from typing import List


class Stack:
    stack: List[any]

    def __init__(self):
        self.stack = []

    def append(self, obj):
        self.stack.append(obj)

    def pop(self):
        self.stack.pop()
