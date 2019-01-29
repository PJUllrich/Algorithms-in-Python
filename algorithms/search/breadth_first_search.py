import collections
import queue
from typing import Optional

import igraph


def depth_first_search(graph: igraph.Graph,
                       start: int,
                       val: int
                       ) -> Optional[int]:
    """
    Implementation of the Breadth First Search algorithm on a
    non-directional, potentially cyclical graph.

    Note that this implementation is NOT thread-safe. For that a
    queue.Queue() needs to be used instead of a collections.deque().

    :param graph: The igraph.Graph in which the algorithm searches.
    :param start: The id of the vertex from which the search is started.
    :param val: The id of the vertex which is searched for.
    :return: Optional[int]. Returns val if vertex is found, None otherwise.
    """
    if start < 0 or val < 0:
        raise ValueError('Start and Search indices must not be negative.')

    if start == val:
        return val

    q = collections.deque([start])
    visited = set([start])

    while len(q) != 0:
        v = q.popleft()

        for n in graph.neighbors(v):
            if n not in visited:
                if n == val:
                    return val

                q.append(n)
                visited.add(n)

    return None
