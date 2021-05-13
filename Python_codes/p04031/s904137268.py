def main():
    from collections import Counter
    n, *a = map(int, open(0).read().split())
    c = Counter(a)
    d = list(c.keys())
    x, y = min(d), max(d)
    ans = float("Inf")
    for i in range(x, y + 1):
        tmp = 0
        for k, v in c.items():
            tmp += (k - i) ** 2 * v
        ans = min(ans, tmp)
    print(ans)


if __name__ == '__main__':
    main()
