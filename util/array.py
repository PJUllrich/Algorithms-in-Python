import random


def create_random_array(length=100):
    return [random.randint(0, 1000) for _ in range(length)]
