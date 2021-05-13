n=int(input())
ans=0
tmp=0
for i in range(n):
    t=int(input())
    ans+=(tmp+t)//2
    tmp=(tmp+t)%2
    if t==0:
        tmp=0
print(ans)