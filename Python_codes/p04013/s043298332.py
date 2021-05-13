# -*- coding: utf-8 -*-
N, A = map(int, input().split(' '))
import collections

X = [int(a) - A for a in input().split(' ')]
sum_positives = sum([x for x in X if x > 0])
sum_negatives = sum([x for x in X if x < 0])

dp = [dict([(i, 0) for i in range(sum_negatives, sum_positives+1)])
            for _ in range(N+1)]
dp[0][0] = 1

for i, x in enumerate(X):
    for j in range(sum_negatives, sum_positives+1):
        dp[i + 1][j] = dp[i][j]
        if (j - x) in dp[i]:
            dp[i + 1][j] += dp[i][j - x]

# for d in dp:
#     print(d)

print(dp[N][0] - 1)
exit()
