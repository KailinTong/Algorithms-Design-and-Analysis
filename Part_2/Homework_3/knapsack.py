import numpy as np
import sys
sys.setrecursionlimit(10000)

class Knapsack:
    def __init__(self, txt_name):
        self.size = 0
        self.num_items = 0
        self.items = [(0, 0)]  # (value, weight)
        self.array = np.array([])
        self.read_txt(txt_name)
        self.cache = {}
        self.value = self.compute_value(self.size, self.num_items)

    def read_txt(self, txt_name):
        with open(txt_name) as f:
            first_line = f.readline().rstrip("\n").split(" ")
            print("Knapsack size: " + first_line[0])
            self.size = int(first_line[0])
            print("Number of items: " + first_line[1])
            self.num_items = int(first_line[1])
            self.array = np.zeros(shape=(self.num_items+0, self.size), dtype=int) # add one row of 0

            for line in f:
                str_list = line.rstrip("\n").split(' ')
                item = tuple(map(int, str_list))
                self.items.append(item)

    def compute_value(self, weight, index):
        if index == 0 or weight == 0:
            return 0
        (this_value, this_weight) = self.items[index]
        # thie item weight is bigger than the weight size, no solution, decrease the index
        if this_weight > weight:
            if (weight, index - 1) not in self.cache:
                self.cache[(weight, index - 1)] = self.compute_value(weight, index - 1)
            return self.cache[(weight, index - 1)]
        else:
            # solution including this item
            if (weight - this_weight, index - 1) not in self.cache:
                self.cache[(weight - this_weight, index - 1)] = self.compute_value(weight - this_weight, index - 1)
            solution_including_this_item = this_value + self.cache[(weight - this_weight, index - 1)]
            if (weight, index - 1) not in self.cache:
                self.cache[(weight, index - 1)] = self.compute_value(weight, index - 1)
            solution_without_this_item = self.cache[(weight, index - 1)]
            return max(solution_including_this_item, solution_without_this_item)


if __name__ == "__main__":
    # k = Knapsack("knapsack1.txt")
    k = Knapsack("knapsack_big.txt")
    print(k.value)