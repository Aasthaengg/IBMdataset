N, M = map(int, input().split())
X = [0] * (M)
Y = [0] * (M)

started = False
contains_red = set([1])
ans = 1

nums = [1] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    X[_] = x
    Y[_] = y

for _ in range(M):
    nums[X[_]] -= 1
    nums[Y[_]] += 1

    if X[_] in contains_red:
        contains_red.add(Y[_])

    if nums[X[_]] == 0 and X[_] in contains_red:
        contains_red.remove(X[_])

# print(contains_red)
print(len(contains_red))
