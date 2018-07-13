import numpy as np
import pandas as pd

class Salesman:
    def __init__(self,distance, nodes):
        self.distance = pd.DataFrame(distance,index=range(len(nodes)), columns=range(len(nodes)))
        self.nodes= nodes
        self.zantei_kai = float("inf")
        self.zantei_route = None
        self.yet_search_part = []
        self.part = []
        
    def __getKanwaValue(self,route):
        already_in = []
        already_out = []
        distance_now = 0
        distance = self.distance.copy()
        if len(route) > 1:
            if route[-1] == 0:
                distance.iat[route[-3],route[-2]] = float("inf")
                route_use = route[:-2]
            else:
                route_use = route[:-1]
        else:
            route_use = route
        for node_id,node in enumerate(route_use):
            if node_id < len(route_use) - 1:
                already_out.append(node)
                already_in.append(route_use[node_id+1])
                print("node:",node)
                print("route_use:",route_use[node_id+1])
                distance_now += self.distance.iat[node,route_use[node_id+1]]
        distance = self.distance.copy()
        distance.iloc[already_out,:] = float("inf")
        distance.iloc[:,already_in] = float("inf")
        distance_min_out = np.min(distance,axis=1).reshape(-1,1)
        distance = pd.DataFrame(distance.values - distance_min_out,index=range(len(self.nodes)), columns=range(len(self.nodes)))
        distance_min_in = np.min(distance,axis=0).reshape(1,-1)
        distance = pd.DataFrame(distance.values - distance_min_in,index=range(len(self.nodes)), columns=range(len(self.nodes)))
        distance_max_value = np.sum(distance_min_out) + np.sum(distance_min_in) + distance_now
        return distance_max_value, distance
    
    def __search(self):
        # self.yet_search_part は2個以上のノードを入れる
        for route in self.yet_search_part:
            self.yet_search_part.remove(route)
            if len(route) == self.distance.shape[0]+1 and route[-1] == 1:
                is_closed = self.__check_circkit(route)
                if is_closed and is_closed < self.zantei_kai:
                    self.zantei_kai = is_closed
                    self.zantei_route = route
            max_value, distance = self.__getKanwaValue(route)
            print("max_value:",max_value)
            print("distance:",distance)
            print("zanteikai:",self.zantei_kai)
            if max_value > self.zantei_kai:
                continue
            else:
                next_node = np.argmin(distance.iloc[route[-1],:])
                route.append(next_node)
                self.yet_search_part.append(route+[next_node,0])
                self.yet_search_part.append(route+[next_node,1])
                
    def __check_circkit(self,route):
        max_value,distance = self.__getKanwaValue(route)
        next_node = np.argmin(distance.iloc[route[-1],:],axis=1)
        if next_node == route[0]:
            return max_value
        else:
            return False
        
    def getAnswer(self):
        self.yet_search_part.append([0])
        self.__search()
        
if __name__=="__main__":
    distance_matrix = [[float("inf"),21,7,13,15],
                       [11,float("inf"),19,12,25],
                       [15,24,float("inf"),13,5],
                       [6,17,9,float("inf"),22],
                       [26,6,11,5,float("inf")]]
    nodes = [0,1,2,3,4]
    salesman = Salesman(distance=distance_matrix, nodes=nodes)
    salesman.getAnswer()