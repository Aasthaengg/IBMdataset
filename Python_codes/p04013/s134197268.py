from functools import lru_cache

N, A = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(lambda i: i - A, x))
X = max(max(x), A)

@lru_cache(maxsize=None)
def solve(j, t):
    global y
    if j == 0 and t == 0:
        return 1
    elif j >= 1 and (t < y[j - 1] - N * X or t > y[j - 1] + N * X):
        return solve(j - 1, t)
    elif j >= 1 and t >= y[j - 1] - N * X and t <= y[j - 1] + N * X:
        return solve(j - 1, t) + solve(j - 1, t - y[j - 1])
    else:
        return 0

print(solve(N, 0) - 1)
