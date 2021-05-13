from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,A = inpl()
x = inpl()
nx = n * max(max(x),A)
dp = [[[0 for _ in range(n+5)] for i in range(nx+1)] for j in range(n+5)]
dp[0][0][0] = 1
for i in range(n):
    for j in range(nx+1):
        for k in range(n):
            if j >= x[i]:
                dp[i+1][j][k+1] = dp[i][j-x[i]][k] + dp[i][j][k+1]
            else:
                dp[i+1][j][k] = dp[i][j][k]

ans = 0
for j in range(1,nx+1):
    for k in range(1,n+1):
        if j/k == A:
            ans += dp[n][j][k]
print(ans)