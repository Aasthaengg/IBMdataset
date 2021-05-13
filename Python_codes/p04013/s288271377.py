# N枚のカード
# 平均aにしたい
n, a = map(int, input().split())
# 手持ちのカード
x = list(map(int, input().split()))
 
# aとの差を記録してリストに入れなおす
# 「選んだカードの xi の平均が A」であることは，
# 「選んだカードの (xi − A) の合計が 0」と言い換えることができる．
x = list(map(lambda i: i-a, x))
#print(x)
 
# dp初期値(辞書型)
# dp[0] = 1という意味
dp = {0: 1}

#xから1枚取り出す
for i in x:
    #dpにあるすべてのkey,valueに対して、
    #すでにdpにkeyがi+kのデータがあればそのvalue、なければ,0を返し、
    #それ+vをdpとする。
    
    # k=key
    # v=dp[key]のvalue
    for k,v in list(dp.items()):
        dp[i+k]=dp.get(i+k,0)+v
    
    #print(dp)

#全部使わない選択肢だけ、回答から除外する
print(dp[0]-1)
#print(dp)