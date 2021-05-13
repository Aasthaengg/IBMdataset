import collections
import sys
import numpy as np
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
MOD = 10**9+7
import itertools
import math

a,b = map(int,input().split())
if a*b<0:
    print("Zero")
if a>0:
    print("Positive")
if b<0:
    cnt = b-a + 1
    if cnt %2 == 1:
        print("Negative")
    else:
        print("Positive")