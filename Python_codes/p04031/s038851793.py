#入力
N = int(input())
lst = input().split()

#整数値化
for i in range(len(lst)):
   lst[i] = int(lst[i])

#ソート
lst.sort()

#コスト計算関数
def get_cost(x, y):
   return (x - y) ** 2

costs = []

#コスト計算
for i in range(lst[0], lst[-1]): #入力値の最小値から最大値まで
   cost = 0
   for j in lst:
      cost = cost + get_cost(j, i)
   costs.append(cost)

#ソート
costs.sort()

#最小コストを出力
#入力値が全て同じとき最小も最大も同じなのでfor文の中のやつは1回も実行されない
#つまりcostsリストが空なのでcosts[0]が存在しない
if costs != []:
   print(costs[0])
else:
   print(0)