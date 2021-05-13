N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N*2):
    if i % 2 == 0:
        ans += L[i]
print(ans)