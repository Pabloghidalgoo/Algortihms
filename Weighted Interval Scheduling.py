import bisect

class WeightedIntervalScheduling(object):
    def __init__(self, I):
        # Sort the intervals by their finish times
        self.I = sorted(I, key=lambda tup: tup[1])
        self.OPT = []
        self.solution = []

    def previous_intervals(self):
        p = [0] * len(self.I)
        end = [task[1] for task in self.I]

        for i in range(len(self.I)):
            # Find the rightmost interval that doesn't conflict
            index = bisect.bisect_right(end, self.I[i][0]) - 1
            p[i] = index
        
        return p

    def compute_opt(self, j):
        if j == -1:
            return 0
        elif j < len(self.OPT):
            return self.OPT[j]
        else:
            # Take the max of not including j or including j
            without_j = self.compute_opt(j - 1)
            with_j = self.I[j][2] + self.compute_opt(self.p[j])
            opt_j = max(without_j, with_j)
            return opt_j
        
    def find_solution(self, j):
        if j == -1:
            return
        if self.I[j][2] + self.OPT[self.p[j]] > self.OPT[j - 1]:
            self.solution.append(self.I[j])
            self.find_solution(self.p[j])
        else:
            self.find_solution(j - 1)

    def weighted_interval(self):
        if len(self.I) == 0:
            return 0, self.solution

        self.p = self.previous_intervals()

        for j in range(len(self.I)):
            opt_j = self.compute_opt(j)
            self.OPT.append(opt_j)
        
        self.find_solution(len(self.I) - 1)

        return self.OPT[-1], self.solution[::-1]



if __name__ == '__main__':
    # They are labeled as:  (start, end, weight)
    t1 = (0, 3, 3)
    t2 = (1, 4, 2)
    t3 = (0, 5, 4)
    t4 = (3, 6, 1)
    t5 = (4, 7, 2)
    t6 = (3, 9, 5)
    t7 = (5, 10, 2)
    t8 = (8, 10, 1)
    I = [t1, t2, t3, t4, t5, t6, t7, t8]
    weighted_interval = WeightedIntervalScheduling(I)
    max_weight, best_intervals = weighted_interval.weighted_interval()
    print('Maximum weight: ' + str(max_weight))
    print('The best items to take are: ' + str(best_intervals))
