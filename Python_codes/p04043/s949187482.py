import sys
from heapq import heappush, heappop, heapify
import math
from math import gcd
import itertools as it
from collections import deque 

input = sys.stdin.readline

def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))

INF = 1001001001

# ---------------------------------------

def main():
    A = inpl()
    A.sort()
    if A[0]==A[1]==5 and A[2]==7:
        print("YES")
    else:
        print("NO")

main()
