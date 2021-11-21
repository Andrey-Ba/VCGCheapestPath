import networkx as nx
import numpy as np


def vcg_cheapest_path(graph: nx.Graph, source, target):
    cheapest_path = nx.shortest_path(graph, source, target, weight='weight')
    path_edges = [(cheapest_path[i], cheapest_path[i + 1]) for i in range(len(cheapest_path) - 1)]
    cheapest_path_cost = sum(graph[u][v]['weight'] for (u, v) in path_edges)
    for (u, v) in graph.edges():
        # If the edge is not on shortest path, then the cost is 0
        cost = 0
        # Otherwise the cost is - shortest path without the edge + ( shortest path - cost of the edge )
        if (u, v) in path_edges or (v, u) in path_edges:
            weight = graph[u][v]['weight']
            # Set weight to inf
            graph[u][v]['weight'] = np.inf
            curr_cost_without_uv = -nx.shortest_path_length(graph, source=source, target=target, weight='weight')
            # Set the weight back
            graph[u][v]['weight'] = weight
            cost_of_cheapest_path_without_uv = cheapest_path_cost - graph[u][v]['weight']
            cost = curr_cost_without_uv + cost_of_cheapest_path_without_uv
        graph[u][v]['cost'] = cost
        print('Cost of edge: ', (u, v), ' is ', cost)
