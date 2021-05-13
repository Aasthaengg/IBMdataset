n, m = list(map(int, input().split()))
b = [["W", 1] for _ in range(n)]
b[0] = ["R", 1]

for i in range(m):
    x, y = list(map(int, input().split()))

    b[x-1][1] -= 1
    if b[x-1][0] == "R":
        b[y-1] = ["R", b[y-1][1]+1]

        if b[x-1][1] == 0:
            b[x-1][0] = "W"
    else:
        b[y-1][1] += 1

cnt = 0
for i in range(n):
    if b[i][0] == "R":
        cnt += 1

print(cnt)