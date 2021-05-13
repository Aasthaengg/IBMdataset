def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    #mod = 10**9 + 7

    n = int(input())
    l = list(map(int, input().split()))
    res = 0
    l.sort()
    for i in range(0, 2*n, 2):
        res += l[i]
    print(res)

if __name__ == '__main__':
    main()