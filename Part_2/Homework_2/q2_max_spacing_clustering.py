import numpy as np
from util.app.union_find import UnionFind


class BigClustering:
    def __init__(self, txt_name):
        self.nodes = np.array([])
        self.n_nodes = 0
        self.n_bits = 0
        self.read_txt(txt_name)
        self.clusters = {i: [i] for i in range(0, self.n_nodes)}  # initial number of clusters
        self.leader = {i: i for i in range(0, self.n_nodes)}

    def read_txt(self, txt_name):
        with open(txt_name) as f:
            str_list = f.readline().split(" ")
            self.n_nodes = int(str_list[0])
            self.n_bits = int(str_list[1])
            self.nodes = np.zeros((self.n_nodes, self.n_bits), dtype=bool)

            for i, line in enumerate(f):
                str_list = line.rstrip('\n').split(' ')
                if str_list[-1] == '':
                    str_list = str_list[:-1]
                bit_list = list(map(int, str_list))
                self.nodes[i, :] = np.array(bit_list)

    def run(self):
        uf = UnionFind(self.n_nodes)
        unions = []
        for from_node in range(0, self.n_nodes):
            hamming_matrix = self.nodes[from_node] - self.nodes[from_node+1:, :]
            count = np.count_nonzero(hamming_matrix, axis=1)

            for plus in range(0, count.size):
                if count[plus] < 3:
                    unions.append((from_node+1, from_node+1+plus+1))  # index starts from 1 for union find

            if from_node % 100 == 0:
                print("from node: ", from_node)

        self.make_unions(uf, unions)

        print("Number of clusters: ", uf.count)

    @staticmethod
    def make_unions(uf, unions_zero):
        for node_from, node_to in unions_zero:
            if not uf.connected(node_from, node_to):
                uf.union(node_from, node_to)

if __name__ == "__main__":
    msc = BigClustering("clustering_big.txt")
    # msc = BigClustering("cluster_big_forum_2.txt")

    msc.run()
