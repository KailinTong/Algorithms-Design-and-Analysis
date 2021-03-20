from random import choice
from random import seed
from copy import deepcopy


class KargeMinCut:
    def __init__(self):
        self.random_seed = seed(0)
        self.adj_dict = dict()
        self.read_txt()


    def read_txt(self):
        """
            read txt and store it in an adjecent dictionary
        """
        with open('kargerMinCut.txt') as f:
            line = f.readline()
            while line:
                str_list = line.split('\t')[:-1]
                new_list = list(map(int, str_list))
                if len(new_list) != len(new_list):
                    print("contain duplicates!")

                self.adj_dict[new_list[0]] = new_list[1:]
                line = f.readline()

    def contraction(self):
        adj_dict_op = deepcopy(self.adj_dict)

        while len(adj_dict_op) > 2:
            # randomly choose one vertex
            v1 = choice(list(adj_dict_op.keys()))
            # randomly choose another neighbored vertex
            v2 = choice(adj_dict_op[v1])

            merge_list = deepcopy(adj_dict_op[v1] + adj_dict_op[v2])
            # delete the connections from v2 to other vetices
            for v in adj_dict_op[v2]:
                # rewire to v1
                adj_dict_op[v] = [v1 if e == v2 else e for e in adj_dict_op[v]]

            # merge two vertex into the first vertex and remove the choosen and edge and self-loops
            adj_dict_op[v1] = [e for e in merge_list if e not in [v1, v2]]

            # remove v2
            del adj_dict_op[v2]

        min_cuts = len(adj_dict_op[list(adj_dict_op.keys())[0]])
        return min_cuts


if __name__ == "__main__":
    kmc = KargeMinCut()
    mc = 200
    for n in range(100000):
        kmc.random_seed = seed(n)
        c = kmc.contraction()
        if c < mc:
            mc = c
        if n % 100 == 0:
            print("episode", n, "has minimal cuts:", mc)
    print(mc)
