# -*- coding: utf-8 -*-
import sys
from collections import defaultdict, deque
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1]


def solve():
    a, b = [int(x) for x in input().split()]
    if a <= 0 and b >= 0:
        print("Zero")
    elif a > 0 and b > 0 or (b - a) % 2:
        print("Positive")
    else:
        print("Negative")

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()



"""

1 4
7
RRRR
1 1 0 1
----
4

1 4
47
RCRR
1 1 0 1
----
-1

2 2
10
RR
RR
1 7
4 1
----
4

2 2
10
RR
RR
7 4
7 4
----
-1

3 3
8
RCR
RRC
RRR
1 1 1
1 1 1
1 3 1


3 3
1
RCR
RRC
RRR
1 1 1
1 1 1
1 3 1


"""



