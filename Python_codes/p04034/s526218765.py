import sys
input = sys.stdin.readline

# from collections import deque

def linput(ty=int, cnv=list):
    return cnv(map(ty, input().split()))

def vinput(rep=1, ty=int, cnv=list):
    return cnv(ty(input().rstrip()) for _ in "*"*rep)

def gcd(n,m):
    while m: n,m = m, n%m
    return n

def lcm(n,m): return n*m//gcd(n,m)

def main():
    N,M = linput()

    vR = [0, 1,] + [0,]*(N-1)
    vN = [0, 1,] + [1,]*(N-1)

    res = 0

    for _ in range(M):
        a,b = linput()
        if vR[a]:
            vR[b] = 1
        if vN[a]==1:
            vR[a] = 0

        vN[a] -= 1
        vN[b] += 1

    res = sum(vR)
    print(res)
    # sT = "No Yes".split()
    # print(sT[res])
    # for vR in mR:
    #     print(*vR, sep="")

main()
