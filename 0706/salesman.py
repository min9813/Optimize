import numpy as np
import pandas as pd

class Salesman:
    def __init__(self,distance, nodes):
        self.distance = pd.DataFrame(distance,index=range(len(nodes)), columns=range(len(nodes)))
        self.nodes= nodes
        self.zantei_kai = float("inf")
        self.zantei_route = None
        self.yet_search_part = []
        
    def __getKanwaValue(self,route):
        print("-------get kanwa with route:{}----------".format(route))
        already_in = []
        already_out = []
        distance_now = 0
        distance = self.distance.copy()
        print("before distance:",distance)
        if len(route) > 1:
            if route[-1] == 0:
                print("route:",route)
                distance.iat[route[-3],route[-2]] = float("inf")
                print("replaced distance ooo:")
                print(distance)
                route_use = route[:-2]
            else:
                route_use = route[:-1]
        else:
            route_use = route
        print("route use:",route_use)
        for node_id,node in enumerate(route_use):
            if node_id < len(route_use) - 1:
                already_out.append(node)
                already_in.append(route_use[node_id+1])
                print("node:",node)
                print("route_use:",route_use[node_id+1])
                distance_now += self.distance.iat[node,route_use[node_id+1]]
        print("distance now:",distance_now)
        distance = distance.drop(already_out,axis=0)
        distance = distance.drop(already_in,axis=1)
        print("replaced distance 1:")
        print(distance)
        distance_min_out = np.min(distance.values,axis=1).reshape(-1,1)
        print("distance_min_out:")
        print(distance_min_out)
        distance = pd.DataFrame(distance.values - distance_min_out,index=distance.index, columns=distance.columns)
        print("replaced distance 2:")
        print(distance)
        distance_min_in = np.min(distance.values,axis=0).reshape(1,-1)
        print("distance_min_in:")
        print(distance_min_in)
        distance = pd.DataFrame(distance.values - distance_min_in,index=distance.index, columns=distance.columns)
        print("replaced distance 3:")
        print(distance)
        distance_max_value = np.sum(distance_min_out) + np.sum(distance_min_in) + distance_now
        return distance_max_value, distance, route_use
    
    def __search(self):
        # self.yet_search_part は2個以上のノードを入れる
        while len(self.yet_search_part)>0:
            route = self.yet_search_part.pop(-1)
            print("-------------new route:{}------------".format(route))
            if len(route) == self.distance.shape[0]+1 and route[-1]==1:
                print("going to check closed")
                is_closed = self.__check_circkit(route)
                print("is closed:",is_closed)
                if is_closed is not False and is_closed < self.zantei_kai:
                    print("update zantei kai")
                    self.zantei_kai = is_closed
                    self.zantei_route = route[:-1] + [0]
                    continue
            max_value, distance, route = self.__getKanwaValue(route)
            print("max_value:",max_value)
            print("distance:",distance)
            print("zanteikai:",self.zantei_kai)
            if max_value > self.zantei_kai:
                continue
            else:
                print("route:",route)
                print("distance raw:",distance.loc[route[-1],:])
                next_node = np.argmin(distance.loc[route[-1],:])
#                 print("min index:",min_index)
#                 next_node = distance.columns[min_index]
                print("next_node:",next_node)
                route.append(next_node)
                if next_node == 0 and len(route) < len(self.nodes)+1:
                    print("yet search:",self.yet_search_part)
                    self.yet_search_part.append(route+[0])
                    print("yet search:",self.yet_search_part)
                else:
                    print("yet search:",self.yet_search_part)
                    self.yet_search_part.append(route+[0])
                    print("yet search:",self.yet_search_part)
                    self.yet_search_part.append(route+[1])
                    print("yet search:",self.yet_search_part)
                
    def __check_circkit(self,route):
        max_value,distance,route = self.__getKanwaValue(route)
        print("max value:",max_value)
        print("distance:",distance)
        print("route:",route)
        print("loc:",distance.loc[route[-1],:])
        next_node = np.argmin(distance.loc[route[-1],:],axis=1)
        print("next node:",next_node)
        if next_node == route[0]:
            print("yes")
            return max_value
        else:
            return False
        
    def draw_route(self):
        route = ""
        for node in map(str,self.zantei_route):
            route += node + ">"
        print("-----route-----")
        print(route[:-1])
        print("-----distance-----")
        print(self.zantei_kai)
        
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
    salesman.draw_route()
