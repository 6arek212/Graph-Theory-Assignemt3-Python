from src.impl.graph_algo import GraphAlgo



class ShortestPathEvent:
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

class CenterEvent:
    pass






class UIController:
    def __init__(self, graph_algo: GraphAlgo, callback):
        self.graph_algo = graph_algo
        self.callback = callback

    def on_trigger_event(self, event):
        if isinstance(event, ShortestPathEvent):
            self.shortest_path(event.id1, event.id2)
        if isinstance(event, CenterEvent):
            self.center()

    def shortest_path(self, id1, id2):
        dist, path = self.graph_algo.shortest_path(id1, id2)
        print(dist,path)
        self.callback((dist, path))

    def center(self):
        node_key, max_dist = self.graph_algo.centerPoint()
        self.callback(('node key is' , node_key,'- max dist is:', max_dist))
