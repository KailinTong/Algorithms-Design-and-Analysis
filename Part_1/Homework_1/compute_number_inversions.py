from copy import deepcopy
from collections import deque


def get_array():
    """

    :rtype: a list of integers
    """
    a = []
    with open('IntegerArray.txt') as f:
        for line in f:
            a.append(int(line))
    return a

def split_array(a):
    """
    split a list into two lists
    :param a: list of integers
    :return: two sub-list of integers
    """
    n = len(a)
    if n == 1:
        return a
    index = n // 2
    b = a[:index]
    c = a[index:]
    return b, c


def merge_and_count(a, b):
    """

    :param a: a list of integers
    :param b: a list of integers
    :return: c: the merged list
            count: the number of inversions
    """
    n = len(a) + len(b)
    i_a = 0
    i_b = 0
    c = []
    count = 0

    for i in range(0, n):
        if i_a >= len(a):
            c.append(b[i_b])
            i_b += 1

        elif i_b >= len(b):
            c.append(a[i_a])
            i_a += 1

        elif a[i_a] < b[i_b]:
            c.append(a[i_a])
            i_a += 1

        else:
            c.append(b[i_b])
            i_b += 1
            count += len(a) - i_a
    return c, count


def countArrary(input_a):
    """
    count the number of inversions
    :param input_a: input list of integers
    :return: count of inversions
    """
    if len(input_a) == 1:
        return 0
    else:
        # split the input array
        split_a = [input_a]
        while len(split_a) != len(input_a):
            new_split_a = []
            for sub_a in split_a:
                if len(sub_a) > 1:
                    b, c = split_array(sub_a)
                    new_split_a.append(b)
                    new_split_a.append(c)
                else:
                    new_split_a.append(sub_a)
            split_a = deepcopy(new_split_a)

        # merge and count
        merge_a = deque(split_a)
        count = 0
        while len(merge_a[0]) < len(input_a):
            new_merge_a = []
            while merge_a:
                a = merge_a.popleft()
                if merge_a:
                    b = merge_a.popleft()
                    c, c_inv = merge_and_count(a, b)
                    count += c_inv
                    new_merge_a.append(c)
                else:
                    new_merge_a.append(a)

            merge_a = deque(deepcopy(new_merge_a))

        # print(merge_a)
        return count


if __name__ == "__main__":
    input_a = get_array()
    print(countArrary(input_a))
