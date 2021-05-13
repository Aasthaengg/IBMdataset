import sys
input = sys.stdin.readline

# from collections import deque

def linput(_t=int, cnv=list):
    return cnv(map(_t, input().split()))

def gcd(n,m):
    while m: n,m = m, n%m
    return n

def lcm(n,m): return n*m//gcd(n,m)

def main():
    N = int(input())
    vA = [int(input()) for _ in [0,]*N]

    res = 0
    odd = 0

    for a in vA:
        x = (a+odd)//2
        k = (a+odd) - 2*x
        res += x
        odd = min(k,a)
        # print(res,a,x,odd)####

    print(res)
    # print("No Yes".split()[res])

main()
