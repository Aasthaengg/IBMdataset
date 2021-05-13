N = int(input())
an = list(map(int, input().split()))

cost = 10000*N
ans = 10000*N
for i in range(-100,100+1):
    cost = sum([(j - i)**2 for j in an])
    ans = min(ans, cost)

print(ans)