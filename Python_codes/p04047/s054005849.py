import heapq

N = int(input())
L = input().split()
L = [int(a) for a in L]

heapq.heapify(L)

sum = 0

for i in range(N):
    k1 = heapq.heappop(L)
    k2 = heapq.heappop(L)
    sum += k1

print(sum)
