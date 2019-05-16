from os import listdir
from os.path import isfile, join
from dateutil.parser import parse
#import snap
# User IDs and movie IDs collide... sigh
import networkx as nx
import matplotlib.pyplot as plt
from itertools import islice
from sklearn.metrics import mean_squared_error
import numpy as np
import scipy

from networkx.algorithms import bipartite

NETWORKX_MOVIE_BIPARTITE_ID = 0
NETWORKX_USER_BIPARTITE_ID = 1
NETWORKX_MOVIE_CLASS = "movie"
NETWORKX_USER_CLASS = "user"

global graph

def load_file(filename):
    movie_id = -1
    with open(filename) as f:
        for line in islice(f, 1, None):
            split_line = line.strip().split(",")
            movie_id = int(split_line[1])
            user_id = int(split_line[0])
            rating = float(split_line[2])
            timestamp = split_line[3]
            graph.add_node(movie_id, bipartite=NETWORKX_MOVIE_BIPARTITE_ID)
            graph.add_node(user_id, bipartite=NETWORKX_USER_BIPARTITE_ID)
            graph.add_edge(user_id, movie_id, rating=rating)

def project_graph(graph):
    #new_graph_1 is only positive correlation
    #new_graph_2 is negatively correlation between nodes
    new_graph_1 = nx.Graph()
    new_graph_2 = nx.Graph()
    for node, d in graph.nodes(data=True):
        if d['bipartite'] == NETWORKX_MOVIE_BIPARTITE_ID:
        # if d['bipartite'] == NETWORKX_USER_BIPARTITE_ID:
            new_graph_1.add_node(node)
            new_graph_2.add_node(node)
    pairs_done = set()
    count = 0
    for node1 in new_graph_1:
        if count % 10 == 0:
            print count
        for node2 in new_graph_1:
            if (node1, node2) in pairs_done or node1 == node2:
                continue
            node1_ratings = []
            node2_ratings = []
            neighbors = set(graph.neighbors(node1)).intersection(set(graph.neighbors(node2)))


            if len(neighbors)>0:
                for user in neighbors:

                    node1_ratings.append(graph.edge[user][node1]['rating'])
                    node2_ratings.append(graph.edge[user][node2]['rating'])
                # if they are strongly correlated
            if node1_ratings == []:
                continue
            pearson = scipy.stats.pearsonr(node1_ratings, node2_ratings)[0]
            if pearson > .75:
                new_graph_1.add_edge(node1,node2)
                new_graph_2.add_edge(node1, node2, weight = 1)
            if pearson < -.75:
                new_graph_2.add_edge(node1, node2, weight = -1)
        count += 1

    return new_graph_1, new_graph_2


if __name__=="__main__":
    # file=r'ratings.csv'
    # graph=nx.Graph()
    # load_file(file)
    # nx.write_gpickle(graph, "netflix_small.gpickle")
    # nx.draw(graph)
    # plt.show()
    #
    # graph = nx.read_gpickle('netflix_small.gpickle')
    # new_graph_1, new_graph_2 = project_graph(graph)
    # nx.write_gpickle(new_graph_1, "netflix_movie.gpickle")

    # nx.write_edgelist(new_graph_1, "projected_graph_positive_tiny.edgelist")
    # nx.write_edgelist(new_graph_2, "projected_graph_pos_neg_tiny.edgelist")

    movie_graph = nx.Graph()
    movie_graph = nx.read_gpickle('netflix_movie.gpickle')
    edge_list = movie_graph.edges()
    # # #
    node_list = movie_graph.nodes()
    print len(edge_list)  #small:100403 movie_graph:27898
    print len(node_list)  #small:9811   movie_graph:879
    # #
    # write_file = r'movie_edge.csv'
    # with open(write_file, 'w') as f:
    #     f.write("Source,Target,Type,weight\n")
    #     for item in edge_list:
    #         f.write(str(item[0])+','+str(item[1])+",undirected,1\n")

    # print new_graph_1.edges(data=True)
    # nx.draw(new_graph_1)
    # plt.show()



