def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = A[0] // 2
    s = A[0] % 2
    for a in A[1:]:
        diff_p = min(s, a)
        self_p = (a - diff_p) // 2
        ans += diff_p + self_p
        s = a - diff_p - 2 * self_p
    print(ans)


if __name__ == '__main__':
    main()