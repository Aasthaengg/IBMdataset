import sys
stdin = sys.stdin
import itertools

mod = 10**9 + 7

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))

N = ni()
A = list()
for _ in range(N):
    A.append(ni())
cnt = 0
if N==1:
    print(A[0]//2)
    quit()
for i in range(N-1):
    ccnt = (A[i] + A[i+1]) //2
    A[i+1] -= max(0, ccnt*2 - A[i])
    A[i] = max(0, A[i]-ccnt*2)
    cnt += ccnt
print(cnt)