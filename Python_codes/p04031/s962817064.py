n=int(input())
a=list(map(int,input().split()))
ans=10**18
for i in range(min(a),max(a)+1):
    x=0
    for j in range(n):
        x+=(a[j]-i)**2
    if ans>x:
        ans=x
print(ans)