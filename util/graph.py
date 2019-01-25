import igraph


def create_random_graph(n=15, p=0.3):
    return igraph.Graph.Erdos_Renyi(n, p)
