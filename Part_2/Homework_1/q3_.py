import heapq


class MinimumSpanningTree:
    def __init__(self, txt_name):
        self.v_cv = {}
        self.n = 0
        self.read_txt(txt_name)

    def read_txt(self, txt_name):
        """
            read txt and store it in a heap        """
        with open(txt_name) as f:
            first_line = f.readline()
            print("Number of nodes and number of edges are:: " + first_line)
            self.n = int(first_line.split(' ')[0])
            for line in f:
                str_list = line.rstrip("\n").split(' ')
                new_list = list(map(int, str_list))
                if new_list[0] not in self.v_cv.keys():
                    self.v_cv[new_list[0]] = []
                if new_list[1] not in self.v_cv.keys():
                    self.v_cv[new_list[1]] = []
                self.v_cv[new_list[0]].append((new_list[2], new_list[1]))  # (cost, to_vertex)
                self.v_cv[new_list[1]].append((new_list[2], new_list[0]))  # (cost, to_vertex

    def run(self):
        from_v = 1  # chosen arbitrarily
        visited_v = set()
        tree = set()
        total_cost = 0

        while True:
            visited_v.add(from_v)
            if len(visited_v) == self.n:
                break
            cost_heap = []
            for v in visited_v:
                for cv in self.v_cv[v]:
                    if cv[1] in visited_v:
                        continue
                    heapq.heappush(cost_heap, (cv[0], (v, cv[1])))
            cost, (from_v, to_v) = heapq.heappop(cost_heap)
            tree.add((from_v, to_v))
            from_v = to_v
            total_cost += cost
        print(total_cost)


if __name__ == "__main__":
    sd = MinimumSpanningTree("edges.txt")
    sd.run()
