N=int(input())

ans=0
co=0
for i in range(N):
    a=int(input())
    ans+=(a+co)//2
    if a==0:
        co=0
    else:
        co=(a+co)%2
print(ans)
