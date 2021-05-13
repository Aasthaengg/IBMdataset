


N = int(input())
A = [int(input()) for _ in range(N)]

"""
i番目を見ている時に、i+1番目と組にするか考える。
i+1はi+2と組にできるので、残せるなら残す。

"""

ans = 0
for i in range(N):
    if i != N-1:
        tmp = A[i] // 2
        ans += tmp
        A[i] -= tmp*2
        if A[i] != 0 and A[i+1] != 0:
            ans += 1
            A[i] = 0
            A[i+1] -= 1

    else:
        ans += A[i] // 2


print(ans)
