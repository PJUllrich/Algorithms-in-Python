import collections
from typing import Optional

import igraph


def depth_first_search(graph: igraph.Graph,
                       start: int,
                       val: int
                       ) -> Optional[int]:
    """
    Implementation of the Depth First Search algorithm. Searches a vertex
    with a given key in a non-directional, potentially cyclic graph.

    Note that this implementation is NOT thread-safe. For that,
    a queue.Queue() would need to be used instead of a collections.deque().

    :param graph: The igraph.Graph in which the algorithm searches.
    :param start: The id of the vertex from which the algorithm starts.
    :param val: The id of the vertex that is searched for.
    :return: Optional[int]. Returns val if the vertex is found, None otherwise.
    """
    if start < 0 or val < 0:
        raise ValueError('Start and Search index must not be negative')

    if start == val:
        return val

    q = collections.deque()
    visited = set()

    q.append(start)
    visited.add(start)

    while len(q) != 0:
        v = q.pop()

        for n in graph.neighbors(v):
            if n not in visited:
                if n == val:
                    return val

                q.append(n)
                visited.add(n)

    return None
