#!/usr/bin/env python3
import sys
# input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    N = INT()
    L = LI()
    L.sort()
    answer = 0
    for i in range(N):
        answer += min(L[2*i],L[2*i+1])

    print(answer)
    return

if __name__ == '__main__':
    main()
