import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

ans = "Possible"
large_pair = -1
for i in range(N-1):
    if A[i]+A[i+1] >= L:
        large_pair = i
        break
if large_pair == -1:
    ans = "Impossible"
    print(ans)
else:
    order = [large_pair]
    start = large_pair
    left = start-1
    right = start+1

    while left >= 0:
        order.append(left)
        left -= 1

    while right < N-1:
        order.append(right)
        right += 1

    print(ans)
    print("\n".join(map(lambda x: str(x+1), reversed(order))))
