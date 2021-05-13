from functools import lru_cache
N, A = map(int, input().split())
X = [int(x) for x in input().split()]
#with open("9", "w") as f:
#    print(50, 1, file=f)
#    print(*([1]*50), file=f)
assert len(X) == N
def solve0(i, n, s):
    if s < 0:
        return -1
    if N-i+1 < n:
        return -1
    if n == 0:
        if s == 0:
            return 1
        else:
            return -1
    if i == N:
        return -1
    s1 = solve(i+1, n-1,s-X[i])
    s2 = solve(i+1, n, s)
    if s1 == -1 and s2 == -1:
        return -1
    if s1 == -1:
        return s2
    if s2 == -1:
        return s1
    return s1 + s2

cache = {}
def solve(i, n, s):
    key = (i, n, s)
    a = cache.get(key, None)
    if a is None:
        a = solve0(i, n, s)
        cache[key] = a
    return a

answer = 0
for n in range(1, N+1):
    s = solve(0, n, n*A)
    if s != -1:
        answer += s
print(answer)