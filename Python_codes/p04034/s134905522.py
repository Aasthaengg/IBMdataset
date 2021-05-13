import math
from math import gcd,pi
INF = float("inf")

import sys
sys.setrecursionlimit(10**6)
import itertools
from collections import Counter,deque
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    n,m = i_map()
    box = [1 for _ in range(n+1)]
    red = [0 for _ in range(n+1)]
    red[1] = 1

    for i in range(m):
        x,y = i_map()
        box[x] -= 1
        box[y] += 1
        if red[x] == 1:
            red[y] = 1
        if box[x] == 0:
            red[x] = 0

    print(sum(red))

if __name__=="__main__":
    main()
