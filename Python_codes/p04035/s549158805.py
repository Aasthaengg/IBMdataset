import heapq
N, K = map(int, input().split())
A = list(map(int, input().split()))

knot = []
for i in range(N - 1):
    heapq.heappush(knot, (-A[i]-A[i+1], i))

ans = []
seen = [False]*N
while knot:
    L, i = heapq.heappop(knot)
    L = -L

    if seen[i]:
        continue
    if L < K:
        break

    seen[i] = True
    ans.append(i + 1)

    if i + 1 < N - 1:
        heapq.heappush(knot, (-L - A[i + 1], i + 1))
    if i - 1 >= 0:
        heapq.heappush(knot, (-L - A[i - 1], i - 1))

if len(ans) != N - 1:
    print("Impossible")
else:
    print("Possible")
    print(*ans[::-1], sep="\n")
