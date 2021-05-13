N = int(input())
L = [int(i) for i in input().split()]
L.sort()

ans = 0
for i in range(0, 2 * N, 2):
    ans += L[i]

print(ans)