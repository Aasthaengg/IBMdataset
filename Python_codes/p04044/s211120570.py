import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections
import bisect

def main():
    n,l = map(int, input().split())
    array = [input() for _ in range(n)]

    array.sort()
    print(''.join(array))


if __name__ == '__main__':
    main()
