
# coding: utf-8

import numpy as np
import pandas as pd
import copy
class Dijkstra:
    def __init__(self,nodes,distance):
        self.nodes_org = nodes
        self.nodes = list(range(len(nodes)))
        self.already_search = []
        self.yet_search = list(copy.deepcopy(self.nodes))
        self.distance_matrix = pd.DataFrame(distance,index=self.nodes, columns = self.nodes)
        self.distance_matrix["previous_node"] = 0
        self.distance_array = np.full(len(self.nodes),float("inf"))
        self.distance_array[0] = 0
        
    def fit(self):
        self.search_main(self.nodes[0])
        
    def search_main(self,node):
        self.already_search.append(node)
        for next_node in self.nodes:
            if self.distance_matrix.iat[node,next_node]+self.distance_array[node] < self.distance_array[next_node]:
                self.distance_array[next_node] = self.distance_matrix.iat[node,next_node]+self.distance_array[node]
                self.distance_matrix["previous_node"][next_node] = node 
        self.yet_search.remove(node)
        if len(self.already_search) < len(self.nodes):
            next_search_node = self.yet_search[np.argmin(self.distance_array[self.yet_search])]
            self.search_main(next_search_node)
        
    def get_route(self,node):
        try:
            goal_node = self.nodes_org.index(node)
        except IndexError:
            sys.exit("{} not in nodes".format(node))
        path_node = []
        path_node = self.route(goal_node, path_node)
        result = np.array(self.nodes_org)[path_node]
        return result
        
    def route(self,node,path_node):
        if len(path_node)==0:
            path_node.append(node)
        else:
            path_node.insert(0,node)
        previous_node = self.distance_matrix["previous_node"][node]
        if path_node[0] != 0:
            path_node = self.route(previous_node, path_node)
        return path_node
        
        
        


distance_matrix = np.array([[float("inf"),50,80,float("inf"),float("inf")],
                            [float("inf"),float("inf"),20,25,float("inf")],
                            [float("inf"),float("inf"),float("inf"),10,15],
                            [float("inf"),float("inf"),float("inf"),float("inf"),30],
                            [float("inf"),float("inf"),float("inf"),float("inf"),float("inf")]])
if __name__=="__main__":
    nodes = [1,2,3,4,5]
    test = Dijkstra(nodes,distance_matrix)
    test.fit()
    goal_node = nodes[4]
    print("-----------------route to node {}-----------------".format(goal_node))
    path = test.get_route(goal_node)
    for node_index,node in enumerate(path):
        if node_index == 0:
            print("first node:",node)
        else:
            print("next_node:",node)
    print("distance to node {}：".format(goal_node),test.distance_array[nodes.index(goal_node)])

