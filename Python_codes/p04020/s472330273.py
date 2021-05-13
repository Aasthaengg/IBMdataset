import sys
input = sys.stdin.readline
from math import floor

def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    x = 0
    for a in A:
        if a == 0:
            yield x // 2
            x = 0
        x += a

    yield x // 2


print(sum(main()))
