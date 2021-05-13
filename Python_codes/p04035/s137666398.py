#!/usr/bin/env python3


def solve(n, l, xs):
    pair_idx = None
    for i in range(n - 1):
        if xs[i] + xs[i + 1] >= l:
            pair_idx = i
            break
    if pair_idx is None:
        return (False, [])
    ans = [x + 1 for x in range(pair_idx)]
    ans.extend(x + 1 for x in range(pair_idx + 1, n - 1)[::-1])
    ans.append(pair_idx + 1)
    return (True, ans)


def main():
    n, l = map(int, input().split())
    xs = list(map(int, input().split()))
    judge, ans = solve(n, l, xs)
    if not judge:
        print("Impossible")
        return
    print("Possible")
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
