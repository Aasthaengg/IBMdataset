n, m = map(int, input().split())
a = [1]*n
ans_box = [False]*n
ans_box[0] = True
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    a[x] -= 1
    a[y] += 1
    if ans_box[x]:
        if a[x] == 0:
            ans_box[x] = False
        ans_box[y] = True
print(ans_box.count(True))




