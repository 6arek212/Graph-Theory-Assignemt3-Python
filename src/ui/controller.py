from typing import List

from src.impl.graph_algo import GraphAlgo


class ShortestPathEvent:
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2


class CenterEvent:
    pass


class TSPEvent:
    def __init__(self, node_lst: List[int]):
        self.nodes_lst: List[int] = node_lst


class UIController:
    """
    this controller handles the graph algorithm functions
    """
    def __init__(self, graph_algo: GraphAlgo, callback):
        self.graph_algo = graph_algo
        self.callback = callback

    def on_trigger_event(self, event):
        if isinstance(event, ShortestPathEvent):
            self.shortest_path(event.id1, event.id2)
        if isinstance(event, CenterEvent):
            self.center()
        if isinstance(event, TSPEvent):
            self.tsp(event)

    def shortest_path(self, id1, id2):
        try:
            dist, path = self.graph_algo.shortest_path(id1, id2)
            print(dist, path)
            self.callback((dist, path))
        except Exception() as e:
            print(e)

    def center(self):
        try:
            node_key, max_dist = self.graph_algo.centerPoint()
            self.callback(('node key is', node_key, '- max dist is:', max_dist))
        except Exception() as e:
            print(e)

    def tsp(self, event):
        try:
            (path, path_cost) = self.graph_algo.TSP(event.nodes_lst)
            self.callback(('full path : ', path, '- path cost is :', path_cost))
        except Exception() as e:
            print(e)
