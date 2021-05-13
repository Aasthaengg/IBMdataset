N=int(input())

nowodd = False
ans = 0
for i in range(N):
    a = int(input())
    if nowodd and a>0:
        a-=1
        ans+=1

    if a%2==1:
        nowodd=True
    else:
        nowodd=False
    ans+=a//2
print(ans)