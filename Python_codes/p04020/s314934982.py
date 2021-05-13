import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N = in_n()
    A = list(in_na())

    if N == 1:
        print(A[0] // 2)
        exit()

    ans = 0
    for i in range(N):
        if A[i] >= 3:
            if A[i] % 2 == 0:
                ans += (A[i] - 2) // 2
                A[i] = 2
            else:
                ans += (A[i] - 1) // 2
                A[i] = 1

    for i in range(N - 1):
        if A[i] == 2 and A[i + 1] == 0:
            A[i] = 0
            ans += 1
        elif A[i] == 2 and A[i + 1] == 1:
            A[i], A[i + 1] = 0, 1
            ans += 1
        elif A[i] == 2 and A[i + 1] == 2:
            A[i], A[i + 1] = 0, 0
            ans += 2
        elif A[i] == 1 and A[i + 1] == 1:
            A[i], A[i + 1] = 0, 0
            ans += 1
        elif A[i] == 1 and A[i + 1] == 2:
            A[i], A[i + 1] = 0, 1
            ans += 1
        elif A[i] == 0 and A[i + 1] == 2:
            A[i], A[i + 1] = 0, 0
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
