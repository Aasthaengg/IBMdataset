# C - 高橋君とカード / Tak and Cards

#import numpy as np
import math

N, A = map(int, input().split())
x = list(map(int, input().split()))

# 数列aと整数Aを与えると、aからいくつか取って合計Aにするパターンが何通りあるかを返す関数
def partial_sum(a,A):
    n = len(a)
    dp = [[0]*(A+2) for _ in range(n+2)] # dp[i+1][j] a[i]までの数からいくつか選んで総和をjにするパターンの数
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(A+1):
            if j >= a[i]:
                dp[i+1][j] = dp[i][j-a[i]] + dp[i][j]
            else:
                dp[i+1][j] = dp[i][j]
                
    return dp[n][A]

x_diff = [a - A for a in x] # ここから合計0になるように取る。負の数列についてpartial_sumが動かないことに注意
x_diff_negative = [-a for a in x_diff if a < 0]
x_diff_positive = [a for a in x_diff if a > 0]

ans = 0
for i in range(1, min(sum(x_diff_negative), sum(x_diff_positive)) + 1):
    ans += partial_sum(x_diff_negative,i) * partial_sum(x_diff_positive,i) 

# 0の選び方
n_pattern_0 = 0
n_0 = x_diff.count(0)
if n_0 > 0:
    for i in range(1, n_0+1):
        n_pattern_0 += math.factorial(n_0) // (math.factorial(n_0-i) * math.factorial(i))

# ここまで数えた全てのパターンそれぞれについて、x_diff中の0をいくつか含めた別パターンがある
# 0単体で選ぶ方法もある
ans += (ans+1) * n_pattern_0
    
print(ans)