import heapq
import random

from src.api.GraphAlgoInterface import GraphAlgoInterface
from src.api.GraphInterface import GraphInterface
from src.impl.DiGraph import DiGraph
from typing import List
import json
import sys
import matplotlib.pyplot as plt
from numpy import inf
import numpy as np

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        json_graph = DiGraph()
        try:
            with open(file_name) as json_file:
                # dic of json
                json_data = json.load(json_file)
            for n in json_data["Nodes"]:
                key = n["id"]
                if "pos" not in n:
                    json_graph.add_node(key)
                else:
                    x, y, z = map(float, str(n["pos"]).split(","))
                    pos = (x, y, z)
                    json_graph.add_node(key, pos)
            for edge in json_data["Edges"]:
                json_graph.add_edge(edge["src"], edge["dest"], edge["w"])
            self.graph = json_graph
            return True
        except Exception as e:
            print("loading from json FAILED!! " + str(e))
            return False

    def save_to_json(self, file_name: str) -> bool:

        to_json = {"Edges": [], "Nodes": []}

        with open(file_name, 'w') as json_file:
            try:
                for n in self.graph.get_all_v().values():
                    if n.pos is None:
                        to_json["Nodes"].append({"id:", n.key})
                    else:
                        to_json["Nodes"].append({"pos": f"{n.pos[0]},{n.pos[1]},{n.pos[2]}", "id": n.key})

                for n in self.graph.get_all_v().keys():
                    out_edges = self.graph.all_out_edges_of_node(n)
                    for key_out_node in out_edges:
                        to_json["Edges"].append({"src": n, "w": out_edges[key_out_node], "dest": key_out_node})

                json.dump(to_json, json_file, indent=2)
                return True
            except Exception as e:
                print("saving to json FAILED!! " + str(e))
                return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):

        if self.graph is None or self.graph.Nodes.get(id1) is None or self.graph.Nodes.get(id2) is None:
            return float("inf"), []

        dist = {}
        for i in self.graph.Nodes.keys():
            dist[i] = inf
        previous = {id1: -1}
        dist[id1] = 0
        queue = []
        # priority queue taking the min
        heapq.heappush(queue, (0, id1))

        while queue:
            # taking the second element in tuple
            curr_min_node = heapq.heappop(queue)[1]

            if curr_min_node == id2:
                break

            for neighbour, w in self.graph.all_out_edges_of_node(curr_min_node).items():

                currWight = dist[curr_min_node] + w

                if currWight < dist[neighbour]:
                    dist[neighbour] = currWight
                    previous[neighbour] = curr_min_node
                    heapq.heappush(queue, (dist[neighbour], neighbour))

        shortestPath = []
        curr = id2
        if dist[id2] == inf:
            return inf, []

        while curr != -1:
            shortestPath.insert(0, curr)
            curr = previous[curr]

        return dist[id2], shortestPath

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
            for node in targetTo:
                if node in tmp:
                    targetTo.remove(node)

            for node in tmp:
                res.append(node)
            if targetTo:
                src = dest
                dest = targetTo[0];

        return res, self.getPathCost(res)

    def getPathCost(self, list) -> float:
        cost = 0
        for i in range(len(list) - 1):
            cost += self.graph.all_out_edges_of_node(i)[i + 1]

        return cost

    def centerPoint(self) -> (int, float):
         pass


   #random.uniform(a, b)¶ -> Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
    def plot_graph(self) -> None:
        my_graph = self.graph
        if my_graph is not None:
            #to check if random point is existed
            existed_points = {}
            #go throw all nodes in the graph
            for node in my_graph.get_all_v().values():
                #check if there is node with no pos to give it new random pos
                if node.pos is None:
                    while True:
                        x = np.random.uniform(1, 100)
                        y = np.random.uniform(1, 100)
                        if x not in existed_points:
                            existed_points[x] = {}
                        if existed_points.get(x).get(y) is None:
                            existed_points[x][y] = node.key
                            break
                    #after choosing two random points set the pos
                    node.setPos((x,y , 0))

                plt.plot(node.pos[0], node.pos[1], 'bo')
                plt.text(node.pos[0], node.pos[1], node.key, fontsize=11,
                         color='red')
            #go throw all nodes and draw arrow edges for all out edges of the node
            for node1 in my_graph.get_all_v().values():
                for node2 in self.graph.all_out_edges_of_node(node1.key).keys():
                    pos_x1 = node1.pos[0]
                    pos_y1 = node1.pos[1]
                    pos_x2 = self.graph.Nodes.get(node2).pos[0]
                    pos_y2 = self.graph.Nodes.get(node2).pos[1]
                    plt.arrow(pos_x1, pos_y1, (pos_x2 - pos_x1), (pos_y2 - pos_y1), length_includes_head=True,
                              head_width=0.0002, width=0)


            plt.show()