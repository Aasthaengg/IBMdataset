N, M = map(int, input().split())

num = [1 for i in range(N)]
red = [False for i in range(N)]
red[0] = True

for i in range(M):
    x, y = map(int, input().split())    
    x -= 1
    y -= 1
    
    if(red[x] and num[x] >= 1):
        red[y] = True
        num[x] -= 1
        num[y] += 1
        if(num[x] <= 0):
            red[x] = False
    else:
        if(num[x]):
            num[x] -= 1
            num[y] += 1

print(red.count(True))  