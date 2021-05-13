n=int(input())
ans=int(0)
s=int(0)
for i in range(n):
    now=int(input())
    if now==0:
        ans+=int(s/2)
        s=int(0)
    else:
        s+=now
ans+=int(s/2)
print(ans)