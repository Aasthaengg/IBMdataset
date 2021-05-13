n=int(input())
a=list(map(int,input().split()))

mn=10**18
for i in range(-100,101):
    sm=0
    for k in range(n):
        sm+=(a[k]-i)**2
    mn=min(sm,mn)

print(mn)