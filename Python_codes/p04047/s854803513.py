N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(0,N,2):
    ans += L[i]
L.sort(reverse=True)
for i in range(1,N,2):
    ans += L[i]
print(ans)
