def resolve():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    start, end = min(A), max(A)
    mincost = float("inf")
    for i in range(start, end+1):
        _cost = 0
        for a in A:
            _cost += abs(a-i)**2
        mincost = min(mincost, _cost)
    print(mincost)


if '__main__' == __name__:
    resolve()

