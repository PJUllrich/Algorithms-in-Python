import collections
import queue
from typing import Optional

import igraph


def breadth_first_search(graph: igraph.Graph,
                         source: int,
                         key: int
                         ) -> Optional[int]:
    """
    Implementation of the Breadth First Search algorithm on a
    non-directional, potentially cyclical graph.

    Note that this implementation is NOT thread-safe. For that a
    queue.Queue() needs to be used instead of a collections.deque().

    :param graph: The igraph.Graph in which the algorithm searches.
    :param source: The source vertex from which the search is started.
    :param key: The id of the vertex which is searched for.
    :return: Optional[int]. Returns key if vertex is found, None otherwise.
    """

    visited = set()
    q = collections.deque()

    q.append(source)
    visited.add(source)

    while q.maxlen != 0:
        v = q.popleft()

        for n in graph.neighbors(v):
            if n not in visited:
                if n == key:
                    return n

                q.append(n)
                visited.add(n)

    return None
