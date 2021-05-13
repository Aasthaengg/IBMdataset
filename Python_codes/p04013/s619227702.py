def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n,a = map(int, input().split())
    x = list(map(int, input().split()))
    for i in range(n):
        x[i] -= a
    dp = [[0]*5001 for _ in range(n+1)]

    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(-2500, 2501):
            dp[i][j] += dp[i-1][j]
            if -2500 <= j-x[i-1] <= 2500:
                dp[i][j] += dp[i-1][j-x[i-1]]
    print(dp[-1][0]-1)

if __name__ == '__main__':
    main()