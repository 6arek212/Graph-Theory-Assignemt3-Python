from src.impl.graph_algo import GraphAlgo
from src.impl.graph_factory import getGraphInstance, getConnectedGraphInstance
import unittest
import timeit


def running_time(fun):
    start = timeit.default_timer()
    print(fun())
    stop = timeit.default_timer()
    print('Time: ', (stop - start) * 1000)


class RunningTimeTest(unittest.TestCase):

    def test_shortest_path(self):
        algo = GraphAlgo(getGraphInstance(1000000, 20))
        running_time(lambda: algo.shortest_path(0, 100))
        """
            1000 -> 0.311ms
            10000 -> 2ms
            100000 -> 30ms
            1000000 -> 308ms
        """

    def test_tsp(self):
        algo = GraphAlgo(getGraphInstance(1000000, 20))
        running_time(lambda: algo.TSP([0, 1, 2, 3, 10, 50, 70, 80, 100]))
        """
            1000 -> 5ms
            10000 -> 54ms
            100000 -> 561ms
            1000000 -> 5585ms
        """

    def test_center(self):
        algo = GraphAlgo(getConnectedGraphInstance(1000))
        running_time(lambda: algo.centerPoint())
        """
            100 -> 916ms
            10000 -> *ms
            100000 -> *ms
            1000000 -> *ms
        """

    def test_build_graph(self):
        running_time(lambda: getGraphInstance(1000000, 20))
        """
            1000 -> 7ms
            10000 -> 83ms
            100000 -> 810ms
            1000000 -> 8463ms
        """
