import sys
n, m = map(int, input().split())
ball = [1 for i in range(n+1)]
box = [0 for i in range(n+1)]
box[1] = 1
for a in sys.stdin.readlines():
    x, y = map(int, a.split())
    ball[x] -= 1
    ball[y] += 1
    if box[y] == 0 and box[x]:
        box[y] = 1
    if box[x] and ball[x] == 0:
        box[x] = 0

print(sum(box))