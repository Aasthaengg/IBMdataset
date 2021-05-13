N, M = map(int, input().split())
ball_count = [1 for _ in range(N)]
if_red_exists = [1] + [0 for _ in range(N-1)]
count = 1
for _ in range(M):
    x, y = map(int, input().split())
    if if_red_exists[x-1]:
        # 赤が存在する場合
        if_red_exists[y-1] = 1
        if ball_count[x-1] <= 1:
            if_red_exists[x-1] = 0
    ball_count[x-1] -= 1
    ball_count[y-1] += 1

count = 0
for e in if_red_exists:
    if e == 1:
        count += 1
print(count)
