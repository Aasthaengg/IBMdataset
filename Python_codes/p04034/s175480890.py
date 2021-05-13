n,m=map(int,input().split())
ball_in_boxes = [1]*n
redball_flag = [False]*n
redball_flag[0] = True
for _ in range(m):
    x,y = map(int,input().split())
    if redball_flag[x-1]: # x番目の箱に赤いボールが入っている可能性がある
        redball_flag[y-1] = True
    ball_in_boxes[x-1] -= 1
    ball_in_boxes[y-1] += 1

    if ball_in_boxes[x-1] == 0: # x番目の箱にボールが入っていないので
        redball_flag[x-1] = False
print(redball_flag.count(True))
