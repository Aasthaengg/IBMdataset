N = int(input())
L = list(map(int, input().split()))

L.sort()
s = 0

for i in range(len(L) // 2):
    s += L[i * 2]

print(s)