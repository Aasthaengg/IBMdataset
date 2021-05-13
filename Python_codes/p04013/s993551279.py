from collections import Counter
N,A = map(int, input().split())
X = list(map(int, input().split()))

"""
普通にやると最大で2**50通りなのでTLE
i枚選んだ時に合計がi*Aになる物を考えるとよい
prd_xxxさんの解答に自分向けのコメントつけただけ
https://atcoder.jp/contests/abc044/submissions/3018277
"""

# 0枚からN枚まで選んで、合計値がkeyでその組み合わせの数がvalue
dp = [Counter() for _ in range(N+1)]
dp[0][0] = 1

for i, a in enumerate(X): # i番目のカードまで選べる
    for j in reversed(range(i+1)): # j枚選ぶとき（０～i枚の範囲）、逆順にしないと１枚目にX_iを選んで３枚目にもX_iを選ぶみたいな重複が発生するのでこれを回避するために逆順にする
        for k,v in dp[j].items(): # j枚選んだ時の合計値とその組み合わせの個数についてみていく
            dp[j+1][k+a] += v # j+1枚目としてi番目のカードを選ぶ時に合計がk+aになる個数は、j枚選んでｋになる個数と同じ（それぞれの場合にaを足してできる）

ans = 0
for i, C in enumerate(dp):
    if i >= 1:
        ans += C[i*A]
print(ans)