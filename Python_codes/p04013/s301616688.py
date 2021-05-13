# https://atcoder.jp/contests/abc044/tasks/arc060_a
# ソートしてからごちゃごちゃやればどうにかなりそう(無理でした)

'''
解説満点解法1
もしもk枚選んだとき、合計がsになる通りの数がわかったら？→s=k*Aとなる場合の数の合計をすれば良い

k枚選んだとき、合計がsになる通りの数は典型的なDP！
dp(j,k,s)... X[0:j]からk枚選んで、その合計をsにするような選び方の総数
と定義すると、
dp(j+1,k,s) = X[j]を選んだ結果sになったときの通りの数 + X[j]を選ばずにsになっている通りの数 なので
dp(j+1,k,s) = dp(j,k-1,s-X[j]) + dp(j,k,s)

あとは初期条件と境界条件と伝播条件を付け加える。
境界条件 dp(j,k,0)=0 (数枚選んで合計が0になるのはありえない)
初期条件 dp(j,0,0)=1 (ただし、0枚選んだときは1通りとなる)(s-X[j]=0のときに1通りとなってほしいという気持ちもある)

伝播条件 s-X[j]<0に関しては dp(j-1,k-1,s-X[j])が必ず0通りとなる(ありえないので)
'''

import sys
read = sys.stdin.readline
from itertools import product


def read_ints():
    return list(map(int, read().split()))


N, A = read_ints()
X = read_ints()
S = sum(X)

# 満点解法1
dp = [[[0] * (S + 1) for _ in range(N + 1)] for _ in range(N + 1)]
for j in range(N + 1):  # 初期条件
    dp[j][0][0] = 1  # 1枚も選ばずに0になるのは1通り


for j, k, s in product(range(N), range(1, N + 1), range(S + 1)):
    dp[j + 1][k][s] = dp[j][k][s] + \
        (0 if s - X[j] < 0 else dp[j][k - 1][s - X[j]])

# s=k*Aとなるような通りの数の総数
ans = 0
for k in range(1, N + 1):  # 0個はとる通りの数はいらない
    s = k * A
    if s <= S:
        ans += dp[N][k][s]

# print(dp)
print(ans)


'''
満点解法2


'''
