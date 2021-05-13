def main():
    n, l = map(int, input().split())
    ss = [list(input()) for _ in range(n)]

    for i in range(l-1, -1, -1):
        ss = sorted(ss, key=lambda x: x[i])

    ans = ''
    for i in range(n):
        for j in range(l):
            ans += ss[i][j]
    print(ans)


if __name__ == "__main__":
    main()
