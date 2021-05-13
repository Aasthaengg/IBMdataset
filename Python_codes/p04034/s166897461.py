import collections
n,m = map(int,input().split())
box = [[1,"white"] for i in range(n)]
box[0][1] = "red"
for i in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    if box[x][1] == "red":
        box[y][1] = "red"
    box[y][0] += 1
    box[x][0] -= 1
    if box[x][0] == 0:
        box[x][1] = "white"
ans = 0
for i in range(n):
    if box[i][1] == "red":
        ans += 1
print(ans)