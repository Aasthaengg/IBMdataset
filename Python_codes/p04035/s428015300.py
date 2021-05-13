n,l = map(int,input().split())
r = list(map(int,input().split()))
o = 0
flag = 1
for i in range(1,n):
    lr = r[i-1] +r[i]
    if lr >= l:
        o = i
        flag = 0
        break
if flag == 0:
    print('Possible')
    for j in range(1,o):
        print(j)
    for k in range(n-1,o,-1):
        print(k)
    print(o)
else:
    print('Impossible')