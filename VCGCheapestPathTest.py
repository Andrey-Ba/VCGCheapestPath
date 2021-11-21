import unittest
import networkx as nx
import numpy as np
from PlotGraph import plot_graph

from VCGCheapestPath import vcg_cheapest_path


class MyTestCase(unittest.TestCase):
    def test_example_from_class(self):
        g = nx.Graph()
        g.add_nodes_from(range(1, 5))
        g.add_weighted_edges_from([(1, 2, 3), (1, 3, 5), (1, 4, 10), (2, 3, 1), (2, 4, 4), (3, 4, 1)])
        plot_graph(g)
        vcg_cheapest_path(g, 1, 4)
        self.assertEqual(g[1][2]['cost'], -4)
        self.assertEqual(g[2][3]['cost'], -2)
        self.assertEqual(g[3][4]['cost'], -3)
        self.assertEqual(g[1][3]['cost'], 0)
        self.assertEqual(g[1][4]['cost'], 0)
        self.assertEqual(g[2][4]['cost'], 0)

    def test_custom_graph1(self):
        g = nx.Graph()
        g.add_nodes_from(range(1, 4))
        print(list(range(1, 4)))
        g.add_weighted_edges_from([(1, 2, 1), (1, 3, 2), (2, 3, 7)])
        plot_graph(g)
        vcg_cheapest_path(g, 1, 3)
        # Shortest path: 1->3, cost: 2
        # All edges that are not on shortest path cost 0 as the shortest path without them is the original one.
        self.assertEqual(g[1][2]['cost'], 0)
        self.assertEqual(g[2][3]['cost'], 0)
        # Without edge (1,3) shortest path: 1->2->3, cost: 8, original cost: 0 => edge cost is -8 + 0 = -8
        self.assertEqual(g[1][3]['cost'], -8)

    def test_custom_graph2(self):
        g = nx.Graph()
        g.add_nodes_from(range(1, 7))
        g.add_weighted_edges_from(
            [(1, 2, 1), (1, 3, 2), (2, 3, 7), (3, 4, 5), (3, 5, 2), (4, 5, 5), (4, 6, 4), (5, 6, 3)])
        plot_graph(g)
        vcg_cheapest_path(g, 1, 6)
        # Shortest path: 1->3->5->6, cost: 7
        # All edges that are not on shortest path cost 0 as the shortest path without them is the original one.
        self.assertEqual(g[1][2]['cost'], 0)
        self.assertEqual(g[2][3]['cost'], 0)
        self.assertEqual(g[3][4]['cost'], 0)
        self.assertEqual(g[4][5]['cost'], 0)
        self.assertEqual(g[4][6]['cost'], 0)
        # Without edge (1,3) shortest path: 1->2->3->5->6, cost: 13, original path cost: 5 => edge cost is - 13 + 5 = -8
        self.assertEqual(g[1][3]['cost'], -8)
        # Without edge (3,5) shortest path: 1->3->4->6, cost: 11, original path cost: 5 => edge cost is - 11 + 5 = -6
        self.assertEqual(g[3][5]['cost'], -6)
        # Without edge (5,6) shortest path: 1->3->4->6, cost: 11, original cost: 4 => edge cost is - 11 + 4 = -7
        self.assertEqual(g[5][6]['cost'], -7)

    def test_custom_graph3(self):
        g = nx.Graph()
        g.add_nodes_from(range(1, 6))
        g.add_weighted_edges_from(
            [(1, 2, 5), (1, 3, 1), (2, 3, 3), (2, 4, 1), (3, 4, 5), (4, 5, 5)])
        plot_graph(g)
        vcg_cheapest_path(g, 1, 5)
        # Shortest path: 1->3->2->4->5, cost: 10
        # All edges that are not on shortest path cost 0 as the shortest path without them is the original one.
        self.assertEqual(g[1][2]['cost'], 0)
        self.assertEqual(g[3][4]['cost'], 0)
        # Without edge (1,3) shortest path: 1->2->4->5, cost: 11, original path cost: 9 => edge cost is - 11 + 9 = -2
        self.assertEqual(g[1][3]['cost'], -2)
        # Without edge (2,3) shortest path: 1->2->4->5, cost: 11, original path cost: 7 => edge cost is - 11 + 7 = -4
        self.assertEqual(g[2][3]['cost'], -4)
        # Without edge (2,4) shortest path: 1->3->4->5, cost: 11, original path cost: 9 => edge cost is - 11 + 9 = -2
        self.assertEqual(g[2][4]['cost'], -2)
        # Without edge (4,5) shortest path: None, cost: inf, original path cost: 4 => edge cost is -inf + 4 = -inf
        self.assertEqual(g[4][5]['cost'], -np.inf)


if __name__ == '__main__':
    unittest.main()
