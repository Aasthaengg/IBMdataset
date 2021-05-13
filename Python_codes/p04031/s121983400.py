n = int(input())
arr = list(map(int, input().split()))

ans = 10**18

for y in range(-100, 101):
    ans = min(ans, sum([(x - y) ** 2 for x in arr]))
print(ans)