n=int(input())
a=list(map(int,input().split()))
mean=sum(a)//n
ans=float('inf')
for i in range(5):
    t=(mean-2)+i
    tmp=0
    for j in range(n):
        tmp+=(a[j]-t)**2
    ans=min(ans,tmp)
print(ans)