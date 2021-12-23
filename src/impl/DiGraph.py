from src.api.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.mc = 0;
        #this list just for printing edges
        self.Edges = []
        self.Nodes = dict()
        self.nodes_counter = 0
        self.edge_counter = 0

    def v_size(self) -> int:
        return self.nodes_counter

    def e_size(self) -> int:
        return self.edge_counter

    def get_all_v(self) -> dict:
        return self.Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
          if self.Nodes is None:
              return {}

          return  self.Nodes.get(id1).edges_in



    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.Nodes.get(id1) is None:
            return {}

        return self.Nodes.get(id1).edges_out

    def get_mc(self) -> int:
        return  self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if (self.Nodes.get(id1) is None) or (self.Nodes.get(id2) is None) or (id1 == id2)or self.Nodes.get(id1).edges_out.get(id2) is not None:
            return  False
        self.Edges.append((id1 , id2 , weight))
        #update edges out for id1
        self.Nodes.get(id1).edges_out[id2] = weight
        #update edges in for id2
        self.Nodes.get(id2).edges_in[id1] = weight
        self.edge_counter+=1
        self.mc +=1
        return  True


    def add_node(self, node_id: int, pos: tuple = None) -> bool:

        if self.Nodes.get(node_id) is not None:
            return False

        new_Node = NodeData(node_id , pos)
        self.Nodes[node_id] = new_Node
        self.mc+=1
        self.nodes_counter+=1
        return True


    def remove_node(self, node_id: int) -> bool:
        if self.Nodes.get(node_id) is None:
            return False

        for i in self.Nodes.get(node_id).edges_in.keys():
            self.Nodes.get(i).edges_out.pop(node_id)
            self.edge_counter-=1

        for i in self.Nodes.get(node_id).edges_out.keys():
            self.Nodes.get(i).edges_in.pop(node_id)
            self.edge_counter-=1

        self.mc +=1
        self.nodes_counter-=1
        self.Nodes.pop(node_id)

        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        #check if nodes are existed and if there is edge  out in the first node
        if self.Nodes.get(node_id1) is not None and self.Nodes.get(node_id2) is not None and self.Nodes.get(node_id1). \
                edges_out.get(node_id2) is not None:
            self.Nodes.get(node_id1).edges_out.pop(node_id2)
            self.Nodes.get(node_id2).edges_in.pop(node_id1)
            self.mc += 1
            self.edge_counter -= 1
            return True
        return False
    def __str__(self):
        return f"Nodes: {self.Nodes}\nEdges: {self.Edges}"

    def __repr__(self):
        return f"Nodes: {self.Nodes}\nEdges: {self.Edges}"


class NodeData:

    def __init__(self, key, pos=None):
        self.key = key
        # tuple pos
        self.pos = pos
        self.edges_in = {}
        self.edges_out = {}


    def setPos(self , pos:tuple):
        self.pos = pos

    def __str__(self):
        return f"id {self.key} - pos : {self.pos}"

    def __repr__(self):
        return f"id {self.key} - pos : {self.pos}"
