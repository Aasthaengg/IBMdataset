n, m = map(int, input().split())

exist = [0] * n
exist[0] = 1
cnt = [1] * n
for i in range(m):
    x, y = map(int, input().split())
    if exist[x - 1] == 1:
        exist[y - 1] = 1
        if cnt[x - 1] == 1:
            exist[x - 1] = 0

    
    cnt[x - 1] -= 1
    cnt[y - 1] += 1
print(sum(exist))