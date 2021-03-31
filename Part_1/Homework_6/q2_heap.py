from sortedcontainers import SortedList


class Heap:
    def __init__(self):
        self.m_sum = 0

    def run(self, txt_name):
        """
            read txt and get median
        """
        with open(txt_name) as f:
            num_list = SortedList()
            for line in f:
                num = int(line.rstrip("\n"))
                num_list.add(num)
                k = len(num_list)
                if k % 2 == 1:
                    m = num_list[(k + 1) // 2 - 1]
                else:
                    m = num_list[k // 2 - 1]
                self.m_sum += m
        print("median sum mod 10000 is:", self.m_sum % 10000)


if __name__ == "__main__":
    h = Heap()
    h.run("Median.txt")
