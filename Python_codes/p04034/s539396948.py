n, m = map(int, input().split())
boxes = [[0, 1] for _ in range(n)]
boxes[0][0] = 1
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    boxes[x][1] -= 1
    boxes[y][1] += 1
    if boxes[x][0] == 1:
        boxes[y][0] = 1
    else:
        if boxes[y][0] == 1:
            continue
        else:
            boxes[y][0] = 0  
    if boxes[x][1] == 0:
        boxes[x][0] = -1
ans = 0
for a, b in boxes:
    # print(a, b)
    if a > 0:
        ans += 1
# print(boxes)
print(ans)
