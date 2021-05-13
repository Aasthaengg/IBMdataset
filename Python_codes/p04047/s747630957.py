import heapq
n = int(input())
src = list(map(int, input().split()))
sorted_src = sorted(src)
heapq.heapify(sorted_src)
count = 0
for i in range(n):
    a = heapq.heappop(sorted_src)
    heapq.heappop(sorted_src)
    count += a
print(count)