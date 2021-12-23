import unittest
from src.impl.DiGraph import DiGraph


def createGraph():
    g = DiGraph()
    for n in range(7):
        g.add_node(n)
    g.add_edge(0, 1, 12)
    g.add_edge(0, 2, 22)
    g.add_edge(1, 2, 9)
    g.add_edge(1, 3, 6)
    g.add_edge(2, 6, 11)
    g.add_edge(4, 5, 6)
    g.add_edge(5, 3, 9)
    g.add_edge(5, 4, 1)
    g.add_edge(6, 0, 5)
    return g


class DiGraphTest(unittest.TestCase):
    # testing remove Node
    def test_removeNode(self):
        g = createGraph()
        nodes = g.get_all_v().copy()
        g.remove_node(5)
        nodes.pop(5)
        self.assertDictEqual(nodes, g.get_all_v())
        self.assertEqual(g.e_size(), 6)
        self.assertEqual(g.v_size(), 6)
        g.remove_node(6)
        nodes.pop(6)
        self.assertDictEqual(nodes, g.get_all_v())
        self.assertEqual(g.e_size(), 4)
        self.assertEqual(g.v_size(), 5)

    # testing remove Edge
    def test_removeEdge(self):
        g = createGraph()
        out_EdgesV2 = g.all_out_edges_of_node(2).copy()
        g.remove_edge(2, 6)
        out_EdgesV2.pop(6)
        self.assertDictEqual(out_EdgesV2, g.all_out_edges_of_node(2))
        self.assertNotEqual(g.e_size(), 7)

    # adding edge and node already existed
    def test_addNodeAndEdgeEROR(self):
        g = createGraph()
        self.assertFalse(g.add_edge(0, 1, 12))
        self.assertFalse(g.add_edge(6, 0, 5))
        self.assertFalse(g.add_edge(5, 3, 9))
        self.assertFalse(g.add_node(4))
        self.assertFalse(g.add_node(1))
        self.assertFalse(g.add_node(2))

    # testing size of graph
    def test_sizeOfGraph(self):
        g = createGraph()
        self.assertEqual(g.v_size(), 7)
        self.assertEqual(g.e_size(), 9)
        g.remove_edge(2, 6)
        g.remove_node(1)
        self.assertEqual(g.v_size(), 6)
        self.assertEqual(g.e_size(), 5)

    # testing in and out edges
    def test_inOutEdges(self):
        g = createGraph()
        g.add_node(7)
        g.add_edge(6, 7, 2)
        self.assertTrue(7 in g.all_out_edges_of_node(6))
        self.assertFalse(6 in g.all_out_edges_of_node(7))
        temp = g.all_in_edges_of_node(7)[6]
        self.assertEqual(temp, 2)
        self.assertEqual(temp, g.all_out_edges_of_node(6)[7])

    # testing mode counter
    def test_mc(self):
        g = createGraph()
        self.assertEqual(g.mc, 16)


if __name__ == '__main__':
    unittest.main()
