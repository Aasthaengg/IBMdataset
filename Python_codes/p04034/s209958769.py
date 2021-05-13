import sys
#import string
#from collections import defaultdict, deque, Counter
#import bisect
#import heapq
#import math
#from itertools import accumulate
#from itertools import permutations as perm
#from itertools import combinations as comb
#from itertools import combinations_with_replacement as combr
#from fractions import gcd
#import numpy as np

stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)
MIN = -10 ** 9
MOD = 10 ** 9 + 7
INF = float("inf")
IINF = 10 ** 18

def solve():
    #n = int(stdin.readline().rstrip())
    n,m = map(int, stdin.readline().rstrip().split())
    #l = list(map(int, stdin.readline().rstrip().split()))
    #numbers = [[int(c) for c in l.strip().split()] for l in sys.stdin]
    #word = [stdin.readline().rstrip() for _ in range(n)]
    #number = [[int(c) for c in stdin.readline().rstrip()] for _ in range(n)]
    #zeros = [[0] * w for i in range(h)]
    red = [0] * n
    red[0] = 1
    ball = [1] * n
    for i in range(m):
        x,y = map(int, stdin.readline().rstrip().split())
        if red[x-1] != 0 and ball[x-1] != 1:
            red[y-1] = 1
            ball[x-1] -= 1
            ball[y-1] += 1
        elif red[x-1] != 0 and ball[x-1] == 1:
            red[x-1] = 0
            red[y-1] = 1
            ball[x-1] -= 1
            ball[y-1] += 1
        else:
            ball[x-1] -= 1
            ball[y-1] += 1
    print(sum(red))


if __name__ == '__main__':
    solve()
