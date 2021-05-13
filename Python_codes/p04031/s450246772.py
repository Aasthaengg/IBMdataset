n = int(input())
a = list(map(int, input().split()))

ans = 10**9
for num in range(-100, 101):
    temp = 0
    for i in range(n):
        temp += (num - a[i])**2
    ans = min(ans, temp)

print(ans)