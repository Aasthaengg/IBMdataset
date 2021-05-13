import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N, L = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())

S.sort()
ans = "".join(S)
print(ans)