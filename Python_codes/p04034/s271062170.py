n , m = map(int,input().split())
aka = [False for i in range(n+1)]
kazu = [1 for i in range(n+1)]
aka[1] = True
for i in range(m):
    x , y = map(int,input().split())
    if aka[x]:
        if kazu[x] >= 2:
            kazu[x] -= 1
            kazu[y] += 1
        elif kazu[x] == 1:
            kazu[x] -= 1
            kazu[y] += 1            
            aka[x] = False
        aka[y] = True
    elif not aka[x]:
        kazu[x] -= 1
        kazu[y] += 1
ans = 0
for i in range(1,n+1):
    if aka[i]:
        ans += 1
print(ans)