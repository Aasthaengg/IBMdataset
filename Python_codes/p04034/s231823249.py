import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N,M = map(int,readline().split())

c = [1]*N
r = [0]*N
r[0] = 1

for _ in range(M):
    x,y = map(int,readline().split())
    x,y = x-1,y-1
    if r[x]:
        if c[x] == 1:
            r[x] = 0
        r[y] = 1
    c[x] -= 1
    c[y] += 1

print(sum(r))