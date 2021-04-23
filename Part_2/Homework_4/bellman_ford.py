import numpy as np


class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost


class BellmanFord:
    def __init__(self, txt_name):
        self.n_edges = 0
        self.size = 0
        self.n_vertices = 0
        self.edges = []  # (value, weight)
        self.read_txt(txt_name)

    def read_txt(self, txt_name):
        with open(txt_name) as f:
            first_line = f.readline().rstrip("\n").split(" ")
            self.n_vertices = int(first_line[0])
            self.n_edges = int(first_line[1])
            for line in f:
                str_list = line.rstrip("\n").split(' ')
                item = tuple(map(int, str_list))
                e = Edge(item[0] - 1, item[1] - 1, item[2])  # shift index to start from 0
                self.edges.append(e)

    def solve_apsp(self):
        sp_costs = []
        for s in range(0, self.n_vertices):  # all-pairs shortest-path problem
            c = self.solve_sp(s)
            if c == "NULL":
                return c
            else:
                sp_costs.append(c)
        return min(sp_costs)

    def solve_sp(self, s):
        INF = 1e8
        costs = np.full(self.n_vertices, INF, dtype=int)
        costs[s] = 0

        for i in range(1, self.n_vertices+1):  # one more additional loop to detect a negative cost cycle
            change = False
            for j in range(self.n_edges):
                if costs[self.edges[j].u] < INF:
                    if costs[self.edges[j].v] > costs[self.edges[j].u] + self.edges[j].cost:
                        costs[self.edges[j].v] = costs[self.edges[j].u] + self.edges[j].cost
                        change = True

            if not change:
                break
            if change and i == self.n_vertices:
                print("Negative cost cycle detected!")
                return "NULL"

        return np.min(costs)


if __name__ == "__main__":
    bf = BellmanFord('g1.txt')
    print("g1 cost: ", bf.solve_apsp())
    bf = BellmanFord('g2.txt')
    print("g2 cost: ", bf.solve_apsp())
    bf = BellmanFord('g3.txt')
    print("g3 cost: ", bf.solve_apsp())