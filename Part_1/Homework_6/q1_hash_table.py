class HashTable:
    def __init__(self, txt_name):
        self.ht = set()
        self.read_txt(txt_name)
        self.counts = 0

    def read_txt(self, txt_name):
        """
            read txt and store it in a hash table (set)
        """
        with open(txt_name) as f:
            for line in f:
                num = int(line.rstrip("\n"))
                self.ht.add(num)

    def run(self):
        for t in range(-10000, 10001):
            for x in self.ht:
                if (t-x) in self.ht:
                    self.counts += 1
                    break

        print("the counts are: ", self.counts)


if __name__ == "__main__":
    ht = HashTable("algo1-programming_prob-2sum.txt")
    ht.run()
