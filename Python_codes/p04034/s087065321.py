N,M = map(int,input().split())
XY = [tuple(map(int,input().split())) for i in range(M)]

may_red = [0] * N
may_red[0] = 1
balls = [1] * N

for x,y in XY:
    x,y = x-1,y-1
    if may_red[x]:
        may_red[y] = 1
        if balls[x] == 1:
            may_red[x] = 0
    balls[x] -= 1
    balls[y] += 1
print(sum(may_red))