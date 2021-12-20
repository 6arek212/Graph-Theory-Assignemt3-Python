import sys
from src.api.GraphInterface import GraphInterface
from src.api.GraphAlgoInterface import GraphAlgoInterface
from typing import List
import json
from src.impl.di_graph import DiGraph
from src.impl.node import Node
import heapdict


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: GraphInterface = DiGraph()):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def max_dest(self, node: Node):
        max = float('-inf')
        for other_node in self.graph.get_all_v().values():
            path_dist = self.shortest_path(other_node.key, node.key)[0]
            if other_node.key != node.key and path_dist > max:
                max = path_dist
        return max

    def centerPoint(self) -> (int, float):
        min = float('inf')
        picked_node = Node

        for node in self.get_graph().get_all_v().values():
            dist = self.max_dest(node)
            if dist < min:
                picked_node = node
                min = dist

        return picked_node.key, min

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        nodes = self.graph.get_all_v()
        if not nodes.__contains__(id1) or not nodes.__contains__(id2) or id1 == id2:
            return float('inf'), []

        for node in nodes.values():
            node.tag = Node.WHITE
            if node.key == id1:
                node.w = 0
            else:
                node.w = float('inf')
        dist = {}
        pq = heapdict.heapdict()
        pq[nodes[id1]] = nodes[id1].w
        while len(pq) > 0:
            node = pq.popitem()[0]
            for (adj, w) in node.edges_out.items():
                if nodes[adj].tag == Node.WHITE and node.w + w < nodes[adj].w:
                    nodes[adj].w = node.w + w
                    pq[nodes[adj]] = nodes[adj].w
                    dist[adj] = node.key
            node.tag = Node.BLACK

        for node in nodes.values(): node.tag = Node.WHITE
        if nodes[id2].w == sys.maxsize:
            return float('inf'), []

        path = []
        start = id2
        path.append(start)
        while start != id1:
            path.append(dist[start])
            start = dist[start]
        path.reverse()
        return nodes[id2].w, path

    def plot_graph(self) -> None:
        pass

    def load_from_json(self, file_name: str) -> bool:
        json_graph = DiGraph()
        try:
            with open(file_name) as json_file:
                json_data = json.load(json_file)
                for node in json_data['Nodes']:
                    x, y, z = map(float, str(node["pos"]).split(","))
                    json_graph.add_node(node['id'], (x, y, z))
                for edge in json_data['Edges']:
                    json_graph.add_edge(edge['src'], edge['dest'], edge['w'])
        except Exception as e:
            print('load failed', e)
            return False
        self.graph = json_graph
        return True

    def save_to_json(self, file_name: str) -> bool:
        json_graph = {"Edges": [], "Nodes": []}
        try:
            with open(file_name, 'w') as json_file:
                for (key, node) in self.graph.get_all_v().items():
                    for (node_dest, w) in node.edges_out.items():
                        json_graph['Edges'].append({
                            "src": node.key,
                            "w": w,
                            "dest": node_dest
                        })
                    json_graph['Nodes'].append(node.__dict__())
                json.dump(json_graph, json_file, indent=2)
                return True

        except Exception as e:
            print("saving to json FAILED!!", e)
        return False


if __name__ == '__main__':
    algo = GraphAlgo()
    algo.load_from_json('../../data/A0.json')
    print(algo.centerPoint())