n=int(input())

t = list(map(int,input().split()))

ans = 10000000000

for i in range(-100, 101):
    memo = 0
    for j in t:
        memo += (i-j)**2
    ans = min(ans, memo)
print(ans)