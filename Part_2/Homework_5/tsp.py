import numpy as np
from math import sqrt, factorial
from itertools import combinations
from copy import deepcopy
import gc

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def n_choose_k(n, k):
    """Computes n choose k."""

    if n < k:
        return 0
    else:
        return factorial(n) / factorial(k) / factorial(n - k)


def n_choose_k_table(num_of_cities):
    """Computes a dictionary which caches all possible n choose k computations."""
    table = {}
    for n in range(num_of_cities):
        for k in range(1, n + 2):
            table[(n, k)] = n_choose_k(n, k)
    return table


def comb_index(comb_start, comb, nck_table):
    """
    Computes a dense index for a given subset 'comb' in all subsets that have
    the same number of elements as 'comb'. 'comb_start' is the minimum element in
    the set from which subset 'comb' is obtained.

    http://en.wikipedia.org/wiki/Combinatorial_number_system
    copied from https://github.com/ChuntaoLu/Algorithms-Design-and-Analysis
      comb        index
    (1, 2, 3)  -->  0
    (1, 2, 4)  -->  1
    (1, 2, 5)  -->  4
    (1, 3, 4)  -->  2
    (1, 3, 5)  -->  5
    (1, 4, 5)  -->  7
    (2, 3, 4)  -->  3
    (2, 3, 5)  -->  6
    (2, 4, 5)  -->  8
    (3, 4, 5)  -->  9
    """
    return sum([nck_table[(y - comb_start, x + 1)]
                for x, y in enumerate(comb)])

class TSP:
    def __init__(self, txt_name):
        self.n_cities = 0
        self.cities = []
        self.read_txt(txt_name)
        pass

    def read_txt(self, txt_name):
        with open(txt_name) as f:
            first_line = f.readline().rstrip("\n").split(" ")
            self.n_cities = int(first_line[0])
            for line in f:
                str_list = line.rstrip("\n").split(' ')
                self.cities.append(tuple(map(float, str_list)))

    def solve_tsp(self):
        INF = 99999999
        city_index = [i for i in range(0, self.n_cities)]
        costs = {}
        new_costs = {}
        nck_table = n_choose_k_table(self.n_cities)
        print("Initialization done!")
        for m in range(2, self.n_cities + 1):  # sub problem size including 0
            print("solving subproblem size ", m)
            for other in combinations(city_index[1:], m - 1):
                s = [0, *other]
                for j in s:
                    if j == 0:
                        continue
                    smaller_s = deepcopy(s)
                    smaller_s.remove(j)
                    for k in smaller_s:
                        cost_k_des = []
                        if k != 0:
                            smaller_c_index = comb_index(0, tuple(smaller_s), nck_table)
                            cost_k_des.append(costs[smaller_c_index, k] + euclidean_distance(self.cities[k], self.cities[j]))
                        else:
                            if smaller_s == [0]:
                                cost_k_des.append(0 + euclidean_distance(self.cities[0], self.cities[j]))
                            else:
                                cost_k_des.append(INF)
                    new_c_index = comb_index(0, tuple(s), nck_table)
                    new_costs[(new_c_index, j)] = min(cost_k_des)
                    del cost_k_des
                gc.collect()
            costs = deepcopy(new_costs)
            new_costs.clear()
            gc.collect()

            # destination 0 will unavoidably cause visiting the vertex twice, such it is removed.
        min_cost = min(
            [costs[0, j] + euclidean_distance(self.cities[j], self.cities[0]) for j in range(1, self.n_cities)])
        return min_cost


if __name__ == "__main__":
    tsp = TSP('tsp.txt')
    print(tsp.solve_tsp())
