N = int(input())
L = list(sorted(map(int, input().split())))

ans = 0
for i in range(0, 2 * N, 2):
    ans += min(L[i], L[i + 1])
print(ans)
