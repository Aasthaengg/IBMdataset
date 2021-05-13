N, M = map(int, input().split())
ball_cnt = [1] * N
exist_red = [False] * N
exist_red[0] = True
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    ball_cnt[x] -= 1
    ball_cnt[y] += 1
    if exist_red[x]:
        exist_red[y] = True
    if ball_cnt[x] == 0:
        exist_red[x] = False
print(exist_red.count(True))
