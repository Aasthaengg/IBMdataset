n, a = map(int, input().split())
X = list(map(int, input().split()))

# editorial 参照 -> 3 dimentional DP
# 制約1: x1-xjのカード, 制約2: k枚選択, 制約3: 点数合計A*k
sum_X = sum(X)
DP = [[[0 for _ in range(sum_X+1)] for _ in range(n+1)] for _ in range(n+1)]


for j in range(n+1):
    for k in range(n+1):
        for s in range(sum_X+1):
            if (j==0) and (k==0) and (s==0):
                DP[j][k][s] = 1
            elif (j >= 1) and (s < X[j-1]):
                DP[j][k][s] = DP[j-1][k][s]
            elif (j >= 1) and (k >= 1) and (s >= X[j-1]):
                DP[j][k][s] = DP[j-1][k][s] + DP[j-1][k-1][s-X[j-1]]
            else:
                DP[j][k][s] = 0

ans  = 0
for k in range(1, n+1):
    if a*k > sum_X:
        pass
    else:
        ans += DP[n][k][a*k]

print(ans)