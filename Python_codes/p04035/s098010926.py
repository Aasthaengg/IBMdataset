# 2019/09/18

n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
res=[]
last=0

flag=False
for i in range(n-1):
    if flag:
        res.append(i+1)
        continue
    if a[i]+a[i+1]<k:
        ans.append(i+1)
    elif not flag:
        last=i
        flag=True

if not flag:
    print('Impossible')
    exit()
if res:
    for e in res[::-1]:
        ans.append(e)
ans.append(last+1)

print('Possible')
print(*ans,sep='\n')