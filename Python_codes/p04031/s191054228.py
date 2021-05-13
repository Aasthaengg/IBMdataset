ans=0
n=int(input())
res=0
a=list(map(int,input().split()))
b=sum(a)//n
c=b+1
for i in a:
    ans+=abs(i-b)**2
    res+=abs(i-c)**2
print(min(ans,res))