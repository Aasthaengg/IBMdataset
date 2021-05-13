# 子供の人数を取得
N = int(input())

# 子供の人数分のキャンディの個数を計算
Childrencnt = 1
Candysum = 0
for Childrencnt in range(1, N+1):
    Candysum = Candysum + Childrencnt

# キャンディの合計個数を出力
else:
    print(Candysum)