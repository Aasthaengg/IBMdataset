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

    a,b = map(int, input().split())
    if a > 0:
        print('Positive')
    elif b>=0:
        print('Zero')
    else:
        if (b-a+1)%2 == 0:
            print('Positive')
        else:
            print('Negative')

if __name__ == '__main__':
    main()