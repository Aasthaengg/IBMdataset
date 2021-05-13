#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

a,b = LI()
if a <= 0 <= b:
    print('Zero')
elif a > 0:
    print('Positive')
elif b < 0:
    if (b - a) % 2 == 0:
        print('Negative')
    else:
        print('Positive') 