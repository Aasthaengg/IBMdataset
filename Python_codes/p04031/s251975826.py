import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cost = []
    for i in range(-100, 101):
        ramen = 0
        for j in range(n):
            ramen += abs(a[j]-i)**2
        cost.append(ramen)
    print(min(cost))
    return 0

if __name__ == "__main__":
    solve()
