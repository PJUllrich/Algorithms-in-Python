import collections
from typing import Optional

import igraph


def depth_first_search(graph: igraph.Graph,
                       source: int,
                       key: int
                       ) -> Optional[int]:
    """
    An implementation of the Depth First Search algorithm. Searches a vertex
    with a given key in a non-directional, potentially cyclic graph.

    Note that this implementation is NOT thread-safe. For that,
    a queue.Queue() would need to be used instead of a collections.deque().

    :param graph: The igraph.Graph in which the algorithm searches.
    :param source: The starting vertex from which the algorithm starts.
    :param key: The id of the vertex which is searched for.
    :return: Optional[int]. Returns key if the vertex is found, None otherwise.
    """
    s = collections.deque()
    visited = set()

    s.append(source)
    visited.add(source)

    while len(s) != 0:
        v = s.pop()

        for n in graph.neighbors(v):
            if n not in visited:
                if n == key:
                    return n

                s.append(n)
                visited.add(n)

    return None
