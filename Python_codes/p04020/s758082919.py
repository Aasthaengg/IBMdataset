def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    ans = 0
    for i in range(1, N):
        if A[i-1] > 1:
            ans += A[i-1] // 2
            A[i-1] %= 2
        if A[i-1] & 1 and A[i] > 1:
            ans += 1
            A[i-1] -= 1
            A[i] -= 1
    ans += A[-1] // 2
    print(ans)


if __name__ == '__main__':
    main()
