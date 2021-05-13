n, m = map(int, input().split())
ball = [1]*n
flg = [False]*n
flg[0] = True

for _ in range(m):
    x, y = map(int, input().split())
    if flg[x-1]:
        flg[y-1] = True
    if ball[x-1] == 1 and flg[x-1]:
        flg[x-1] = False
    ball[y-1] += 1
    ball[x-1] -= 1
    # print(x, y, ball, flg)

ans = flg.count(True)
print(ans)
