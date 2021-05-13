N,M = map(int,input().split())

XY = [list(map(int,input().split())) for _ in range(M)]

ball_count = [1]*N

red_ball_cand = [0]*N
red_ball_cand[0] = 1

for i in range(M):
    x,y = XY[i]
    x,y = x-1,y-1
    if 0 < red_ball_cand[x]:
        red_ball_cand[y] = 1
        
    ball_count[x] -= 1
    ball_count[y] += 1
    
    if ball_count[x] == 0:
        red_ball_cand[x] = 0
print(sum(red_ball_cand))