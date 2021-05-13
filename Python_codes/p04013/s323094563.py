from collections import Counter

X, A = map(int, input().split())
x = [i - A for i in map(int, input().split())]
x.sort()
dp = Counter()

for i in x:
    for j, k in list(dp.items()):
        dp[j + i] = dp[j + i] + k
    dp[i] += 1

print(dp[0])