import heapq as pq
from copy import deepcopy


class DSearch():
    def __init__(self, txt_name):
        self.graph = dict()
        self.read_txt(txt_name)
        v_list = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
        self.shortest_paths = {i: 100000 for i in v_list}
        self.g = {i: 100000000 for i in range(1, 201)}

    def recover_path(self, parent, goal):
        to_vertex = goal
        distance = 0
        while parent[to_vertex]:
            from_vertex = parent[to_vertex]
            for v in self.graph[from_vertex]:
                if v[0] == to_vertex:
                    distance += v[1]
            to_vertex = from_vertex
        self.shortest_paths[goal] = distance

    def read_txt(self, txt_name):
        """
            read txt and store it in an adjecent dictionary
        """
        with open(txt_name) as f:
            for line in f:
                str_list = line.rstrip("\n").split('\t')[:-1]
                node = int(str_list.pop(0))
                self.graph[node] = set()
                while str_list:
                    edge = str_list.pop(0)
                    self.graph[node].add(tuple(map(int, edge.split(','))))

    def saerch(self):
        for goal in self.shortest_paths.keys():
            source = (0, 1)  # (g(n), vertex)
            g = deepcopy(self.g)  # g(n)
            g[1] = 0
            parent_node = {1: []}
            open_list = []
            pq.heappush(open_list, source)
            closed_list = set()
            find_path = False
            while open_list:
                node = pq.heappop(open_list)
                if node in closed_list: # in graph search, visited node will not be visited again.
                    continue
                closed_list.add(node[1])
                if node[1] == goal:
                    find_path = True
                    break
                for neighbor in self.graph[node[1]]:  # (to_vertex, edge length)
                    if neighbor[0] not in closed_list:
                        if g[neighbor[0]] >= 100000000:
                            g[neighbor[0]] = g[node[1]] + neighbor[1]  # g(m) = g(n) + Cnm
                            pq.heappush(open_list, (g[neighbor[0]], neighbor[0]))
                            parent_node[neighbor[0]] = node[1]  # change parents
                        if g[neighbor[0]] > g[node[1]] + neighbor[1]: # update g in the open list
                            g[neighbor[0]] = g[node[1]] + neighbor[1]
                            pq.heappush(open_list, (g[neighbor[0]], neighbor[0])) # push the new value into it
                            parent_node[neighbor[0]] = node[1]  # change parents
            if find_path:
                self.shortest_paths[goal] = g[goal]
                # self.recover_path(parent_node, goal)


if __name__ == "__main__":
    ds = DSearch("dijkstraData.txt")
    ds.saerch()
    print(ds.shortest_paths)
    # TODO a few answers are wrong!!!
