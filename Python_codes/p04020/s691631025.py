import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = [0] * N
    for i in range(N):
        A[i] = int(input())

    if N == 1:
        ans = A[0] // 2
    else:
        ans = 0
        for i in range(N - 1):
            if A[i + 1] == 0:
                ans += A[i] // 2
            else:
                q, r = divmod(A[i] + A[i + 1], 2)
                ans += q
                A[i + 1] = r

    print(ans)


if __name__ == "__main__":
    main()
