N, M = list(map(int, input().split()))

box = []
box.append([1, True])
for _ in range(N - 1):
    box.append([1, False])

for _ in range(M):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1

    box[x][0] -= 1
    box[y][0] += 1

    if box[x][1]:
        box[y][1] = True

    if box[x][0] == 0:
        box[x][1] = False
    
ans = 0
for i in range(N):
    if box[i][1]:
        ans += 1
print(ans)