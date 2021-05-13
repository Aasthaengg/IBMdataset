
def resolve():
    N = int(input())
    A = [int(input()) for _ in range(N)] + [0]

    ans = 0
    for i in range(N):
        ans += A[i] // 2
        A[i] %= 2
        if A[i] > 0 and A[i + 1] > 0:
            ans += 1
            A[i] -= 1
            A[i + 1] -= 1

    print(ans)


if __name__ == "__main__":
    resolve()