N, M = map(int, input().split())
possibility = [False] * N  # True: 赤いボールが入っている可能性がある
possibility[0] = True
balls = [1] * N  # 箱に入っているボールの数
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if possibility[x]:
        possibility[y] = True
    balls[x] -= 1
    balls[y] += 1
    if balls[x] == 0:
        possibility[x] = False

ans = possibility.count(True)
print(ans)
