# B - Box and Ball
N,M = map(int,input().split())
move = [list(map(int,input().split())) for _ in range(M)]
box = [[1,0] for _ in range(N+1)]
box[1][1] = 1
for x,y in move:
    box[x][0] -= 1
    box[y][0] += 1
    if box[x][1]==1:
        box[y][1] = 1
        if box[x][0]==0:
            box[x][1] = 0
print(sum(b[1] for b in box))