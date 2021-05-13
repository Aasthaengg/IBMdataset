N = int(input())
L = list(map(int, input().split()))

L.sort()

count = 0
for i in range(N):
    count += min(L[2*i], L[2*i+1])

print(count)