import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
boxes = [0]*N
balls = [1]*N
boxes[0] = 1
for _ in range(M):
    x, y = mapint()
    boxes[y-1] = 1 if boxes[x-1]==1 else boxes[y-1]
    balls[x-1] -= 1
    balls[y-1] += 1
    if balls[x-1]==0:
        boxes[x-1] = 0

print(sum(boxes))