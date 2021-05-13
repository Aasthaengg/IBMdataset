n_box, n_move = map(int,input().split())
num_balls = [1] * n_box
can_red = [0] * n_box
can_red[0] = 1
for i in range(n_move):
    From, to = map(int,input().split())
    From -= 1
    to -= 1
    if can_red[From] == 1:
        if num_balls[From] == 1:
            can_red[From] = 0
            can_red[to] = 1
        else:
            can_red[to] = 1
    num_balls[From] -= 1
    num_balls[to] += 1

ans = 0
for i in range(n_box):
    if can_red[i] == 1:
        ans += 1
print(ans)

