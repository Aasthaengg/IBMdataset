def main(n: int, l: list):
    ans = 0

    l.sort(reverse=True)

    for _ in range(n):
        a, b = l.pop(), l.pop()
        ans += a

    print(ans)


if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))

    main(n, l)
