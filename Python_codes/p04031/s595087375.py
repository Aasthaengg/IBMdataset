N = int(input())
A = list(map(int, input().split(' ')))
ans = []
if A.count(A[0]) == len(A):
    print(0)
    exit(0)
for i in range(-100,101):
    cost = 0
    for j in range(N):
        if A[j] == i:
            continue
        else:
            cost += (A[j] - i)**2
    ans.append(cost)
import heapq
heapq.heapify(ans)
print(heapq.heappop(ans))