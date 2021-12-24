from src.api.GraphInterface import GraphInterface
from src.impl.node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.number_of_edges = 0
        self.mc = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.number_of_edges

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.nodes or id2 not in self.nodes:
            return False

        self.nodes[id1].edges_out[id2] = weight
        self.nodes[id2].edges_in[id1] = weight
        self.number_of_edges = self.number_of_edges + 1
        self.mc = self.mc + 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = Node(node_id, pos)
        self.mc = self.mc + 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False
        self.number_of_edges = self.number_of_edges - (
                len(self.nodes[node_id].edges_in) + len(self.nodes[node_id].edges_out))

        for node in self.nodes[node_id].edges_in.keys():
            self.nodes[node].edges_out.__delitem__(node_id)
        self.nodes.__delitem__(node_id)

        self.mc = self.mc + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if not self.nodes[node_id1].edges_out.__contains__(node_id2):
            return False

        if node_id2 not in self.nodes[node_id1].edges_out:
            return False

        self.nodes[node_id1].edges_out.__delitem__(node_id2)
        self.number_of_edges = self.number_of_edges - 1

        self.mc = self.mc + 1
        return True

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].edges_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].edges_out
