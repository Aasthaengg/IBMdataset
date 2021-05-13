N=int(input())
have=0
ans=0
for i in range(N):
    a=int(input())
    now=a+have
    if a==0:
        have=0
    else:
        have=now%2
    ans+=now//2

print(ans)