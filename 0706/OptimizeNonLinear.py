#conding:utf-8

import numpy as np
import scipy as sp
import sys 
import matplotlib.pyplot as plt

class Problem3:
    
    def __init__(self,x):
        self.x = x
        self.f_history = []
    
        
    def partial(self,x):
        grad_x1 = 2*(x[0,0]-1) + 20*(x[0,0]**2-x[1,0])*2*x[0,0]
        grad_x2 = -20*(x[0,0]**2-x[1,0])
        return np.array([grad_x1,grad_x2]).reshape(-1,1)
    
    def function(self,x):
        first = (x[0,0]-1)**2
        second = 10*(x[0,0]**2-x[1,0])**2
        return first + second
    
    def line_search(self,diff):
        alpha = self.ougon_search(0.00001,10,diff)
        return alpha
        
    def ougon_search(self,minimum,maximum,diff):
        ratio = (-1+np.sqrt(5))/2
        if maximum - minimum < 1e-4:
            ans = minimum
        else:
            l1 = minimum + ratio**2*(maximum - minimum)
            l2 = minimum + ratio*(maximum - minimum)
            if self.function(self.x + l1*diff) > self.function(self.x+l2*diff):
                ans = self.ougon_search(l1,maximum,diff)
            else:
                ans = self.ougon_search(minimum,l2,diff)
        return ans

        
    def sdm(self,alpha = 0.01):
        self.iter_time = 0
        diff = np.float("inf")
        cont = True
        while(cont):
            diff = -self.partial(self.x)
            alpha = self.line_search(diff)
            before_x = self.x
            self.x = self.x + alpha*diff
            self.iter_time += 1
            if self.iter_time > 10000:
                sys.exit("too many iteration {}".format(self.iter_time))
            self.f_history.append(self.function(self.x))
            if np.sum(np.abs(self.x-before_x))>1.0e-4:
                cont = True
            else:
                cont = False
        return self.x,self.iter_time,self.function(self.x)
    
    def cgm(self,alpha=0.01):
        self.iter_time = 0
        cont = True
        before_x = 0
        while(cont):
            if self.iter_time == 0:
                s = -self.partial(self.x)
            else:
                tmp_diff = self.partial(self.x)
                prev_diff = self.partial(before_x)
                s = -tmp_diff + s*np.dot(tmp_diff.T,tmp_diff)/(np.dot(prev_diff.T,prev_diff)+1e-4)
            before_x = self.x
            alpha = self.line_search(s)
            self.x = self.x + alpha*s
            self.iter_time += 1
            if self.iter_time > 1000:
                sys.exit("too many iteration {}".format(self.iter_time))
            self.f_history.append(self.function(self.x))
            if np.sum(np.abs(self.x-before_x))>1.0e-4:
                cont = True
            else:
                cont = False
        return self.x,self.iter_time,self.function(self.x)
    
    def newton(self,alpha = 0.01):
        H = np.eye(2)
        self.iter_time = 0
        cont = True
        while(cont):
            self.iter_time += 1
            s = -np.dot(np.linalg.inv(H),self.partial(self.x))
            before_x = self.x
            alpha = self.line_search(s)
            self.x = self.x + alpha*s
            self.f_history.append(self.function(self.x))
            if self.iter_time > 300:
                print("too many iteration")
                break
            if np.sum(np.abs(self.x-before_x))>1e-4:
                y = self.partial(self.x)-self.partial(before_x)
                first = np.dot(np.dot(np.dot(H,s),s.T),H)/(1e-4+np.dot(np.dot(s.T,H),s))
                second = np.dot(y,y.T)/(1e-4+np.dot(s.T,y))
                H = H - first + second
                cont = True
            else:
                cont = False
        return self.x,self.iter_time,self.function(self.x)

