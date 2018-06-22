# coding: utf-8
import numpy as np
import copy
import sys
class BranchSearch:
    
    def __init__(self,opt,cost,max_cost):
        self.opt = opt
        self.cost = cost
        self.max_cost = max_cost
        self.solve = np.zeros(self.opt.shape)
        self.solve_list = []
        self.cost_rate_order = np.argsort(self.opt/self.cost)[::-1]
        self.opt_now = 0
    
    def greedy_algorithm(self):
        for index in self.cost_rate_order:
            if np.sum(self.cost * self.solve) + self.cost[index] > self.max_cost:
                continue
            else:
                self.solve[index] = 1
        self.opt_now = np.sum(self.solve * self.opt)
    
    def branch_kanwa(self,search,index):
        is_last_element_one = False
        is_terminal = False
        while(np.sum(search * self.cost[self.cost_rate_order]) < self.max_cost):
            try:
                index +=1
                search[index]=1
            except IndexError:
                break
        index = min(len(search)-1,index)
        search[index] = 0
        last_element = min((self.max_cost - np.sum(self.cost[self.cost_rate_order]*search))/(self.cost[self.cost_rate_order][index]),1)
        search[index] = last_element
        is_terminal = self.is_terminal(search)
        if not is_terminal and last_element == 1:
            is_last_element_one = True
            self.opt_now = np.sum(search * self.opt[self.cost_rate_order])
            self.solve = copy.deepcopy(search)
        else:
            search[index] = 0
        return (search,is_terminal,is_last_element_one)
        
    def is_terminal(self, solve_array):
        if np.sum(solve_array * self.opt[self.cost_rate_order]) >= self.opt_now:
            return False
        else:
            return True
    
    def branch_main(self,metric = "width"):
        metric_list = ["width","depth"]
        if metric not in metric_list:
            sys.exit("Error:::metric mast be \'width\' or \'depth\'")
        solve = None
        target_index = 0
        self.solve_list = [[0]]
        while(len(self.solve_list)>0):
            if metric == "width":
                solve = self.solve_list.pop(-1)
            else:
                solve = self.solve_list.pop(0)
            target_index = len(solve)
            if target_index:
                solve = np.hstack([solve,np.zeros(self.solve.shape[0]-target_index)])
            else:    
                solve = np.hstack([solve,np.zeros(self.solve.shape[0]-target_index-1)])
            solve[target_index] = 0
            return_1 = self.branch_kanwa(solve,target_index)
            solve, is_terminal, is_last_element_one = return_1[0],return_1[1],return_1[2]
            if is_terminal is False and is_last_element_one is False:
                self.solve_list.append(copy.deepcopy(solve[:target_index+1]))
            solve[target_index+1:] = 0
            solve[target_index] = 1
            return_1 = self.branch_kanwa(solve[:],target_index)
            solve, is_terminal, is_last_element_one = return_1[0],return_1[1],return_1[2]
            if is_terminal is False and is_last_element_one is False:
                self.solve_list.append(copy.deepcopy(solve[:target_index+1]))
            if target_index == len(self.solve)-1:
                break
        return self.opt_now, self.solve                   
                    
if __name__ == "__main__":
    test1 = BranchSearch(np.array([4,5,12,14]),np.array([2,3,5,6]),9)
    test1.greedy_algorithm()
    opt_answer, x_list = test1.branch_main(metric="depth")
    x_name = np.array(["x1","x2","x3","x4"])[test1.cost_rate_order]
    for k,v in enumerate(x_name):
        print("{0}:{1}".format(v,x_list[k]))
    print("score:{}".format(opt_answer))
