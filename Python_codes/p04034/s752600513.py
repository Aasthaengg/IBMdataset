import math
import collections
import fractions
import itertools
import functools
import  operator

def solve():
    n, m = map(int, input().split())
    ball, can = [1]*n, [False]*n
    can[0] = True
    for _ in range(m):
        x, y = map(int, input().split())
        if can[x-1] == True:
            can[y-1] = True
        ball[x-1] -= 1
        ball[y-1] += 1
        if ball[x-1] == 0:
            can[x-1] = False
    print(can.count(True))
    return 0

if __name__ == "__main__":
    solve()
