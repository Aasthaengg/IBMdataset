#!/usr/bin/env python3
import sys


def main():
    N, M = map(int, input().split())
    red = [0] * N
    red[0] = 1
    num = [1] * N

    for i in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if red[x]:
            red[y] = 1
            
        num[x] -= 1
        num[y] += 1
        if num[x] == 0:
            red[x] = 0
    print(sum(red))

if __name__ == '__main__':
    main()
