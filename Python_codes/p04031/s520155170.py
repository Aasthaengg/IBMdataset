n = int(input())
A = list(map(int, input().split()))

ans = 1000000000

for i in range(-101, 101):
    tmp = 0
    for j in range (n):
        tmp += (i - A[j]) * (i - A[j])
    ans = min(ans, tmp)

print(ans)
