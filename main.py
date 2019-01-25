import random
import time

from igraph import plot

from algorithms.breadth_first_search import breadth_first_search
from algorithms.depth_first_search import depth_first_search
from util.graph import create_random_graph

if __name__ == "__main__":
    graph = create_random_graph()
    plot(graph)

    source = random.randint(0, graph.vcount())
    key = random.randint(0, graph.vcount())
    t0 = time.time()
    key = depth_first_search(graph, source, key)
    t1 = time.time()

    print(f'Found: {key is not None}. Time: {t1 - t0}s')
