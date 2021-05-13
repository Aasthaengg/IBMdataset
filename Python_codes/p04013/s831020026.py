n, a = map(int, input().split())
x = list(map(int, input().split()))

'''
辞書がめっちゃ書きやすい！ただし、3次元配列でdpやりたい時むずいかも。
x = [i-a for i in x]
dp = {0:1}
print(dp)
for item in x:
    print('--------for item:{}-----------'.format(item))
    for key, value in list(dp.items()):
        print('key:{},value:{}'.format(key,value))
        dp[item + key] = dp.get(item + key, 0) + value
        print(dp)
print(dp[0]-1)
'''

diff = [i-a for i in x]
ma = max(max(x),a)

dp = [[0 for j in range(2*n*ma+1)] for k in range(n+1)]
# 0を初期値として1からNまでやりたいので結果の箱は1+n回ループを回す準備をする。
# print(dp[1][71])
# この初期化をした時に添字はどっちがどっちみたいのはいい加減覚える。
# 0~2*n*naまでの列がn+1倍なのでそれがn+1個並んでいるイメージ。最初の添字ではn+1個並んでいるうちの一つを指定する。

dp[0][n*ma] = 1
# initialize

for l in range(0,n):
    # diff(入力の全てからaを引いたやつ)は0~n-1までしかないことに注意
    # 同様に後ろのdpの添字も注意
    for m in range(2*n*ma+1):
        if abs(m - diff[l]) > 2*n*ma:
            dp[l+1][m] = dp[l][m]
            #ループ回すまでもなく選んでも無理な時はそのまま 
        else:
            dp[l+1][m] = dp[l][m] + dp[l][m - diff[l]]
print(dp[n][n*ma]-1)



'''
countzero = len([i for i in diff if i == 0])
#print(countzero)
over = sorted([i for i in diff if i > 0])
under = sorted([i for i in diff if i < 0])
#print(over)
#print(under)
countover = [0 for i in range(50)]
countunder = [0 for i in range(50)]
for item in set(over):
    countover[item-1] = over.count(item)
for item in set(under):
    countunder[item] = under.count(item)
countunder = sorted(countunder)

valover = [countover[0]]
valunder = [countunder[0]]

for i in range(1,2500):
    plus = 0
    minus = 0
    if i%2 == 0:
        plus = countover[int(i/2)]*(countover[int(i/2)]-1)/2
        minus = countunder[int(i/2)]*(countunder[int(i/2)]-1)/2
    for j in range(int(i/2)):
        plus += countover[i]*countover[-i]
        minus += countunder[i]*countunder[-i]
    valover.append(plus)
    valunder.append(minus)

plusminus = 0
for i in range(2500):
    plusminus += valover[i]*valunder[i]

print((plusminus+1)*2**(countzero)-1)
'''