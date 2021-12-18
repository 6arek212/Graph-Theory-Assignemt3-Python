from src.api.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.edges = {}
        self.nodes = {}
        self.mc = 0

    def __init__(self, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.mc = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.edges.__contains__((id1, id2)):
            return False
        self.edges[(id1, id2)] = Edge(id1, id2, weight)

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.__contains__((node_id)):
            return False
        #add it


    def remove_node(self, node_id: int) -> bool:
        self.nodes.__delitem__(node_id)
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        self.edges.__delitem__((node_id1,node_id2))
        return True
