n,l = map(int,input().split())
L = list(map(int,input().split()))
flag = False
cur = 0
for i in range(n-1):
    if L[i]+L[i+1] >= l:
        flag = True
        cur = i+1
        break
if flag:
    print('Possible')
    for i in range(1,cur):
        print(i)
    for i in range(n-1,cur,-1):
        print(i)
    print(cur)
else:
    print('Impossible')