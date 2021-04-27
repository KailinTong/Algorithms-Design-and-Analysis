import numpy as np
from math import sqrt
from itertools import combinations
from copy import deepcopy


def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


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
                            cost_k_des.append(costs[tuple(smaller_s), k] + euclidean_distance(self.cities[k], self.cities[j]))
                        else:
                            if smaller_s == [0]:
                                cost_k_des.append(0 + euclidean_distance(self.cities[0], self.cities[j]))
                            else:
                                cost_k_des.append(INF)
                    costs[(tuple(s), j)] = min(cost_k_des)
                    # destination 0 will unavoidably cause visiting the vertex twice, such it is removed.
        min_cost = min(
            [costs[tuple(s), j] + euclidean_distance(self.cities[j], self.cities[0]) for j in range(1, self.n_cities)])
        return min_cost


if __name__ == "__main__":
    tsp = TSP('tsp_test.txt')
    print(tsp.solve_tsp())
