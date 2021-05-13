N = int(input())
L = list(map(int, input().split()))
L.sort()

sum = 0
for i in range(N * 2):
  if i % 2 == 1:
    sum += min(L[i-1], L[i])

print(sum)
