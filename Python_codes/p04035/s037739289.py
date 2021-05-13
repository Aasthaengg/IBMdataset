from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
INF = 10 ** 10


def main():
    N, L = map(int, input().split())
    a_list = list(map(int, input().split()))

    for i in range(N - 1):
        if a_list[i] + a_list[i + 1] >= L:
            break
    else:
        print("Impossible")
        return

    print("Possible")
    for x in range(1, i + 1):
        print(x)
    for x in range(N - 1, i, -1):
        print(x)


if __name__ == '__main__':
    main()
