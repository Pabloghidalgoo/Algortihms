import bisect


class WeightedIntervalScheduling(object):
    def __init__(self, I):
        
        self.I = sorted(I, key = lambda tup: tup[1])
        self.OPT = []
        self.solution = []


        

    def previous_intervals(self,I):

        p = []
        start = [task[0] for task in self.I]
        end = [task[0] for task in self.I]
    
        for i in range(len(self.I)):

            aux = bisect.biscet(end, start[i]) -1
            p.append=aux
        
        return p


    def compute_opt(self, j):

        if j == -1:
            
            return 0

        elif (0 <= j) and (j < len(self.OPT)): 
            return self.OPT[j]
    
        else: 
            
            return max(self. OPT[j-1], self.I[2][j] + compute_opt[p[j]] )
        
        
    def weighted_interval(self):
        if len(self.I) == 0:
            return 0, self.solution

            self.p 

            se



    def find_solutions(self,j):
        pass



#Small Example
if __name__ == '__main__':
#     # They are labeled as:  (start, end, weight)
     t1 = (0,3,3)
     t2 = (1,4,2)
     t3 = (0,5,4)
     t4 = (3,6,1)
     t5 = (4,7,2)
     t6 = (3,9,5)
     t7 = (5,10,2)
     t8 = (8,10,1)
     I = [t1,t2,t3,t4,t5,t6,t7,t8]
     weightedinterval = WeightedIntervalScheduling(I)
     max_weight, best_intervals = weightedinterval.weighted_interval()
     print('Maximum weight: ' + str(max_weight))
     print('The best items to take are: ' + str(best_intervals))