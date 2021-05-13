import copy
N, M = map(int, input().split())
XY = []
for _ in range(M):
    x, y = map(int, input().split())
    XY.append([x - 1, y - 1])

ball_num = [1] * N
is_red = [False] * N
is_red[0] = True

for i in range(M):
    s = XY[i][0]
    g = XY[i][1]
    if is_red[s]:
        if ball_num[s] == 1:
            ball_num[s] -= 1
            ball_num[g] += 1
            is_red[s] = False
            is_red[g] = True
        else:
            ball_num[s] -= 1
            ball_num[g] += 1
            is_red[g] = True
    else:
        ball_num[s] -= 1
        ball_num[g] += 1

print(sum(is_red))