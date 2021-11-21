import networkx as nx
from matplotlib import pyplot as plt


def plot_graph(g: nx.Graph):
    pos = nx.spring_layout(g, seed=1)
    nx.draw_networkx(g, pos)
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    plt.show()