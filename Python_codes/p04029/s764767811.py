# 43a
# 競プロ幼稚園には N 人の子供がいます。えび先生は、
# 子供たちを一列に並べ、一人目にはキャンディーを
# 1個,二人目には2個,..., N 人目にはN個あげることにしました。
# 必要なキャンディーの個数の合計は何個でしょう?

# Nに入力された数字を格納する
N = int(input())

# answer(計算結果を格納するところ)を定義
answer = 0


# while文で 1以上100以下の数字で値を繰り返し処理
# Nの値をanswerに＋するたびにNの値から-1するようにする
while 1 <= N <= 100:
    answer = answer + N
    N = N - 1

print(answer)