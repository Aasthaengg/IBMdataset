N,M = map(int, input().split())

balls_in_box = [0] + [1 for _ in range(1,N+1)]
red_ball_containable_box = set()
red_ball_containable_box.add(1)

for i in range(M):
    x,y = map(int, input().split())
    if x in red_ball_containable_box:
        balls_in_box[x] -= 1
        balls_in_box[y] += 1
        red_ball_containable_box.add(y)
        if balls_in_box[x] == 0: #赤玉が入っている可能性が100％の箱を全部空にすれば確実に移る
            red_ball_containable_box.remove(x)
    else:
        balls_in_box[x] -= 1
        balls_in_box[y] += 1

print(len(red_ball_containable_box))