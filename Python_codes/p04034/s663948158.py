N,M = map(int,input().split())

moves = [list(map(int,input().split())) for i in range(M)]
isRed = [False for i in range(N)]
isRed[0] = True
Ball = [1 for i in range(N)]

for i in range(M):
    p = moves[i][0] - 1
    q = moves[i][1] - 1

    if isRed[p] == True:
        isRed[q] = True
        Ball[p] -= 1
        Ball[q] += 1
        if Ball[p] < 1:
            isRed[p] = False
        
    else:
        Ball[p] -= 1
        Ball[q] += 1
    
ans = isRed.count(True)

print(ans)
