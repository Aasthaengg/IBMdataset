N, A = input().split(" ")
N, A = int(N), int(A)
x = input().split(" ")
x = [int(i) for i in x]
y = [0]+[int(i)-A for i in x]
X = max(x+[A])

dp = [[0 for t in range(2*N*X+1)] for j in range(N+1)]

for j in range(N+1):
    for t in range(2*N*X+1):
        if j == 0 and t == N*X:  # 0枚の時は0しか達成できない
            dp[j][t] = 1
        elif j >= 1 and (t - y[j-1] < 0 or t-y[j] > 2*N*X):  # xの値が平均Aを超えてしまう場合は、前回の結果から場合の総数に変化なし
            dp[j][t] = dp[j-1][t]
        elif j >= 1 and 0 <= t-y[j-1] <= 2*N*X:  # 前回の場合の総数に、今回の数を足して0になる場合の総数を足す
            dp[j][t] = dp[j-1][t] + dp[j-1][t-y[j]]
        else:
            dp[j][t] = 0
print(dp[N][N*X] - 1)