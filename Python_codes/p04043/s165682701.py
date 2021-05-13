from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A = list(map(int, input().split()))

    print('YES') if A.count(5) == 2 and A.count(7) == 1 else print('NO')

if __name__ == '__main__':
    main()