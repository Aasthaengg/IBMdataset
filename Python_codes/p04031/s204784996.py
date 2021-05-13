import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    A = read_ints()
    avg = sum(A)/N
    cost = lambda M: sum(abs(a-M)**2 for a in A)
    return min(cost(math.floor(avg)), cost(math.ceil(avg)))


if __name__ == '__main__':
    print(solve())
