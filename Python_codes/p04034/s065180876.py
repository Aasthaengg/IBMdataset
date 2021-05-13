n, m = map(int, input().split())

# ボール個数、赤いボールがある可能性を管理
b = [1] * n
red = [1] + [0] * (n - 1)

for i in range(m):
    x, y = map(int, input().split())

    # 移す元に赤いボールがある可能性があれば、移す先に赤いボールが渡る可能性がある
    if red[x - 1] == 1:
        red[y - 1] = 1

    # ボール数の足し引き
    b[x - 1] -= 1
    b[y - 1] += 1

    # xのボールが0になったら赤いボールがある可能性が消える
    if b[x - 1] == 0:
        red[x - 1] = 0

ans = len([x * y for x, y in zip(b, red) if x * y > 0])

print(ans)