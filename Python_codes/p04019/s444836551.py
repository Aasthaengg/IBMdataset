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

    s = input().rstrip()
    if ('N' in s and 'S' in s) or ('N' not in s and 'S' not in s):
        if ('W' in s and 'E' in s) or ('W' not in s and 'E' not in s):
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()