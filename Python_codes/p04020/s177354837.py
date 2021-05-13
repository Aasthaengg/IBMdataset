N=int(input())
former=0
ans=0
for i in range(0,N):
    a=int(input())
    if former==0:
        former=a%2
        ans+=a//2
    else:
        if a%2==0:
            if a!=0:
                former=1
                ans+=a//2
            else:
                former=0
        else:
            former=0
            ans+=a//2+1

print(ans)