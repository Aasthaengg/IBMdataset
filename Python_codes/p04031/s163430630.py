n = int(input())
a = list(map(int,input().split()))

ans =10**8
for i in range(-100,101):
    cost = 0
    for k in a:
        cost += (k-i)**2
    ans = min(cost,ans)

print(ans)
