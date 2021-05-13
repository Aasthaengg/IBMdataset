N,M = map(int, input().split())
red = [0 for i in range(N)]
cnt = [1 for i in range(N)]
red[0] = 1
for i in range(M):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    if red[x] > 0:
        if cnt[x] >= 2:
            cnt[x] -= 1
            cnt[y] += 1
            red[y] = 1
        else:
            cnt[x] -= 1
            cnt[y] += 1
            red[x] = 0
            red[y] = 1
    else:
        cnt[x] -= 1
        cnt[y] += 1

ans = 0
for i in range(N):
    if red[i] > 0:
        ans += 1

print(ans)