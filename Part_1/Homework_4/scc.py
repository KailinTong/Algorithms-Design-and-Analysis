from collections import deque
import sys
from copy import deepcopy
sys.setrecursionlimit(100000)

class Graph:
    def __init__(self, g_input=None):
        self.g = {}
        if isinstance(g_input, str):
            self.read_txt(g_input)
        else:
            self.g = g_input
        self.closed = []
        # self.open = deque()
        self.t = 0  # finishing time
        self.max_vertex = self.get_max_vertex()  # source of dfs
        self.ft = {}  # finishing time of each vertex
        self.scc_size = []  # scc size

    def read_txt(self, txt_name):
        """
            read txt and store it in an adjecent dictionary
        """
        with open(txt_name) as f:
            line = f.readline()
            while line and line != "\n":
                str_list = line.split(' ')[:-1]
                new_list = list(map(int, str_list))
                if new_list[1] not in self.g.keys():
                    self.g[new_list[1]] = []
                if new_list[0] not in self.g.keys():
                    self.g[new_list[0]] = [new_list[1]]
                else:
                    self.g[new_list[0]].append(new_list[1])

                line = f.readline()

    def get_r_graph(self):
        """
        get a direction-reversed Graph
        :return: direction-reversed Graph
        """
        r_graph = {}
        for k, v_list in self.g.items():
            for v in v_list:
                if v not in r_graph.keys():
                    r_graph[v] = []
                r_graph[v].append(k)
        return Graph(r_graph)

    def get_max_vertex(self):
        """
            get maximal vertex
        :return: max vertex
        """
        return max(self.g.keys())

    def dfs(self, s):
        """
        depth first search
        :param s: source of expansion in int
        """
        self.closed.append(s)
        if s in self.g.keys():  # todo correct?
            for n in self.g[s]:
                if n not in self.closed:
                    self.dfs(n)
        self.t += 1
        self.ft[s] = self.t

    def dfs_loop(self, step=1):
        """
            the main depth first search loop
        """
        s = self.max_vertex
        while True:
            last_size = len(self.closed)
            self.dfs(s)
            # in  graph but not in closed
            ret = list(set(self.g.keys()).difference(set(self.closed)))
            this_size = len(self.closed)
            if step == 2:
                self.scc_size.append(this_size - last_size)
            if not ret:
                break
            s = max(ret)

    # def dfs_stack(self, step=1):
    #     """
    #         the main depth first search based on stack
    #     """
    #
    #     s = self.max_vertex
    #     open_stack = deque([s])
    #     while True:
    #         last_size = len(self.closed)
    #         while open_stack:
    #             r = open_stack.pop()
    #             if r in self.g.keys():
    #                 for n in self.g[s]:
    #                     if n not in self.closed:
    #                         open_stack.append(n)
    #                     else:
    #                         self.t += 1
    #                         self.ft[r] = self.t
    #         # in  graph but not in closed
    #         ret = list(set(self.g.keys()).difference(set(self.closed)))
    #         this_size = len(self.closed)
    #         if step == 2:
    #             self.scc_size.append(this_size - last_size)
    #         if not ret:
    #             break
    #         s = max(ret)
    #         open_stack = deque([s])

    def get_graph_from_mapping(self, map_dict):
        """

        :param map_dict: mapping dictiionary
        :return: a mapped Graph
        """
        new_g = {}
        for key, v_list in self.g.items():
            new_g[map_dict[key]] = [map_dict[v] for v in v_list]
        return Graph(new_g)


# process:
# create a graph (adjecent list)
# create a reverse graph (copy from the first one)
# DFS

if __name__ == "__main__":
    # test
    # g = Graph("jason_smko_last.txt")
    # print(g)
    # g_ = g.get_r_graph()
    # g_.dfs_loop()
    # print(g_.ft)
    # g_ft = g.get_graph_from_mapping(g_.ft)
    # print(g_ft.g)
    # del g_, g
    # g_ft.dfs_loop(step=2)
    # print(g_ft.scc_size)

    # # real data
    # g = Graph("SCC.txt")
    # g_ = g.get_r_graph()
    # print("get reversed graph")
    # del g
    # g_.dfs_loop()
    # print("first pass okay!")
    # ft = deepcopy(g_.ft)
    # g = Graph("SCC.txt")
    # g_ft = g.get_graph_from_mapping(ft)
    # del g_, g
    # g_ft.dfs_loop(step=2)
    # print("second pass okay!")
    # print(g_ft.scc_size)


    #Sumary:
    # my code is correct is small test cases but memory meets an overflow. And it runs rather slowly.
    # To be improved:
    # Using stack for DFS instead of recursive call of functions, recursive calls are too many > 1000
    # using negative edge to record reversed graph in one dict instead of creating a new reversed graph
    # using set() to track visited nodes and finished nodes instead of list, cause the index is not important and membership test is faster for sets

