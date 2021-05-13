n, m = map(int,input().split())
box = [[1,0] for i in range(n)]#個数、赤の可能性
box[0][1] = 1
ans = 1

for i in range(m):
    x, y = map(int,input().split())
    if box[x-1][0] == 0:
        continue
    box[x-1][0] -= 1
    box[y-1][0] += 1
    if box[x-1][1] == 1:
        if box[y-1][1] == 0:
            box[y-1][1] = 1
            ans += 1
        if box[x-1][0] == 0:
            box[x-1][1] = 0
            ans -= 1


print(ans)


