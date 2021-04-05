import heapq


class JobScheduler:
    def __init__(self, txt_name):
        self.difference_heap = []
        self.ratio_heap = []

        self.read_txt(txt_name)

    def read_txt(self, txt_name):
        """
            read txt and store it in a heap        """
        with open(txt_name) as f:
            first_line = f.readline()
            print("Number of jobs: " + first_line)
            n = 0
            for line in f:
                str_list = line.rstrip("\n").split(' ')
                new_list = list(map(int, str_list))
                heapq.heappush(self.difference_heap, (
                    -(new_list[0] - new_list[1]), -new_list[0], -new_list[1]))  # change from min heap to max heap
                heapq.heappush(self.ratio_heap, (
                    -(new_list[0] / new_list[1]), -new_list[0], -new_list[1]))  # change from min heap to max heap
                n += 1
            print(str(n) + " read!")

    def difference_run(self):
        completion_time = 0
        weighted_completion_time = 0
        while self.difference_heap:
            (_, w, ct) = heapq.heappop(self.difference_heap)
            completion_time += -ct  # negative to positive
            weighted_completion_time += -w * completion_time  # negative to positive
        print(weighted_completion_time)

    def ratio_run(self):
        completion_time = 0
        weighted_completion_time = 0
        while self.ratio_heap:
            (_, w, ct) = heapq.heappop(self.ratio_heap)
            completion_time += -ct  # negative to positive
            weighted_completion_time += -w * completion_time  # negative to positive
        print(weighted_completion_time)


if __name__ == "__main__":
    sd = JobScheduler("jobs.txt")
    sd.difference_run()
    sd.ratio_run()
