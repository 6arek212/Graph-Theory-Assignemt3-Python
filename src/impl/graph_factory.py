import random

from src.impl.di_graph import DiGraph


def getGraphInstance(node_size: int, edges_size: int, seed: int = 1):
    """
        create a random graph
        :param node_size: size of nodes
        :param edges_size: size of edges
        :param seed: seed for debug
        :return: connected graph
        """
    graph = DiGraph()
    for i in range(0, node_size):
        random.seed(seed)
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        graph.add_node(i, (x, y, 0))

    for i in range(0, edges_size):
        id1 = random.randint(0, node_size - 1)
        id2 = random.randint(0, node_size - 1)
        w = random.randint(0, 10)
        graph.add_edge(id1, id2, w)
    return graph


def getConnectedGraphInstance(node_size: int, seed: int = 1):
    """
    create a random connected graph with node_size nodes
    :param node_size: size of nodes
    :param seed: seed for debug
    :return: connected graph
    """
    graph = DiGraph()
    for i in range(0, node_size):
        random.seed(seed)
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        graph.add_node(i, (x, y, 0))

    for i in range(0, node_size - 1):
        w = random.randint(0, 10)
        graph.add_edge(i, i + 1, w)
    graph.add_edge(node_size - 1, 0, random.randint(0, 10))
    return graph
