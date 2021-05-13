import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

large_pair = -1
# 一つでもA[i]+A[i+1]>=Lとなるところが存在すれば、そこを最後まで残して、他を全部解けばいい
for i in range(N-1):
    if A[i]+A[i+1] >= L:
        large_pair = i
        break

if large_pair == -1:
    ans = "Impossible"
    print(ans)
else:
    # 解く順を逆から辿っていく
    ans = "Possible"
    order = [large_pair]
    for a in reversed(range(large_pair)):
        order.append(a)
    for a in range(large_pair+1, N-1):
        order.append(a)

    print(ans)
    print("\n".join(map(lambda x: str(x+1), reversed(order))))
