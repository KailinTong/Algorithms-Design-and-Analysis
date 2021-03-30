from copy import deepcopy
from collections import deque


class QuickSort:
    def __init__(self, a):
        """

        :param a: a list of input array
        """
        self.a = a
        self.par = [(0, len(self.a) - 1)]  # recording pivots
        self.m = 0  # number of comparisons

    def partition(self, start_idx, end_idx):
        """

        :param start_idx: start index of a subarray (partition)
        :param end_idx: end index of a subarray (partition)
        :return: is_sorted: is it a sorted partition
                (i-2): the left index of the pivot
                i: the right index of the pivot
        """
        # Q2: swap the first and final element, so that pivot is the final element
        # self.a[start_idx], self.a[end_idx] = self.a[end_idx], self.a[start_idx]

        # Q3: swap the first and median element
        self.swap_median_of_three(start_idx, end_idx)

        self.m += end_idx - start_idx
        p = start_idx  # pivot is always the first element of an array
        if start_idx == end_idx:  # end_index is included
            return True, start_idx, end_idx
        else:
            # i tracking the first element index of value bigger than the pivot,
            # j tracking the first unpartitioned number, bigger than len(a) means no un unpartitioned element
            i = p + 1
            for j in range(p + 1, end_idx + 1):
                if self.a[p] < self.a[j]:
                    pass
                else:
                    # swap
                    self.a[i], self.a[j] = self.a[j], self.a[i]
                    i += 1

        # swap the last element smaller than the pivot and the pivot value
        self.a[p], self.a[i - 1] = self.a[i - 1], self.a[p]
        # print(self.a)
        return False, (i - 2), i

    def sort(self):
        """
        quick sort
        :return:
        """
        if len(self.a) <= 1:
            return self.a
        else:
            # recursive calling partition until number of pivots equals to number of elements in the array
            while self.par:
                temp_list = []
                for par in self.par:
                    is_par_sorted, new_p_l, new_p_r = self.partition(par[0], par[1])
                    if is_par_sorted:
                        pass
                    else:
                        if new_p_l > par[0]:
                            temp_list.append((par[0], new_p_l))
                        if new_p_r < par[1]:
                            temp_list.append((new_p_r, par[1]))

                self.par = deepcopy(temp_list)

    def swap_median_of_three(self, s_index, e_index):
        """

        :param s_index: start index of an array
        :param e_index: end index of an array
        :return: index of the medan
        """
        l = e_index - s_index + 1
        m_index = l // 2 - 1 + s_index if l % 2 == 0 else l // 2 + s_index

        l, m, r = self.a[s_index], self.a[m_index], self.a[e_index]
        if l <= m <= r or l <= m <= r:
            self.a[s_index], self.a[m_index] = self.a[m_index], self.a[s_index]
        elif l <= r <= m or m <= r <= l:
            self.a[s_index], self.a[e_index] = self.a[m_index], self.a[e_index]


def get_array():
    """

    :rtype: a list of integers
    """
    a = []
    with open('QuickSort.txt') as f:
        for line in f:
            a.append(int(line))
    return a


if __name__ == "__main__":
    input_a = get_array()
    # input_a = [3, 8, 2, 5, 1, 4, 7, 6]
    # input_a = [1, 2, 3, 4, 5, 6, 7, 8]
    # print(input_a)
    qs = QuickSort(input_a)
    qs.sort()
    print(qs.a)
    print("number of comparisons:")
    print(qs.m)
    # print(get_median_index(3, 6))

    # TODO: this code worked for question 1 and 2 but did not pass the third question, the reason is unknown.
    #  I guess a better implementation will solve the problem. ref: https://github.com/sestus/algorithms-stanfordK
    #  Improvement: using recursive function instead of recording pivot index
