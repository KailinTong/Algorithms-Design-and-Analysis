class MaxSpacingClustering:
    def __init__(self, txt_name):
        self.k_cluster = 4
        self.n_nodes = 0
        self.cost_dict = {}
        self.sorted_list = []
        self.read_txt(txt_name)
        self.clusters = {i: [i] for i in range(1, self.n_nodes + 1)}  # initial number of clusters
        self.leader = {i: i for i in range(1, self.n_nodes + 1)}

    def read_txt(self, txt_name):
        with open(txt_name) as f:
            first_line = f.readline().rstrip("\n")
            print("Number of nodes: " + first_line)
            self.n_nodes = int(first_line)
            temp_list = []
            for line in f:
                str_list = line.rstrip("\n").split(' ')
                new_list = list(map(int, str_list))
                endpoints = tuple(new_list[0:2])
                self.cost_dict[endpoints] = new_list[2]
                temp_list.append(endpoints)
            self.sorted_list = sorted(temp_list, key=self.get_cost)

    def get_cost(self, key):
        return self.cost_dict[key]

    def run(self):
        for i, e in enumerate(self.sorted_list):
            n1, n2 = e
            if self.leader[n1] == self.leader[n2]:
                continue

            # merge small cluster to large cluster
            # merge n2 into n1
            if len(self.clusters[self.leader[n1]]) >= len(self.clusters[self.leader[n2]]):
                new_leader = self.leader[n1]
                discarded_leader = self.leader[n2]
                for n in self.clusters[discarded_leader]:
                    self.clusters[new_leader].append(n)  # update cluster
                    self.leader[n] = new_leader  # rewiring leader
                del self.clusters[discarded_leader]  # the small cluster is discarded
            # merge n1 into n2
            else:
                new_leader = self.leader[n2]
                discarded_leader = self.leader[n1]
                for n in self.clusters[discarded_leader]:
                    self.clusters[new_leader].append(n)  # update cluster
                    self.leader[n] = new_leader  # rewiring leader
                del self.clusters[discarded_leader]

            if len(self.clusters) <= self.k_cluster:
                break

        spacing = {}
        for j in range(i+1, len(self.sorted_list)):
            e = self.sorted_list[j]
            leader1, leader2 = self.leader[e[0]], self.leader[e[1]]
            if leader1 != leader2:
                print("the max spacing is: ", self.cost_dict[e])
                break


if __name__ == "__main__":
    msc = MaxSpacingClustering("clustering1.txt")
    # msc = MaxSpacingClustering("cluster_small_forum_2.txt")
    msc.run()