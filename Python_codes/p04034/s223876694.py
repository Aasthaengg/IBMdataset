N, M = map(int, input().split())

red = [0]*N
red[0] = 1
white = [1]*N
white[0] = 0
ans = 1
for i in range(M):
    a, b = map(int, input().split())
    if red[a-1] == 1:
        if red[b-1] == 0:
            red[b-1] += 1
            ans += 1
        else:
            white[b-1] += 1

        if white[a-1] > 0:
            white[a-1] -= 1
        else:
            red[a-1] -= 1
            ans -= 1
    elif white[a-1] > 0:
        white[a-1] -= 1
        white[b-1] += 1
print(ans)
    
        
        
    
