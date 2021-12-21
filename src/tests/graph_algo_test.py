from src.impl.graph_algo import GraphAlgo
import unittest


class test(unittest.TestCase):

    def test_dijkstra(self):
        algo = GraphAlgo()
        algo.load_from_json('../../data/A0.json')
        algo.get_graph().add_node(0)
        algo.get_graph().add_node(1)
        algo.get_graph().add_node(2)
        algo.get_graph().add_edge(0, 1, 1)
        algo.get_graph().add_edge(1, 2, 4)

        self.assertEqual(algo.shortest_path(0, 2), (5, [0, 1, 2]))
        self.assertEqual(algo.shortest_path(0, 1), (1, [0, 1]))

    def test_center(self):
        algo = GraphAlgo()
        algo.load_from_json('../../data/A0.json')
        center = algo.centerPoint()
        self.assertEqual(center , (2, 7.216600510347101))
