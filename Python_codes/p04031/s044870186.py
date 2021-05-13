n=int(input())
a=list(map(int,input().split()))
cost=float("inf")
for j in range(-100,101,1):
    total=0
    for i in range(n):
        total+=(a[i]-j)**2
    if total<cost:
        cost=total
print(cost)