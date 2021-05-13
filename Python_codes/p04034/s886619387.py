import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

opes = []
for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    opes.append((x-1, y-1))

transported = set()
transported.add(0)
boxes = [1 for _ in range(N)]

for (x, y) in opes:
    boxes[x] -= 1
    boxes[y] += 1
    if x in transported:
        transported.add(y)
    if boxes[x] == 0 and x in transported:
        transported.remove(x)

print(len(transported))