class Problem1:
    
    def __init__(self,x,A,b,c,prob_num):
        self.A = A
        self.b = b
        self.x = x
        self.c = c
        self.iter_time = 0
        self.prob_num = prob_num
        self.f_history = []
        
    def partial(self,x):
        diff = np.dot(self.A,x) + self.b
        return diff
    
    def function(self,x):
        first = np.dot(np.dot(x.T,self.A),x)
        second = np.dot(self.b.T,x)
        return 1/2*first + second + self.c
    
    def line_search(self,diff):
        alpha = self.ougon_search(0.00001,10,diff)
        return alpha
        
    def ougon_search(self,minimum,maximum,diff):
        ratio = (-1+np.sqrt(5))/2
        if maximum - minimum < 1e-4:
            ans = minimum
        else:
            l1 = minimum + ratio**2*(maximum - minimum)
            l2 = minimum + ratio*(maximum - minimum)
            if self.function(self.x + l1*diff) > self.function(self.x+l2*diff):
                ans = self.ougon_search(l1,maximum,diff)
            else:
                ans = self.ougon_search(minimum,l2,diff)
        return ans

        
    def sdm(self,alpha = 0.01):
        self.iter_time = 0
        diff = np.float("inf")
        cont = True
        while(cont):
            diff = -self.partial(self.x)
            if self.prob_num == 1:
                alpha = self.line_search(diff)
            before_x = self.x
            self.x = self.x + alpha*diff
            self.iter_time += 1
            if self.iter_time > 10000:
                sys.exit("too many iteration {}".format(self.iter_time))
            self.f_history.append(self.function(self.x)[0][0])
            if np.sum(np.abs(self.x-before_x))>1.0e-4:
                cont = True
            else:
                cont = False
        return self.x,self.iter_time,self.function(self.x)
    
    def cgm(self,alpha=0.01):
        self.iter_time = 0
        cont = True
        before_x = 0
        while(cont):
            if self.iter_time == 0:
                s = -self.partial(self.x)
            else:
                tmp_diff = self.partial(self.x)
                prev_diff = self.partial(before_x)
                s = -tmp_diff + s*np.dot(tmp_diff.T,tmp_diff)/(np.dot(prev_diff.T,prev_diff)+1e-8)
            if self.prob_num == 1:
                alpha = self.line_search(s)
            before_x = self.x
            self.x = self.x + alpha*s
            self.iter_time += 1
            if self.iter_time > 1000:
                sys.exit("too many iteration {}".format(self.iter_time))
            self.f_history.append(self.function(self.x)[0][0])
            if np.sum(np.abs(self.x-before_x))>1.0e-4:
                cont = True
            else:
                cont = False
        return self.x,self.iter_time,self.function(self.x)
    
    def newton(self,alpha = 0.01):
        H = np.eye(4)
        self.iter_time = 0
        cont = True
        while(cont):
            self.iter_time += 1
            s = -np.dot(np.linalg.inv(H),self.partial(self.x))
            before_x = self.x
            if self.prob_num == 1:
                alpha = self.line_search(s)
            self.x = self.x + alpha*s
            self.f_history.append(self.function(self.x)[0][0])
            if self.iter_time > 300:
                print("too many iteration")
                break
            if np.sum(np.abs(self.x-before_x))>1e-4:
                y = self.partial(self.x)-self.partial(before_x)
                first = np.dot(np.dot(np.dot(H,s),s.T),H)/(1e-4+np.dot(np.dot(s.T,H),s))
                second = np.dot(y,y.T)/(1e-4+np.dot(s.T,y))
                H = H - first + second
                cont = True
            else:
                cont = False
        return self.x,self.iter_time,self.function(self.x)
    
if __name__ == "__main__":
    A1 = np.array([[9,12,-6,-3],
                  [12,41,2,11],
                  [-6,2,24,-8],
                  [-3,11,-8,62]])
    b1 = np.array([-27,-42,32,-23]).reshape(-1,1)
    c1 = 163
    A2 = np.array([[16,8,12,-12],
                   [8,29,16,9],
                   [12,16,29,-19],
                   [-12,9,-19,35]])
    b2 = np.array([7,5,-2,9]).reshape(-1,1)
    c2 = 5
    
    x = np.random.randn(4,1)
    prob1 = Problem1(x,A1,b1,c1,prob_num=1)
    ans1 = prob1.sdm()
    print("----------Problem1 SDM-----------")
    print("Answer x:")
    print(ans1[0])
    print("Answer f(x):",ans1[2])
    print("iteration :",ans1[1])
    
    x = np.random.randn(4,1)
    prob1 = Problem1(x,A1,b1,c1,prob_num=1)
    ans1 = prob1.cgm()
    print("----------Problem1 CGM-----------")
    print("Answer x:")
    print(ans1[0])
    print("Answer f(x):",ans1[2])
    print("iteration :",ans1[1])
    
    x = np.random.randn(4,1)
    prob1 = Problem1(x,A1,b1,c1,prob_num=1)
    ans1 = prob1.newton()
    print("----------Problem1 Newton-----------")
    print("Answer x:")
    print(ans1[0])
    print("Answer f(x):",ans1[2])
    print("iteration :",ans1[1])
    
    x = np.random.randn(4,1)
    prob2 = Problem1(x,A2,b2,c2,prob_num=1)
    ans2 = prob2.sdm()
    print("----------Problem2 SDM-----------")
    print("Answer x:")
    print(ans2[0])
    print("Answer f(x):",ans2[2])
    print("iteration :",ans2[1])

    x = np.random.randn(4,1)
    prob2 = Problem1(x,A2,b2,c2,prob_num=1)
    ans2 = prob2.cgm()
    print("----------Problem2 CGM-----------")
    print("Answer x:")
    print(ans2[0])
    print("Answer f(x):",ans2[2])
    print("iteration :",ans2[1])

    x = np.random.randn(4,1)
    prob2 = Problem1(x,A2,b2,c2,prob_num=1)
    ans2 = prob2.newton()
    print("----------Problem2 Newton-----------")
    print("Answer x:")
    print(ans2[0])
    print("Answer f(x):",ans2[2])
    print("iteration :",ans2[1])

    x = np.random.randn(2,1)
    prob = Problem3(x)
    ans1 = prob.sdm()
    print("----------Problem3 SDM-----------")
    print("Answer x:")
    print(ans1[0])
    print("Answer f(x):",ans1[2])
    print("iteration :",ans1[1])
    
    x = np.random.randn(2,1)
    prob = Problem3(x)
    ans1 = prob.cgm()
    print("----------Problem3 CGM-----------")
    print("Answer x:")
    print(ans1[0])
    print("Answer f(x):",ans1[2])
    print("iteration :",ans1[1])
    
    x = np.random.randn(2,1)
    prob = Problem3(x)
    ans1 = prob.sdm()
    print("----------Problem3 Newton-----------")
    print("Answer x:")
    print(ans1[0])
    print("Answer f(x):",ans1[2])
    print("iteration :",ans1[1])
            
                
                
        