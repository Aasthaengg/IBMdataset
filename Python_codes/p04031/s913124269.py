N = int(input())
A = list(map(int, input().split()))

ans = float('inf')
for k in range(-100, 101):
    cnt = 0
    for a in A:
        cnt += pow(a - k, 2)
    ans = min(ans, cnt)

print(ans)
