n,m = list(map(int, input().split()))

box = [1] * (n+1) 
redbox = [False] * (n+1) 
redbox[1] = True
for _ in range(m):
    x,y = list(map(int, input().split()))
    box[x]-=1
    box[y]+=1
    if redbox[x]:
        redbox[y] = True
    if box[x]==0:
        redbox[x] = False
#    print(box)
#    print(redbox)
print(sum(map(int, redbox[1:])))