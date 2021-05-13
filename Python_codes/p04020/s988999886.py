import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)] + [0]

ans = 0
for i in range(N):
    # できるだけ左でペアを作る
    Lpair = A[i] // 2
    ans += Lpair
    A[i] -= 2 * Lpair

    if A[i] > 0 and A[i + 1] > 0:
        ans += 1
        A[i] -= 1
        A[i + 1] -= 1


print(ans)
