import sys
from collections import defaultdict, deque
import bisect
from heapq import *
from math import factorial, ceil, floor
from collections import defaultdict
import itertools
sys.setrecursionlimit(200000)
input = sys.stdin.readline

# N, M, = map(int, input().split())
# N = int(input())
# L = [int(v) for v in input().split()]
# L = [[int(v) for v in input().split()] for _ in range(N)]
# L = [int(input()) for _ in range(N)]
# L = [list(input().strip())  for _ in range(N)]
# S = input().strip()

N, = map(int, input().split())
L = [int(input()) for _ in range(N)]

ans = 0
for i in range(N):
    ans += L[i] //2
    L[i] = L[i] % 2

    if i < N - 1:
        if L[i] == 1 and L[i + 1] >= 1:
            L[i] = 0
            L[i + 1] -= 1
            ans += 1

print(ans)
