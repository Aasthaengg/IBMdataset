def solve(n, L):
    L.sort()
    return sum(min(L[2 * i], L[2 * i + 1]) for i in range(n))

_n = int(input())
_L = list(map(int, input().split()))
print(solve(_n, _L))
