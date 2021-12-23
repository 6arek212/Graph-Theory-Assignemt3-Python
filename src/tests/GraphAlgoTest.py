import unittest
from src.impl.GraphAlgo import GraphAlgo
from src.impl.DiGraph import DiGraph



class algoGraphTest(unittest.TestCase):


       def test_shortest_path_test(self):
           g = DiGraph()
           g.add_node(1)
           g.add_node(2)
           g.add_node(3)
           g.add_node(4)
           g.add_node(5)
           g.add_node(6)
           g.add_edge(1, 2, 2)
           g.add_edge(1, 3, 4)
           g.add_edge(2, 4, 7)
           g.add_edge(2, 3, 1)
           g.add_edge(3, 5, 3)
           g.add_edge(5, 4, 2)
           g.add_edge(4, 6, 1)
           g.add_edge(5, 6, 6)
           g_a = GraphAlgo(g)
           s = g_a.shortest_path(1, 5)
           self.assertEqual((6, [1, 2, 3, 5]), s)
       #test save and load
       def test_save_load(self):
           g = DiGraph()
           g.add_node(1,(42.4,32.3,0))
           g.add_node(2,(41.4,34.3,0))
           g.add_node(3,(42,33,0))
           g.add_node(4,(41.4,32.3,0))
           g.add_edge(1, 2, 3)
           g.add_edge(1, 3, 2)
           g.add_edge(2, 3, 1)
           g.add_edge(4, 1, 6)
           g_a1 = GraphAlgo(g)
           g_a1.save_to_json("../data/graph.json")
           g_a2 = GraphAlgo()
           g_a2.load_from_json("../data/graph.json")
           g2 = g_a2.get_graph()
           self.assertIsNotNone(g2)
           self.assertEqual(4, g2.e_size())
           g2.add_node(6 ,(23,21.2,0))
           self.assertNotEqual(g2.v_size(), g.v_size())

       def test_TSP(self):
           pass

       def test_Center(self):
           pass






if __name__ == '__main__':
    unittest.main()