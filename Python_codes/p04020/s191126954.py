import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Xs = [int(input()) for _ in range(N)]

last = 0
ans = 0
for i in range(1, N+1):
    cnt = Xs[i-1]
    if cnt<=last:
        ans += cnt
        last = 0
    else:
        ans += last
        cnt -= last
        ans += cnt//2
        last = cnt%2
print(ans)