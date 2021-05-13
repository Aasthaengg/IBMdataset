import sys
input = sys.stdin.readline
from math import floor

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)] + [0]

    for i in range(n):
        if a[i+1] == 0:
            yield a[i] // 2
        else:
            yield a[i] // 2 + a[i] % 2
            a[i+1] -= a[i] % 2


print(sum(main()))
