import heapq

from src.api.GraphInterface import GraphInterface
from src.api.GraphAlgoInterface import GraphAlgoInterface
from typing import List
import json
from src.impl.di_graph import DiGraph
from src.impl.node import Node
import numpy as np
import matplotlib.pyplot as plt


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: GraphInterface = DiGraph()):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def path_cost(self, list) -> float:
        cost = 0
        for i in range(len(list) - 1):
            cost += self.graph.all_out_edges_of_node(i)[i + 1]

        return cost

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        targetTo = node_lst.copy()
        res = []
        src = targetTo[0]
        if len(node_lst) == 1:
            return self.shortest_path(src, src)
        dest = targetTo[1]
        while targetTo:

            if (res and res[len(res) - 1] == src):
                res.pop(len(res) - 1)

            tmp = self.shortest_path(src, dest)[1]
            # targetTo = [node for node in targetTo if node not in tmp]
            for node in targetTo:
                if node in tmp:
                    targetTo.remove(node)

            for node in tmp:
                res.append(node)
            # res = [node for node in tmp]
            if targetTo:
                src = dest
                dest = targetTo[0]

        return res, self.path_cost(res)

    def max_dest(self, node: Node):
        max_dst = float('-inf')
        for node_key in self.graph.get_all_v().keys():
            path_dist = self.shortest_path(node.key, node_key)[0]
            if path_dist == float('inf'):
                return None;
            if path_dist != float('inf') and path_dist > max_dst:
                max_dst = path_dist
        return max_dst

    def centerPoint(self) -> (int, float):
        min = float('inf')
        picked_node = None

        for node in self.get_graph().get_all_v().values():
            dist = self.max_dest(node)
            if dist is None:
                return -1, float('inf')
            if dist < min:
                picked_node = node
                min = dist
        return picked_node.key, min

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        nodes = self.graph.get_all_v()
        if id1 not in nodes or id2 not in nodes:
            return float('inf'), []

        for node in nodes.values():
            node.tag = Node.WHITE
            if node.key == id1:
                node.w = 0
            else:
                node.w = float('inf')
        dist = {}
        queue = []
        heapq.heappush(queue, (0, id1))

        while queue:
            node = nodes[heapq.heappop(queue)[1]]

            for (adj, w) in node.edges_out.items():
                if nodes[adj].tag == Node.WHITE:
                    if node.w + w < nodes[adj].w:
                        nodes[adj].w = node.w + w
                        dist[adj] = node.key
                    heapq.heappush(queue, (nodes[adj].w, adj))
            node.tag = Node.BLACK

        for node in nodes.values(): node.tag = Node.WHITE
        if nodes[id2].w == float('inf'):
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
        my_graph = self.graph
        if my_graph is not None:
            # to check if random point is existed
            existed_points = {}
            # go throw all nodes in the graph
            for node in my_graph.get_all_v().values():
                # check if there is node with no pos to give it new random pos
                if node.pos is None:
                    while True:
                        x = np.random.uniform(1, 100)
                        y = np.random.uniform(1, 100)
                        if x not in existed_points:
                            existed_points[x] = {}
                        if existed_points.get(x).get(y) is None:
                            existed_points[x][y] = node.key
                            break
                    # after choosing two random points set the pos
                    node.pos = (x, y, 0)

                plt.plot(node.pos[0], node.pos[1], 'bo')
                plt.text(node.pos[0], node.pos[1], node.key, fontsize=11,
                         color='red')
            # go throw all nodes and draw arrow edges for all out edges of the node
            for node1 in my_graph.get_all_v().values():
                for node2 in self.graph.all_out_edges_of_node(node1.key).keys():
                    pos_x1 = node1.pos[0]
                    pos_y1 = node1.pos[1]
                    pos_x2 = self.graph.get_all_v().get(node2).pos[0]
                    pos_y2 = self.graph.get_all_v().get(node2).pos[1]
                    plt.arrow(pos_x1, pos_y1, (pos_x2 - pos_x1), (pos_y2 - pos_y1), length_includes_head=True,
                              head_width=0.0002, width=0)

            plt.show()

    def load_from_json(self, file_name: str) -> bool:
        json_graph = DiGraph()
        try:
            with open(file_name) as json_file:
                json_data = json.load(json_file)
                for node in json_data['Nodes']:
                    if 'pos' in node:
                        x, y, z = map(float, str(node["pos"]).split(","))
                        json_graph.add_node(node['id'], (x, y, z))
                    else:
                        json_graph.add_node(node['id'])
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
