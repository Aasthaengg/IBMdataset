N=int(input())
a=list(map(int, input().split()))
ans = float("inf")

for num in range(-100, 101):
    tmp = sum([(a[i]-num)**2 for i in range(N)])
    ans = min(ans, tmp)
print(ans)