n, m = map(int, input().split())
count = [1 for i in range(n + 1)]
count[0] = 0
flag = [False for i in range(n + 1)]
flag[1] = True
for i in range(m):
    x, y = map(int, input().split())
    if flag[x] == True:
        flag[y] = True
    count[x] -= 1
    count[y] += 1
    if count[x] == 0:
        flag[x] = False
print(sum(flag))