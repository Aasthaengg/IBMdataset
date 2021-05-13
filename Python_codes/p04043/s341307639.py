from sys import stdin, stdout
from time import perf_counter

import sys
sys.setrecursionlimit(10**9)
mod = 10**9+7


l = [int(item) for item in input().split()]

if (l[0]==5 and l[1] == 5 and l[2]==7) or (l[0]==5 and l[1] == 7 and l[2]==5) or (l[0]==7 and l[1] == 5 and l[2]==5):
    print("YES")
else:
    print("NO")