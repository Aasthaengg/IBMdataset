N = int(input())
A = list(map(int,input().split()))
ans = float('inf')
for i in range(-100, 101):
    cnt = 0
    for a in A:
        cnt += (a - i) ** 2
    ans = min(ans, cnt)
print(ans)