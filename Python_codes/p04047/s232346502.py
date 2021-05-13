N = int(input())
l = [0] * 2 * N
l = list(map(int, input().split()))
l.sort()
total = 0
for i in range(N):
  total += l[i * 2]
print(total)