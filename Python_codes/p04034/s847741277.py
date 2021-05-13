n,m = map(int,input().split())
xy = [[int(i) for i in input().split()] for _ in range(m)]
num = [1]*n
red = [False]*n
red[0] = True
flag = True
for i in range(m):
    p = xy[i][0]
    q = xy[i][1]
    num[p-1] -= 1
    num[q-1] += 1
    if red[p-1]==True:
        red[q-1] = True
    
    if num[p-1]==0:
        red[p-1] = False
        

count = 0
for i in range(n):
    if num[i]>0 and red[i]:
        count += 1
print(count)