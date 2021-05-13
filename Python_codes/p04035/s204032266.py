
def knot(N, L, a):
    res = []
    for i in range(N - 1):
        if a[i] + a[i + 1] >= L:
            res.append(i + 1)
            start = i
            break
    else:
        return res

    for i in range(start + 1, N - 1):
        res.append(i + 1)
    for i in range(start - 1, -1, -1):
        res.append(i + 1)
    return res


if __name__ == "__main__":
    N, L = map(int, input().split())
    a = list(map(int, input().split()))
    knot = knot(N, L, a)
    if not knot:
        print("Impossible")
    else:
        print("Possible")
        print(*knot[::-1], sep="\n")
