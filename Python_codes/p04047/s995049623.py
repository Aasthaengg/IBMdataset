N = int(input())
L = list(map(int, input().split()))
res = 0
L.sort()
for i in range(len(L)%2, len(L), 2):
    res += L[i]

print(res)
