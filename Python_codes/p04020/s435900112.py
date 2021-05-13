N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0
for key,val in enumerate(A):
    ans += int(val/2)

    if key < N-1 and int(val/2)*2 != val and A[key+1] != 0:
        A[key+1] -= 1
        ans += 1
print(ans)